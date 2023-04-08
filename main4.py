# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
#Сколько журавликов сделал каждый ребенок, если известно, 
#что Петя и Сережа сделали одинаковое количество журавликов, 
#а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10
print()
print('=============================================')

def outStr(s):
    if s < 5: return "журавлика"
    else: return "журавликов"

flag = True
while flag:
    number = input('Введите количество сделанных журавликов: ')
    if number == '': 
        number = 0
        print("Вы ничего не ввели...")
    else: number = int(number)
    
    if number % 6 != 0 or number < 6: 
        print()
        print('Данная задача не решается целочисленным способом...')
        print('...но есть шанс все исправить')
        print()
    else:
        numKatja = number // 3 * 2
        numPetja = numKatja // 4
        numSrezha = numPetja
        flag = False

print()
print(f'Катя сделала {numKatja} {outStr(numKatja)}')
print(f'Петя сделал {numPetja} {outStr(numPetja)}')
print(f'Сергежа сделал {numSrezha} {outStr(numPetja)}')

print('=============================================')
print()