"""
Attributes and functions of an exam.
"""

# imports
import random

# define the class

class Exam:
    """
    This class contains the elements of an exam
    and functions to modify an exam.
    """

    def __init__(self, exam_number: int, exam_version: int, questions=[]):
        """
        Instantiate an exam

        Parameters
        ----------
        exam_number : int
            The number of the exam
        exam_version : int
            Exam version number
        questions : list, optional
            Questions to include on the exam.
        """

        self.exam_number = exam_number
        self.exam_version = exam_version
        self.questions = questions
        self.cover_page = ""
        self.answers = []
        self.total_points = 0
        

    def add_question(self, question_text: str):
        """
        Add a question to an existing exam

        Parameters
        ----------
        question_text : str
            The question to add
        """

        # use the self keyword to update an instance
        # otherwise it may accidentally upate every exam!

        self.questions.append(question_text)

    def randomize_questions(self):
        """
        Randomize the question list. This will
        overwrite the original question list.
        """

        # take the list of questions, randomize, 
        # and overwrite the original list
        random.shuffle(self.questions)



# this only runs if the file is called directly from the terminal
# it will not run when imported by another script
if __name__ == '__main__':
    print('Exam Class Example')

    # list of questions
    question_list = ['Who do you think you are?',
                     'What is a question?',
                     'What is a class?']

    # create an instance of an exam
    exam_v1 = Exam(1, 1, questions=question_list)
    print(f'Exam V1 Version: {exam_v1.exam_version}')
    print(f'Exam V1 Questions: {exam_v1.questions}')

    # print after randomizing
    exam_v1.randomize_questions()
    print(f'Exam V1 questions (randomized): {exam_v1.questions}')
    
    # create another instance of an exam
    exam_v2 = Exam(exam_number=1, exam_version=2)
    print(f'Exam V2 Version: {exam_v2.exam_version}')
    print(f'Exam V2 Questions: {exam_v2.questions}')