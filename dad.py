from pyfiglet import figlet_format
from colorama import init
from termcolor import colored
from requests import get
from random import choice

init()

header = figlet_format("Dad Joke 3000")
header = colored(header, 'cyan')
print(header)


def dad_joke_gen(subject):
    url = "https://icanhazdadjoke.com/search"
    res = get(
        url,
        headers={"Accept": "application/json"},
        params={"term": subject}
    ).json()
    data = res['results']
    num_jokes = res['total_jokes']
    if num_jokes > 1:
        rand_joke = choice(data)
        return f"I've got {num_jokes} jokes about {subject}. Here's one:\n {rand_joke['joke']}"
    elif res['total_jokes'] == 1:
        return f"I've got one joke about {subject}. Here it is:\n {data[0]['joke']}"
    return f"Sorry, I don't have any jokes about {subject}! Please try again."


subject = input("Let me tell you a joke! Give me a topic: ")
print(dad_joke_gen(subject))
