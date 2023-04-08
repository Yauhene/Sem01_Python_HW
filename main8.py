# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

#plateW = 3 
plateL = 2

# функция ввода значений ================================
def sInput(s):
    flag1 = True
    
    while flag1:
        value = input(s)
        
        if len(value) == 0 or int(value) == 0:
            print('Несерьезно как-то, еще раз...')
            print()
        elif (len(value) != 0) and (value[0] != '-'): 
            return int(value)
            flag1 = False
            
            
# тело программы ===========================================

flag = True
print()
print()
plateW = sInput('Введите ширину плитки в дольках: ')
plateL = sInput('Введите длину плитки в дольках: ')
print()

while flag:
    
    neededPart = sInput('Сколько долек отламываем? Введите число: ')
    print()

    # проверка на "пустой" ввод или превышение количества долек в плитке
    if neededPart == 0: 
        print('Без ложной скромности, пожалуйста...')
    elif plateL * plateW < int(neededPart): 
        print(f'Тут вся плитка - {plateL * plateW} долек, перебор...')
    else:
        neededPart = int(neededPart)
        
        if neededPart % plateW == 0 or neededPart % plateL == 0:
            print("Вполне реальная задача,")
            print(" Yes")
        else:
            print("Увы, это невозможно...")
            print("...No")
        flag = False
        print()