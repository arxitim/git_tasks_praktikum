import os
import time

questions = [
    'The Answer to the Ultimate Question of Life, the Universe, and Everything?',
    'What\'s the amount of power required to go back to the future?',
    'What is the name of Iron Man\'s assistant?',
    'Who lives in a pineapple under the sea?',
    'What is the name of the USS Enterprise\'s navigator?',
    'Oh my God! They killed {name}!',
    'Where\'s the money, {name} ? Where\'s the f***ing money, shithead?',
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
        for line in lines:
            if '</tr>' in line:
                lines.insert(lines.index(line) + 1,
                             '\n\t\t<tr>\n\t\t\t<td>{name}</td>\n\t\t\t<td>{question}</td>\n\t\t\t<td></td>\n\t\t</tr>'
                             .format(name=name, question=question))
                break

    with open('index.html', 'w') as f:
        f.write('\n'.join(lines))


def make_astley():
    print("HERE")
    with open('index.html', 'r') as f:
        data = f.read()
        data.replace('src="img/logo.png"', 'src="http://giphygifs.s3.amazonaws.com/media/6b9QApjUesyOs/giphy.gif"')

    with open('index.html', 'w') as f:
        f.write(data)


for i in range(len(questions)):
    os.system('git pull')  # актуализируем репозиторий
    time.sleep(3)
    if i == 4:
        make_astley()
    add_question(names[i], questions[i])
    os.system('git commit -am "MOD: question {number}"'.format(number=i))
    time.sleep(2)
    os.system('git push')
    time.sleep(5) # время до следующего добавления вопроса

