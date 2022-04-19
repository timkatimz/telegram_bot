import json
from random import sample


def load_data():
    with open("1.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def shuffle_questions():
    data = load_data()
    for question in sample(data, len(data)):
        return question
