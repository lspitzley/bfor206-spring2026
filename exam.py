"""
Attributes and functions of an exam.
"""

# imports

# define the class

class Exam:
    """
    This class contains the elements of an exam
    and functions to modify an exam.
    """

    def __init__(self, exam_number, exam_version):
        """
        initiate an instance of an exam
        """

        self.cover_page = ""
        self.questions = []
        self.answers = []
        self.total_points = 0
        self.exam_number = exam_number
        self.exam_version = exam_version

    def add_question(self, question_text: str):
        """
        Add a question to an existing exam
        """

        # use the self keyword to update an instance
        # otherwise it may accidentally upate every exam!

        self.questions.append(question_text)

# this only runs if the file is called directly from the terminal
# it will not run when imported by another script
if __name__ == '__main__':
    print('Exam Class Example')

    # create an instance of an exam
    exam_v1 = Exam(1, 1)
    print(f'Exam V1 Version: {exam_v1.exam_version}')
    print(f'Exam V1 Questions: {exam_v1.questions}')

    # add a question to V1
    exam_v1.add_question('Who do you think you are?')
    exam_v1.add_question('What is a question?')
    print(f'Exam V1 Questions: {exam_v1.questions}')
    
    # create another instance of an exam
    exam_v2 = Exam(exam_number=1, exam_version=2)
    print(f'Exam V2 Version: {exam_v2.exam_version}')
    print(f'Exam V2 Questions: {exam_v2.questions}')