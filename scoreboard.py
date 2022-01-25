from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.highscore_update()
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def highscore_update(self):
        with open("data.txt") as data:
            self.highscore = int(data.read())

    def update_scoreboard(self):
        self.clear()
        self.highscore_update()
        self.write(f'Score: {self.score} Highscore: {self.highscore}', False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            with open("data.txt", "w") as data:
                data.write(str(self.score))
        self.score = 0
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
