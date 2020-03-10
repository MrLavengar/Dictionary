import json
data = json.load(open("data.json"))
from difflib import get_close_matches

def translate(word):
    def answer(w):
        answer = f"Meanings of word '{w}:'\n"
        w = data[w]
        for i in range(len(w)):
            w[i] = w[i].replace('[', '').replace(']', '')
            answer += f' {i + 1}) {w[i]}\n'
        return answer
    if word in data:
        return answer(word)
    match = get_close_matches(word,data.keys(),cutoff=0.6)
    if len(match)>0:
        possible_word = match[0]
        user_input = input(f"Do you mean '{possible_word}' instead? y/n: ").lower()
        if user_input == 'y':
            return answer(possible_word)
        elif user_input !='n':
            return 'Incorect entry'
    return "Word doesn't exist, please double check it."

print("Welcome in our dictionary! Type 'q' to exit.")
while True:
    word = input("Enter word: ").lower()
    if word == 'q':
        break
    print(translate(word))
