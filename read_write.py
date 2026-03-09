"""
A script to demonstrate reading and writing
different file types in Python.
"""
# imports
import json
import os

# empty list to store file lines
text_contents = []

# open the file. f is a variable that stores the
# connection to the file while it is open
with open('data/example.txt', 'r') as f:
    text_contents = f.readlines()

# after the with statement, the file is closed 
# and the connection (f) is deleted.
print(text_contents)

# The \n character in the output is a special character
# for a newline

# load the json file
with open('data/q1.json', 'r') as f:
    question = json.load(f)

# print it
print(question)

# this is stored as a dictionary
# they are stored as "key": value
# access values by key
print(f'Question ID: {question['question_id']}')
print(f'Question Text: {question['question_text']}')
print(f'Question answers: {question['answers']}')

# list files with the 'os' library
files = os.listdir('data')
print(f"files in the data folder: {files}")

# write to a new file
# make sure you have a folder called 'output'
with open('output/answers.csv', 'w') as f:
    f.write('question_id,question_text,correct_answer')

for file in files:
    print(f"file: {file}")
    
    # only load json files
    if file.endswith('.json'):
        print(f'found json file: {file}')

        # load the json file
        # need to add the folder name because it only has the file name
        with open('data/' + file, 'r') as f:
            question = json.load(f)

        # get the question id, text

        # use a for loop to get the correct answer

        # append the question id, text, and correct answer to the csv file
        # use 'a' -> with open('output/answers.csv', 'a') as f:
        # f.write(f"{question_id},{question_text},{correct_answer}\n")