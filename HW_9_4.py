import os
import random
from pprint import pprint
from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

l1 = map(lambda x, y: x == y, first, second)
print(list(l1))
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, "a", encoding="utf-8")
        for i in data_set:
            file.write(str(i) + '\n')
        file.close()

    return write_everything
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
class MysticBall:
    def __init__(self, *words):
        self.words = words
    def __call__(self):
        elem = random.choice(self.words)
        return elem

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())