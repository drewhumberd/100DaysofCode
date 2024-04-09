import tkinter
from day17.quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quizbrain:QuizBrain):
        self.quiz = quizbrain
        self.window = tkinter.Tk()
        self.window.title("Quizler")
        false_img = tkinter.PhotoImage(file="supportfiles/wrong.png")
        true_img = tkinter.PhotoImage(file="supportfiles/right.png")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score = tkinter.Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR, font=("Arial", 14, "italic"))
        self.score.grid(row=0, column=1, pady=20)
        self.triviablock = tkinter.Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.triviatext = self.triviablock.create_text(
            150,
            125,
            text="Trivia Question",
            fill="black",
            width=280,
            font=("Arial", 20, "italic")
            )
        self.triviablock.grid(row=1, column=0, columnspan=2, pady=20)
        self.truebutton = tkinter.Button(
            image=true_img,
            bg=THEME_COLOR,
            highlightthickness=0,
            bd=0,
            command=self.true_response
            )
        self.truebutton.grid(row=2, column=0, pady=20)
        self.falsebutton = tkinter.Button(
            image=false_img,
            bg=THEME_COLOR,
            highlightthickness=0,
            bd=0,
            command=self.false_response
            )
        self.falsebutton.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.triviablock["bg"] ="white"
        if self.quiz.still_has_questions():
            ques_tuple = self.quiz.next_question()
            q_text = ques_tuple[0]
            self.ques_answer = ques_tuple[1]
            self.triviablock.itemconfig(self.triviatext, text=q_text)
        else:
            self.triviablock.itemconfig(self.triviatext, text="You've reached the end of the quiz.")
            self.truebutton.config(state="disabled")
            self.falsebutton.config(state="disabled")

    def false_response(self):
        if self.quiz.check_answer(user_answer="False", correct_answer=self.ques_answer):
            self.triviablock["bg"] ="green"
        else:
            self.triviablock["bg"] ="red"
        self.score["text"] = f"Score: {self.quiz.score}"
        self.window.after(1000, self.get_next_question)

    def true_response(self):
        if self.quiz.check_answer(user_answer="True", correct_answer=self.ques_answer):
            self.triviablock["bg"] ="green"
        else:
            self.triviablock["bg"] ="red"
        self.score["text"] = f"Score: {self.quiz.score}"
        self.window.after(1000, self.get_next_question)