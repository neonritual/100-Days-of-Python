#TODO: asking the questions
#TODO: checking of the answer was correct.
#TODO: Checking if we're at the end of the quiz yet.

#created class QuizBrain
#2 attributes: question_number = 0, to keep track of the question the user is currently on.
#questions_list (pass question_bank into it)
#and 1 method: next_question, to pull up next q.

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.user_score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False?)")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("That's right!")
            self.user_score += 1
        else:
            print("Sorry, that's incorrect.")



