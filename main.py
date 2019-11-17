questions = [
    'The Answer to the Ultimate Question of Life, the Universe, and Everything?',
    'Where\'s the money, {name} ? Where\'s the f***ing money, shithead?',
    'What\'s the amount of power required to go back to the future?',
    'What is the name of Iron Man\'s assistant?',
    'Oh my God! They killed {name}!',
    'Who lives in a pineapple under the sea?',
    'What is the name of the USS Enterprise\'s navigator?',
    'Who said: "Wakka wakka wakka?"',
    'All you had to do, was follow the f***ing {transport}, CJ.',
    'Wake the f**ck up, {warrior}, we have a city to burn.',
    'Heaviest object in the Universe?',
    'What does the fox say?',
    'What did Admiral Akbar say, when he arrived in Thailand?',
    'I used to be an adventurer like you, but then I took an {weapon} in the knee.',
    '{}. {} never changes.',
    'Triss or Yeniffer?',
]


def add_question(name, question):
    with open('index.html', 'r') as f:
        lines = f.read().splitlines()
        for line in reversed(lines):
            if line == '        </tr>':
                lines.insert(lines.index(line) + 1,
                             '\n\t\t<tr>\n\t\t\t<td>{name}</td>\n\t\t\t<td>{question}</td>\n\t\t\t<td></td>\n\t\t</tr>'
                             .format(name=name, question=question))

    with open('index.html', 'w') as f:
        f.write('\n'.join(lines))



