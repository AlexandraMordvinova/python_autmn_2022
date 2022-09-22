#задано целое число от 10 до 99, необходимо найти сумму и произведение его цифр.
x = input(53)
sum = 0
mult = 1
for a in x:
    sum += int(a)
    mult += int(a)

    print(sum)
    print(mult)
