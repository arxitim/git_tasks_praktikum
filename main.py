import os
import time

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

names = [
    'name1',
    'name2',
    'name3',
    'name4',
    'name5',
    'name6',
    'name7',
    'name8',
    'name9',
    'name10',
    'name11',
    'name12',
    'name13',
    'name14',
    'name15',
    'name16'
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


for i in range(len(questions)):
    add_question(names[i], questions[i])
    os.system('git commit -am "MOD: question {number}"'.format(number=i))
    time.sleep(1)
    os.system('git push')
    time.sleep(5)

