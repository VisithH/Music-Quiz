import sys

from _musicQuizDatabase import Reader
import os
import tkinter as tk

test: Reader = Reader((os.path.dirname(os.path.realpath(__file__)) + "/Quiz Songs.db"))


class EntryFrame(tk.Frame):
    usernameEntry: tk.Entry
    passwordEntry: tk.Entry

    def __init__(self, windowRef: tk.Tk, oldFrame: tk.Frame = None):
        if oldFrame is not None:
            oldFrame.destroy()
        super().__init__(windowRef)
        self.Setuplayout()
        self.pack(fill="both", expand=True)

    # def loopforQuizID(self, quizID):
    #     self.quizID = quizID
    #     print(" - ".join(test.GetPackMetadata(self.quizID)))  # The Title of the quiz
    #
    #     for songData in test.GetPackSongsData(self.quizID):
    #         # Print the song's details like song name, album name, and artist(s)
    #         # If there are multiple artists, show them separated by commas
    #         artistName = " - ".join(
    #             [str(i) if type(i) != list else ", ".join(i) for i in test.GetSongMetadata(songData[0])])
    #
    #         # Get the lyrics for this song, split them into lines, and pick the correct line
    #         line = test.GetSongLyrics(songData[0]).split("\n")[songData[1]]
    #
    #         # Find the word to replace based on the lyric word number
    #         blank = line.split(" ")[songData[2]]
    #
    #         # Replace the word with "____" (a blank) and print the modified line
    #         print(line.replace(blank, "____"))
    #         # Also print the blank (answer)

    # def Setuplayout(self):
    #     # for data in test.GetPackMetadata(2): print(data, end="".join(" - "))
    #     self.quizID = 1
    #     # name of the quiz
    #     tk.Label(self, text=f"{" - ".join(test.GetPackMetadata(self.quizID))}").grid(row=0, column=0)
    #
    #     #Number of the quiz
    #     tk.Label(self, text="Question 1").grid(row=1, column=0)
    #
    #     self.songName = test.GetSongMetadata(2)
    #     #name of the song and artist
    #     # tk.Label(self, text=f"{" - ".join([str(i) if type(i) != list else ", ".join(i) for i in test.GetSongMetadata(2)])}").grid(row=2, column=0)
    #
    #     #question
    #
    #     songs = test.GetPackSongsData(self.quizId)
    #
    #     for songData in songs:
    #
    #         self.line = test.GetSongLyrics(songData[0]).split("\n")[songData[1]]
    #         tk.Label(self, text=f"{self.line}").grid(row=3, column=0)
    #
    #     #answer
    #     # self.blank = self.line.split(" ")[songData[2]]
    #     # tk.Label(self, text=f"{self.blank}").grid(row=4, column=0)
    #     #
    #     # #answer Entry
    #     # self.answerEntry = tk.Entry(self)
    #     # self.answerEntry.grid(row=5, column=0, columnspan=2)

    def Setuplayout(self):
        self.configure(bg="black")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        X = 1
        for packId in test.GetAllPacks():
            tk.Button(self, text=" - ".join(test.GetPackMetadata(packId)),
                      command=lambda packID=packId: quizFrame(self.master, self, packID), font=["Myriad Pro", 20],
                      width=23, bg='#9d31f5', fg='black').grid(row=X, column=0, padx=(10, 10), pady=10)
            # tk.Button(self, text=" - ".join(test.GetPackMetadata(packId))).grid(row=X, column=0)
            X = X + 1


class quizFrame(tk.Frame):
    def __init__(self, windowRef: tk.Tk, oldFrame: tk.Frame = None, packId: int = None):
        self.songMetaNo = None
        self.songdata = None
        if oldFrame is not None:
            oldFrame.destroy()

        super().__init__(windowRef)
        self.packID = packId
        self.quizID = 0
        self.correctAnswerNo = 0
        self.SetupLayout()
        # self.grid(row=0, column=0, padx=10, pady=10)
        self.pack(fill="both", expand=True)

    def SetupLayout(self):
        self.configure(bg="black")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # for data in test.GetPackMetadata(packId):
        #     print(data, end="".join(" - "))

        # Name of the quiz
        tk.Label(self, text=f"{' - '.join(test.GetPackMetadata(self.packID))}", font=["Century Gothic", 12],
                 width=20).grid(row=0, column=0)


        try:
            tk.Label(self, text=f"Question {self.quizID + 1}", font=["Century Gothic", 12]).grid(row=1, column=0)
            tk.Button(self, text="Next Question", command=lambda: self.nextButton(), font=["Century Gothic", 10],
                      bg='#9d31f5').grid(row=8, column=0)
            # Question meta number
            self.songMetaNo = test.GetPackSongsData(self.packID)[self.quizID]
            # Title
            tk.Label(self,
                     text=f"{" - ".join([str(i) if type(i) != list else ", ".join(i) for i in test.GetSongMetadata(self.songMetaNo[0])])}",
                     font=["Century Gothic", 9], fg='#45027a').grid(
                row=2, column=0)

            # Song lines
            line = test.GetSongLyrics(self.songMetaNo[0]).split("\n")[self.songMetaNo[1]]
            tk.Label(self, text=line, font=["Century Gothic", 9]).grid(row=4, column=0)

            # the Blank
            self.blank = line.split(" ")[self.songMetaNo[2]]
            print(self.blank)
            tk.Label(self, text=line.replace(self.blank, "____")).grid(row=5, column=0)

            # Answer entry
            self.answer = tk.Entry(self, font=["Century Gothic", 10])
            self.answer.grid(row=6, column=0, columnspan=2)

        except IndexError:
            endScreen(self.master, self, self.correctAnswerNo, self.quizID)

    def nextButton(self):
        self.quizID = self.quizID + 1  # Increment the quiz ID or question index
        self.songdata = 1
        answer: str = self.answer.get()

        print(f"Your answer is {answer}")
        if answer.strip() == self.blank:
            print("Correct")
            self.correctAnswerNo += 1
            print(self.correctAnswerNo)

        for widget in self.winfo_children():
            widget.destroy()

        self.SetupLayout()

class endScreen(tk.Frame):
    def __init__(self, windowRef: tk.Tk, oldFrame: tk.Frame = None, correctAnswers: int = 0, quizNo: int = 0):
        self.correctAnswerNo = correctAnswers
        self.quizID = quizNo
        if oldFrame is not None:
            oldFrame.destroy()

        super().__init__(windowRef)
        self.setupLayout()
        # self.grid(row=0, column=0, padx=10, pady=10)
        self.pack(fill="both", expand=True)

    def setupLayout(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.configure(bg="#001421")

        tk.Label(self, text="You got", font=["Century Gothic", 15]).grid(row=0, column=0, padx=(10, 10), pady=0)
        tk.Label(self, text=f"{self.correctAnswerNo} out of {self.quizID} correct", font=["Century Gothic", 15],
                 fg='#9d31f5').grid(row=1, column=0, padx=(10, 10), pady=0)

        tk.Button(self, text="Try Again", command=lambda: EntryFrame(self.master, self), font=["Century Gothic", 10],
                  bg='#9d31f5').grid(row=2, column=0)
        tk.Button(self, text="Exit", command=lambda: sys.exit(), font=["Century Gothic", 10],
                  bg='#9d31f5').grid(row=3, column=0)

class mainProgram(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Question Frame")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.configure(bg="#ff8000")
        EntryFrame(self)
        self.mainloop()

if __name__ == "__main__":
    mainProgram().mainloop()

# Go through each song in the current pack
# for packId in test.GetAllPacks():


# Gets a selected Quiz
# packID = 1  #The Id of the quiz you need
# print(test.GetPackSongsData(packID))

# print(" - ".join(test.GetPackMetadata(packID)))  #The Title of the quiz
# for songData in test.GetPackSongsData(packID):
#     # Print the song's details like song name, album name, and artist(s)
#     # If there are multiple artists, show them separated by commas
#     artistName = " - ".join([str(i) if type(i) != list else ", ".join(i) for i in test.GetSongMetadata(songData[0])])
#
#     # Get the lyrics for this song, split them into lines, and pick the correct line
#     line = test.GetSongLyrics(songData[0]).split("\n")[songData[1]]
#
#     # Find the word to replace based on the lyric word number
#     blank = line.split(" ")[songData[2]]
#
#     # Replace the word with "____" (a blank) and print the modified line
#     print(line.replace(blank, "____"))
#     # Also print the blank (answer)
#     print("(" + blank + ")")
#
#     print()
#
#     print()
#
# print()

