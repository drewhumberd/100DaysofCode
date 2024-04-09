import html

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(current_question.text)
        q_answer = current_question.answer
        return q_text, q_answer

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
            return True
        else:
            print("You got it wrong.")
            return False
        # print(f"The correct answer was {correct_answer}.")
        # print(f"Your current score is {self.score}/{self.question_number}.")
        # print("\n")