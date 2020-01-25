import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def get_meaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.upper() in data:
        return data[w.upper()]
    elif w.title() in data:
        return data[w.title()]
    elif len(get_close_matches(w, data.keys())) > 0:
        ans = input("Did you mean '%s' ? Enter Y if yes: " % get_close_matches(w, data.keys())[0])
        if ans == "Y" or ans == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif ans == "N" or ans == 'n':
            return "That word doesn't exist."
        else:
            return "We didn't understand your answer"
    else:
        return "That word doesn't exist."

word = input("Enter word: ")
result = get_meaning(word)
if type(result) == list:
    for item in result:
        print(item)
else:
    print(result)