# Написать игру "Поле чудес"
import random

#Отгадываемые слова и описание лежат в разных  массивах по одинаковому индексу.
#words = ["оператор", "конструкция", "объект"]
#desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования", "..", ".." ]
#Пользователю выводится определение слова и количество букв в виде шаблона. Стиль шаблона может быть любым.
#Слово из массива берется случайным порядком. Принимая из ввода букву мы ее открываем
#в случае успеха а в случае неуспеха насчитывам штрафные балы. Игра продолжается до 10 штрафных баллов
#либо победы.
#Пример вывода:
#"Это слово обозначает наименьшую автономную часть языка программирования"
#▒  ▒  ▒  ▒  ▒  ▒  ▒  ▒
#Введите букву: O
#O  ▒  ▒  ▒  ▒  ▒  O  ▒
#Введите букву: Я
#Нет такой буквы.
#У вас осталось 9 попыток !
#Введите букву:

print("Добро пожаловать в игру Поле чудес.\n\
Игра продолжается до 10 штрафных баллов, либо до победы")
print("Внимание!\n")
a = open('questions.txt', 'w')
a.write('questions')
a.close()

import pathlib
from pathlib import Path

path = Path('Desktop', 'python_autumn_2022', 'unit_one', 'task15.py', 'questions.txt')
def join(current_view):
    pass
while True:
    question = input('Введите вопрос или q')
    if question == 'q':
        break
    else:
        answer = input('Введите ответ')
        with open ('questions.txt', 'a', encoding = 'utf-8') as f:
            f.write ('question+; answer+\n')
def get_question():
    global answer
    with open ('questions.txt', 'r', encoding = 'utf-8') as f:
        question_list = f.read().splitlines()
    number_question = random.randrange(0,len(question_list))
    question_answer = str (question_list[number_question])
    for i in range(0, len(question_answer)):
        if question_answer[i]==';':
            question = question_answer[0:i]
            answer = question_answer[i+1:len(question_answer)]
    return (answer, question)
answer, question = get_question()
print (question)
print (answer)
current_view = []
for i in range (0, len(answer)):
    current_view.append('▒')
print('', join(current_view))

while True:
    user = input('Введите букву или назовите слово')
    if user == answer:
        print('Вы правильно назвали слово!');break
    if (user in answer):
        print('Есть такая буква!')
        for i in range (0, len(answer)):
            if answer[i] == user:
                current_view[i] = user
                user_answer=''.join(current_view)
    else:
        print('Такой буквы нет!')
    if current_view == list(answer):
        print('вы правильно назвали все буквы!'); break
    print(user_answer)