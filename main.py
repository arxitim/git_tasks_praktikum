import os
import time

QUESTIONS = [
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

NAMES = [
    'student_1',
    'student_2',
    'student_3',
    'student_4',
    'student_5',
    'student_6',
    'student_7',
    'student_8',
    'student_9',
    'student_10',
    'student_11',
    'student_12',
    'student_13',
    'student_14',
    'student_15',
    'student_16'
]


def add_question(name, question):
    """
    Adds a question to the HTML code

    :param name: string Name of student
    :param question: string Question for the student
    :return: None
    """
    with open('index.html', 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            if '</tr>' in line:
                lines.insert(lines.index(line) + 1,
                             f'\n\t\t<tr>\n\t\t\t<td>{name}</td>\n\t\t\t<td>{question}</td>\n\t\t\t<td></td>\n\t\t</tr>')
                break

    with open('index.html', 'w') as f:
        f.write('\n'.join(lines))


def make_astley():
    """
    Function to replace the main logo with the Rick (imitation of colleagues' mistakes)

    :return: None
    """
    with open('index.html', 'r') as f:
        data = f.read()
        data = data.replace('src="img/logo.png"', 'src="http://giphygifs.s3.amazonaws.com/media/6b9QApjUesyOs/giphy.gif"')

    with open('index.html', 'w') as f:
        f.write(data)


def main():
    for i, question in enumerate(QUESTIONS):
        os.system('git pull')
        time.sleep(5)
        if i == 4:          # "random", yeah
            make_astley()
        add_question(NAMES[i], question)
        os.system(f'git commit -am "MOD: question {i}"')
        time.sleep(5)
        os.system('git push')
        time.sleep(120)


if __name__ == '__main__':
    main()
