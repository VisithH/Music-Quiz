import sqlite3
import os



class Reader:

    databaseLoc: str

    def __init__(self, givenDatabaseLoc: str):

        """
        .. method:: __init__(givenDatabaseLoc: str)

        Initializes the database connection with the given database file location.

        :param givenDatabaseLoc: The file path of the database.
        :type givenDatabaseLoc: str
        """

        self.databaseLoc = givenDatabaseLoc

    def RunQuery(self, query: str, data:list = []):

        """
        .. method:: RunQuery(query: str, data: list = [])

        Executes a SQL query on the database and returns the fetched results.

        :param query: The SQL query to be executed.
        :type query: str
        :param data: Optional list of parameters to be used in the query.
        :type data: list
        :return: The fetched results from the query execution.
        :rtype: list
        """

        db = sqlite3.connect(self.databaseLoc)
        data = db.execute(query, data)
        result = data.fetchall()
        db.commit()
        db.close()
        return result
    
    def GetSongMetadata(self, songId: int):

        """
        .. method:: GetSongMetadata(songId: int)

        Retrieves metadata for a given song, including its name, album, and associated artists.

        :param songId: The ID of the song to retrieve metadata for.
        :type songId: int
        :return: A list containing the song name, album name, and a list of associated artist names.
        :rtype: list
        """

        md = self.RunQuery("""SELECT SongData.songName, AlbumData.albumName 
                           FROM SongData 
                           INNER JOIN AlbumData ON SongData.albumId = AlbumData.id 
                           WHERE SongData.id = ?""", [songId])
        
        md = list(md[0])
        
        ar = self.RunQuery("""SELECT ArtistData.artistName 
                           FROM SongData 
                           INNER JOIN ArtistSongLink ON SongData.id = ArtistSongLink.songId 
                           INNER JOIN ArtistData ON ArtistSongLink.artistId = ArtistData.id 
                           WHERE SongData.id = ?""", [songId])
        
        ar = [i[0] for i in ar]

        return md + [ar]


    def GetSongLyrics(self, songId: int):

        """
        .. method:: GetSongLyrics(self, songId: int)
        
        Retrieves the lyrics of a song from the database based on the provided song ID.

        This method queries the database for the lyrics of a specific song identified by its `songId`.

        :param songId: The ID of the song whose lyrics are to be fetched.
        :type songId: int
        :return: The lyrics of the specified song.
        :rtype: str
        """
        
        return self.RunQuery("""SELECT SongData.lyrics 
                             FROM SongData 
                             WHERE SongData.id = ?""", [songId])[0][0]
    
    def GetPackMetadata(self, packId: int):

        """
        .. method:: GetPackMetadata(self, packId: int)

        Retrieves the pack name and author username from the database based on the provided pack ID.

        This method queries the database to fetch the pack name and the associated author username
        for a specific pack identified by its `packId`.

        :param packId: The ID of the pack whose details are to be fetched.
        :type packId: int
        :return: A list containing the pack name and the author's username.
        :rtype: list of str
        """

        return list(self.RunQuery("""SELECT PackData.packName, AuthorData.authorUsername 
                                  FROM PackData 
                                  INNER JOIN AuthorData ON PackData.packAuthorId = AuthorData.id 
                                  WHERE PackData.id = ?""", [packId])[0])
    

    def GetPackSongsData(self, packId: int):
        
        """
        .. method:: GetPackSongsData(self, packId: int)

        Retrieves the song IDs, lyric line numbers, and lyric word numbers associated with a specific pack.

        This method queries the database to fetch song data (song ID, lyric line number, and lyric word number)
        for songs linked to a specific pack identified by its `packId`.

        :param packId: The ID of the pack whose songs' data is to be fetched.
        :type packId: int
        :return: A list of tuples, each containing a song ID, lyric line number, and lyric word number.
        :rtype: list of tuple
        """

        return list(self.RunQuery("""SELECT songId, lyricLineNumber, lyricWordNumber 
                                  FROM PackSongLink 
                                  WHERE packId = ?""", [packId]))


    def GetAllPacks(self):

        """
        .. method:: GetAllPacks()

        Retrieves a list of all pack IDs from the database.

        :return: A list of pack IDs.
        :rtype: list of int
        """

        data = self.RunQuery("""SELECT id 
                             FROM PackData""")
        
        data = [i[0] for i in data]
        return data


# BELOW IS FOR TESTING
if __name__ == "__main__":

    # Create a reader object to interact with the database
    test: Reader = Reader((os.path.dirname(os.path.realpath(__file__))+"/Quiz Songs.db"))
    
    # Go through each pack in the database
    for packId in test.GetAllPacks():

        # Print the name of the pack and the author's name
        print(" - ".join(test.GetPackMetadata(packId)))

        print()

        # Go through each song in the current pack
        for songData in test.GetPackSongsData(packId):
            # Print the song's details like song name, album name, and artist(s)
            # If there are multiple artists, show them separated by commas
            print(" - ".join([str(i) if type(i) != list else ", ".join(i) for i in test.GetSongMetadata(songData[0])]))
            print(songData[0])

            # Get the lyrics for this song, split them into lines, and pick the correct line
            line = test.GetSongLyrics(songData[0]).split("\n")[songData[1]]

            # Find the word to replace based on the lyric word number
            blank = line.split(" ")[songData[2]]

            # Replace the word with "____" (a blank) and print the modified line
            print(line.replace(blank, "____"))
            # Also print the blank (answer)
            print("("+blank+")")

            print()

        print()

            
        

