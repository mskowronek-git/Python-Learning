
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.correct_answer_number = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        one_question = self.questions_list[self.question_number]
        self.question_number += 1
        answer_input = input(f"Q.{self.question_number}: {one_question.text} (True/False)?: ")
        self.check_answer(answer_input, one_question.answer)

    def check_answer(self, answer_input, one_question_answer):
        if one_question_answer.lower() == answer_input.lower():
            print("You got it right!")
            self.correct_answer_number += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {one_question_answer}.")
        print(f"Your current score is: {self.correct_answer_number}/{self.question_number}.")


