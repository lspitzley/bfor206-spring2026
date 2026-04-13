"""
Tests for the exam class
"""

import pytest
import random

# import the exam.py class file
import exam


# test the question order randomizaiton

def test_randomize_questions():
    """
    Test the randomized question orders using a fixed seed
    """
    
    question_list = ['Who do you think you are?',
                    'What is a question?',
                    'What is a class?']
    
    # create two exam versions
    v1 = exam.Exam(1, 1, questions=question_list)
    v2 = exam.Exam(1, 2, questions=question_list)

    # set seed to a fixed value
    # seed 0 gives a different list than the original for both versions
    # and both v1 and v2 are different
    random.seed(0)

    v1.randomize_questions()
    print(f'Exam V1 questions (randomized): {v1.questions}')

    v2.randomize_questions()
    print(f'Exam V2 questions (randomized): {v2.questions}')

    print(f'Original question list: {question_list}')

    # with seed = 0, all question lists are different
    # other seeds may not do this
    assert question_list != v1.questions != v2.questions
