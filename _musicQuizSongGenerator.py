import sqlite3



class Generator:

    """
    A class to manage and interact with a music database, performing operations such as adding artists, albums, songs,
    authors, and packs. It provides methods for inserting data into the database, creating necessary relationships 
    between entities, and generating required database tables if they do not already exist.

    The following tables are managed by this class:
    
    - **ArtistData**: Stores artist information.
    - **AlbumData**: Stores album information.
    - **SongData**: Stores song details, including album association and lyrics.
    - **ArtistSongLink**: Establishes a many-to-many relationship between artists and songs.
    - **AuthorData**: Stores information about authors.
    - **PackData**: Represents song packs, linked to authors.
    - **PackSongLink**: Links songs to packs with lyric position details.

    This class assumes that the underlying database is an SQLite database, and it performs SQL queries to interact 
    with the database.
    
    :param givenDatabaseLoc: The location of the SQLite database file.
    :type givenDatabaseLoc: str
    :ivar databaseLoc: The location of the SQLite database file.
    :vartype databaseLoc: str
    """

    databaseLoc: str

    def __init__(self, givenDatabaseLoc: str):

        """Constructor method
        """

        self.databaseLoc = givenDatabaseLoc
        self.GenerateTables()

    def GenerateTables(self):

        """
        .. method:: GenerateTables()

        Creates the necessary database tables if they do not already exist.

        This method initializes the following tables:
        
        - **ArtistData**: Stores artist information.
        - **AlbumData**: Stores album information.
        - **SongData**: Stores song details, including album association and lyrics.
        - **ArtistSongLink**: Establishes a many-to-many relationship between artists and songs.
        - **AuthorData**: Stores information about authors.
        - **PackData**: Represents song packs, linked to authors.
        - **PackSongLink**: Links songs to packs with lyric position details.

        :return: None
        :rtype: None
        """

        self.RunQuery("""CREATE TABLE IF NOT EXISTS ArtistData(
            id INTEGER PRIMARY KEY NOT NULL, 
            artistName TEXT NOT NULL
        )""")

        self.RunQuery("""CREATE TABLE IF NOT EXISTS AlbumData(
            id INTEGER PRIMARY KEY NOT NULL, 
            albumName TEXT NOT NULL
        )""")

        self.RunQuery("""CREATE TABLE IF NOT EXISTS SongData(
            id INTEGER PRIMARY KEY NOT NULL, 
            songName TEXT NOT NULL, 
            albumId INTEGER NOT NULL, 
            lyrics TEXT NOT NULL, 
            FOREIGN KEY (albumId) REFERENCES AlbumData(id)
        )""")

        self.RunQuery("""CREATE TABLE IF NOT EXISTS ArtistSongLink(
            artistId INTEGER NOT NULL, 
            songId INTEGER NOT NULL, 
            FOREIGN KEY (artistId) REFERENCES ArtistData(id), 
            FOREIGN KEY (songId) REFERENCES SongData(id)
        )""")

        self.RunQuery("""CREATE TABLE IF NOT EXISTS AuthorData(
            id INTEGER PRIMARY KEY NOT NULL, 
            authorUsername TEXT NOT NULL
        )""")

        self.RunQuery("""CREATE TABLE IF NOT EXISTS PackData(
            id INTEGER PRIMARY KEY NOT NULL, 
            packName TEXT NOT NULL, 
            packAuthorId INTEGER NOT NULL, 
            FOREIGN KEY (packAuthorId) REFERENCES AuthorData(id)
        )""")

        self.RunQuery("""CREATE TABLE IF NOT EXISTS PackSongLink(
            packId INTEGER NOT NULL, 
            songId INTEGER NOT NULL, 
            lyricLineNumber INTEGER NOT NULL, 
            lyricWordNumber INTEGER NOT NULL, 
            PRIMARY KEY (packId, songId), 
            FOREIGN KEY (packId) REFERENCES PackData(id), 
            FOREIGN KEY (songId) REFERENCES SongData(id)
        )""")

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


    def InsertAuthor(self, authorName: str):

        """
        .. method:: InsertAuthor(authorName: str)

        Inserts a new author into the database and returns the generated author ID.

        :param authorName: The username of the author to be added.
        :type authorName: str
        :return: The ID of the newly inserted author.
        :rtype: int
        """

        return self.RunQuery("INSERT INTO AuthorData(authorUsername) VALUES (?) RETURNING id", [authorName])[0][0]

    def InsertArtist(self, artistName: str):

        """
        .. method:: InsertArtist(artistName: str)

        Inserts a new artist into the database and returns the generated artist ID.

        :param artistName: The name of the artist to be added.
        :type artistName: str
        :return: The ID of the newly inserted artist.
        :rtype: int
        """

        return self.RunQuery("INSERT INTO ArtistData(artistName) VALUES (?) RETURNING id", [artistName])[0][0]

    def InsertAlbum(self, albumName: str):

        """
        .. method:: InsertAlbum(albumName: str)

        Inserts a new album into the database and returns the generated album ID.

        :param albumName: The name of the album to be added.
        :type albumName: str
        :return: The ID of the newly inserted album.
        :rtype: int
        """

        return self.RunQuery("INSERT INTO AlbumData(albumName) VALUES (?) RETURNING id", [albumName])[0][0]
    
    def InsertSong(self, songName: str, artistNames: list[str], albumName: str, lyrics: str, packLink: list=None):

        """
        .. method:: InsertSong(songName: str, artistNames: list[str], albumName: str, lyrics: str, packLink: list = None)

        Inserts a new song into the database, linking it to an album and artists, and optionally links it to a pack.

        :param songName: The name of the song to be added.
        :type songName: str
        :param artistNames: A list of artist names associated with the song.
        :type artistNames: list of str
        :param albumName: The name of the album the song belongs to.
        :type albumName: str
        :param lyrics: The lyrics of the song.
        :type lyrics: str
        :param packLink: Optional list containing the pack ID, lyric line number, and lyric word number to link the song to a pack. Example: [1, 12, 5] links to pack with ID 1, lyric line 12, and word 5.
        :type packLink: list, optional
        :return: The ID of the newly inserted song.
        :rtype: int
        """

        # packLink takes the form [packId, lyricLineNumber, lyricWordNumber]

        albumId = self.RunQuery("SELECT id FROM albumData WHERE albumName = ?", [albumName])

        if len(albumId) > 0:
            albumId = albumId[0][0]
        else:
            albumId = self.InsertAlbum(albumName)

        

        songId = self.RunQuery("INSERT INTO SongData(songName, albumId, lyrics) VALUES (?, ?, ?) RETURNING id", [songName, albumId, lyrics])[0][0]

        for aName in artistNames:

            artistId = self.RunQuery("SELECT id FROM artistData WHERE artistName = ?", [aName])
            
            if len(artistId) > 0:
                artistId = artistId[0][0]
            else:
                artistId = self.InsertArtist(aName)

            self.RunQuery("INSERT INTO ArtistSongLink(artistId, songId) VALUES (?, ?)", [artistId, songId])

        if packLink is not None:
            self.LinkSongToPack(packLink[0], songId, packLink[1], packLink[2])
        else:
            return songId
    
    def CreatePack(self, packName, authorUsername):

        """
        .. method:: CreatePack(packName: str, authorUsername: str)

        Creates a new pack and associates it with an author. If the author doesn't already exist, they will be created.

        :param packName: The name of the pack to be created.
        :type packName: str
        :param authorUsername: The username of the author creating the pack.
        :type authorUsername: str
        :return: The ID of the newly created pack.
        :rtype: int
        """


        authorId = self.RunQuery("SELECT id FROM authorData WHERE authorUsername = ?", [authorUsername])
        if len(authorId) > 0:
            authorId = authorId[0][0]
        else:
            authorId = self.InsertAuthor(authorUsername)

        return self.RunQuery("INSERT INTO PackData(packName, packAuthorId) VALUES (?, ?) RETURNING id", [packName, authorId])[0][0]
    


    def LinkSongToPack(self, packId, songId, lyricLineNumber, lyricWordNumber):

        """
        .. method:: LinkSongToPack(packId: int, songId: int, lyricLineNumber: int, lyricWordNumber: int)

        Links a song to a pack, specifying the lyric line and word number.

        :param packId: The ID of the pack to which the song is being linked.
        :type packId: int
        :param songId: The ID of the song being linked to the pack.
        :type songId: int
        :param lyricLineNumber: The line number of the lyric to associate with the pack.
        :type lyricLineNumber: int
        :param lyricWordNumber: The word number within the line to associate with the pack.
        :type lyricWordNumber: int
        :return: None
        :rtype: None
        """

        self.RunQuery("INSERT INTO PackSongLink(packId, songId, lyricLineNumber, lyricWordNumber) VALUES (?, ?, ?, ?)", [packId, songId, lyricLineNumber, lyricWordNumber])


    def GetSongId(self, songName, artistName):

        return self.RunQuery("""SELECT SongData.id FROM SongData 
                             INNER JOIN ArtistSongLink ON SongData.id = ArtistSongLink.songId 
                             INNER JOIN ArtistData ON ArtistSongLink.artistId = ArtistData.id 
                             WHERE SongData.songName = ? 
                             AND ArtistData.artistName = ?""", [songName, artistName])[0][0]


