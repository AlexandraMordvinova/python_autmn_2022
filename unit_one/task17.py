#todo: Создайте функцию compute_bill, считающаю итоговую сумму товаров в чеке.
#Функция должна принимать 1 параметр - словарь, в котором указано количество едениц товара.
#Цены хранятся в словаре:
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}
shopping_list = ['banana', 'apple', 'orange', 'pear']
import csv
with open('prices.csv', 'r+', encoding='utf-8') as p:
  reader = csv.reader(p, delimiter=',')
  count = 0
  for row in reader:
    prices[row[0]] = row[1]
input_file = csv.DictReader(open('prices.csv'))

def compute_bill(prices):
  total = 0
  for a in food:
    total += prices[a]
  return total



