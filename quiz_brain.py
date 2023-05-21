import html

class QuizBrain:

    def __init__(self, q_list):
        print(q_list)
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def return_question_list(self):
        pass

    def still_has_questions(self) -> bool:
        """returns True if less questions have been displayed than the total questions
        in the question list, else False"""
        print(f"{self.question_number=}, {len(self.question_list)=}")
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = self.current_question.text
        return f"Q.{self.question_number}: {html.unescape(q_text)} (True/False): "
        # user_answer = input()
        # self.check_answer(user_answer)

    def check_answer(self, user_answer: str) -> bool:
        """Returns True if user_answer is the same as the question's answer, else False."""
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
        # Commenting out the print commands so the function is more suited to the GUI
        #     print("You got it right!")
        # else:
        #     print("That's wrong.")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
