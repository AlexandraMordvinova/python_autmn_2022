# todo: Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).
# Примечание: коэффициенты получаем через функцию input().
A = int(input())
B = int(input())
if A==0:
    print(None)
if A > 0:
    x = -B/A
    print(x)
elif A < 0:
    x = -B/A
    print(x)
