from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # display a button for each answer
        self.answer1_button = Button(text="Some answer text", highlightthickness=0, command=self.press1)
        self.answer1_button.grid(row=2, column=0)

        self.answer2_button = Button(text="Some answer text", highlightthickness=0, command=self.press2)
        self.answer2_button.grid(row=2, column=1)

        self.answer3_button = Button(text="Some answer text", highlightthickness=0, command=self.press3)
        self.answer3_button.grid(row=3, column=0)

        self.answer4_button = Button(text="Some answer text", highlightthickness=0, command=self.press4)
        self.answer4_button.grid(row=3, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text, answers = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.answer1_button.config(text=answers[0])
            self.answer2_button.config(text=answers[1])
            self.answer3_button.config(text=answers[2])
            self.answer4_button.config(text=answers[3])
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.answer1_button.config(state="disabled")
            self.answer2_button.config(state="disabled")
            self.answer3_button.config(state="disabled")
            self.answer4_button.config(state="disabled")

    def press1(self):
        is_right = self.quiz.check_answer(self.answer1_button.cget("text"))
        self.give_feedback(is_right)

    def press2(self):
        is_right = self.quiz.check_answer(self.answer2_button.cget("text"))
        self.give_feedback(is_right)

    def press3(self):
        is_right = self.quiz.check_answer(self.answer3_button.cget("text"))
        self.give_feedback(is_right)

    def press4(self):
        is_right = self.quiz.check_answer(self.answer4_button.cget("text"))
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)
