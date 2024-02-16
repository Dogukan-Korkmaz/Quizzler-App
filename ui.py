from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=4, pady=50, padx=20)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=3)

        self.question_text = self.canvas.create_text(
            150,
            125,
            anchor="center",
            width=250,
            text="",
            font=("arial", 18, "italic")
        )

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, relief="flat")
        self.true_button.grid(row=4, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, relief="flat")
        self.false_button.grid(row=4, column=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

