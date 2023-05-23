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


def give_questions_to_user(category_id: int | None) -> list[Question]:
    """
    Takes an optional integer argument as the category ID and  returns a bank of questions based on the data
    returned from get_questions_from_API()
    """
    parameters["category"] = category_id
    question_bank = []
    for question in get_questions_from_API(params=parameters):
        question_text = html.unescape(question["question"])
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
    return question_bank


def get_questions_from_API(params=None):
    """returns a dictionary with all the data for the questions from calling the API with the parameters
    outlined in the parameters variable"""
    response = requests.get("https://opentdb.com/api.php?amount=10", params)
    response.raise_for_status()
    data = response.json()
    print(f"{data=}")
    question_data = data["results"]
    return question_data


def get_cat_strings() -> list[str]:
    """Returns a list of strings, each string being the category name to display in the combobox"""
    with open("categories.txt", "r") as category_file:
        list_of_categories = category_file.readlines()
    i = 0
    for item in list_of_categories:
        item = item.strip("\n")
        list_of_categories[i] = item
        i += 1
    return list_of_categories
