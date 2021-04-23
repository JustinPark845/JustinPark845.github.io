from turtle import Turtle
import time
ALIGN = "center"
FONT = ("Courier", 24, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.retrieve_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def retrieve_high_score(self):
        with open("/Users/justinpark/Desktop/Code/Angela_Yu_Coding_Class/snake game/highscores.txt", mode="r") as file:
            contents = file.read()
            self.high_score = contents
            print(contents)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("/Users/justinpark/Desktop/Code/Angela_Yu_Coding_Class/snake game/highscores.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAMEOVER", align=ALIGN, font=("Courier", 64, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def restart(self):
        time.sleep(1.5)
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score} HighScore: {self.high_score}", align=ALIGN, font=FONT)
        self.goto(0,0)
        self.write("Thank you for playing!", align=ALIGN, font=("Courier", 32, "normal"))

    def highscore_list(self):
        with open("/Users/justinpark/Desktop/Code/Angela_Yu_Coding_Class/snake game/saved_highscores.txt", mode="r") as file:
            self.clear()
            self.goto(0,0)
            self.write(f"{file}", align=ALIGN, font=("Courier", 64, "normal"))
        self.write("Would you like to add yourself to the high score list?", align=ALIGN, font=("Courier", 64, "normal"))
        add_score = input("Would you like to add yourself to the high score list?").lower()
        if add_score == "yes" or "ye" or "y":
            pass