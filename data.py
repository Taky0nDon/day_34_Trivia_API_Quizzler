import requests
import json
from question_model import Question
import html

URL = "https://opentdb.com/api.php"
TOKEN_URL = "https://opentdb.com/api_token.php"

token = requests.get(TOKEN_URL)
token.raise_for_status()

parameters = {
    "type": "boolean",
    "amount": "10",
    # "token": token,
    "category": 9
}


def get_category_id(category_string):
    with open("categories.json") as category_data:
        categories = json.load(category_data)["trivia_categories"]
    for item in categories:
        if category_string == item["name"]:
            return item["id"]
def give_questions_to_user(category_id: int | None) -> list[Question] :
    parameters["category"] = category_id
    question_bank = []
    for question in get_questions_from_API(parameters=parameters):
        question_text = html.unescape(question["question"])
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
    return question_bank
def get_questions_from_API(parameters=None):
    response = requests.get("https://opentdb.com/api.php?amount=10", parameters)
    response.raise_for_status()
    data = response.json()
    print(f"{data=}")
    question_data = data["results"]
    return question_data
def get_cat_strings():
    with open("categories.txt", "r") as category_file:
        list_of_categories = category_file.readlines()
    i = 0
    for item in list_of_categories:
        item = item.strip("\n")
        list_of_categories[i] = item
        i += 1
    return list_of_categories
# question_data = json_data["results"]

# question_data = [
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The HTML5 standard was published in 2014.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The first computer bug was formed by faulty wires.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "FLAC stands for 'Free Lossless Audio Condenser'.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Linus Torvalds created Linux and Git.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "The programming language 'Python' is based off a modified version of 'JavaScript'",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "AMD created the first consumer 64-bit processor.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "'HTML' stands for Hypertext Markup Language.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "In most programming languages, the operator ++ is equivalent to the statement '+= 1'.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "hard",
#         "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     }
# ]
