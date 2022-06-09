# Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо. 
# Используйте знания с последней лекции. Выполните ее в виде функции. 

'''with open('file_first.txt', 'r+', encoding="utf-8") as ff: 
    line = ff.readline().split() 
    list = [i for i in line if 'абв' not in i.lower()] 
    print(list)'''

# Вы когда-нибудь играли в игру "Крестики-нолики"? 
# Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку. 
'''def user_cord(): 
    cord = list(map(int, input().split())) 
    return cord 

def bot_cord(us, tb): 
    if us == [0, 0]: 
        if tb[1][0] == '*': 
            tb[1][0] = '0' 
        elif tb[2][0] == '*': 
            tb[2][0] = '0' 
    elif us == [0, 1]: 
        if tb[1][0] == '*': 
            tb[0][0] = '0' 
        elif tb[0][2] == '*': 
            tb[0][2] = '0' 
        elif tb[1][1] == '*': 
            tb[1][1] = '0' 
        elif tb[2][1] == '*': 
            tb[2][1] = '0' 
    elif us == [0, 2]: 
        if tb[0][1] == '*': 
            tb[0][1] = '0' 
        elif tb[0][0] == '*': 
            tb[0][0] = '0' 
        elif tb[1][1] == '*': 
            tb[1][1] = '0' 
        elif tb[2][0] == '*':  
            tb[2][0] = '0' 
        elif tb[10][2] == '*': 
            tb[1][2] = '0' 
        elif tb[2][2] == '*': 
            tb[2][2] = '0' 
    elif us == [1, 0]: 
        if tb[0][0] == '*': 
            tb[0][0] = '0' 
        elif tb[1][1] == '*': 
            tb[1][1] = '0' 
        elif tb[1][2] == '*': 
            tb[1][2] = '0' 
        elif tb[2][0] == '*':  
            tb[2][0] = '0' 
    elif us == [1, 1]: 
        if tb[0][1] == '*': 
            tb[0][1] = '0' 
        elif tb[2][1] == '*': 
            tb[2][1] = '0' 
        elif tb[1][0] == '*': 
            tb[1][0] = '0' 
        elif tb[1][2] == '*':  
            tb[1][2] = '0' 
        elif tb[0][0] == '*': 
            tb[0][0] = '0' 
        elif tb[2][2] == '*': 
            tb[2][2] = '0' 
        elif tb[0][2] == '*': 
            tb[0][2] = '0' 
        elif tb[2][0] == '*': 
            tb[2][0] = '0' 
    elif us == [1, 2]: 
        if tb[0][2] == '*': 
            tb[0][2] = '0' 
        elif tb[1][1] == '*': 
            tb[1][1] = '0' 
        elif tb[2][2] == '*': 
            tb[2][2] = '0' 
    elif us == [2, 0]: 
        if tb[1][0] == '*': 
            tb[0][1] = '0' 
        elif tb[0][0] == '*': 
            tb[0][0] = '0' 
        elif tb[2][1] == '*': 
            tb[2][1] = '0' 
        elif tb[2][2] == '*':  
            tb[2][2] = '0' 
        elif tb[1][1] == '*': 
            tb[1][1] = '0' 
        elif tb[0][2] == '*': 
            tb[0][2] = '0' 
    elif us == [2, 1]: 
        if tb[1][1] == '*': 
            tb[1][1] = '0' 
        elif tb[0][1] == '*': 
            tb[0][1] = '0' 
        elif tb[2][0] == '*': 
            tb[2][0] = '0' 
        elif tb[2][2] == '*':  
            tb[2][2] = '0' 
    elif us == [2, 2]: 
        if tb[1][2] == '*': 
            tb[1][2] = '0' 
        elif tb[0][2] == '*': 
            tb[0][2] = '0' 
        elif tb[1][2] == '*': 
            tb[1][2] = '0' 
        elif tb[0][2] == '*':  
            tb[0][2] = '0' 
        elif tb[1][1] == '*': 
            tb[1][1] = '0' 
        elif tb[0][0] == '*': 
            tb[0][0] = '0' 
 
def game(tab, uc, bc): 
    a = True 
    while a: 
        if '*' in tab: 
            a = False 
        elif (tab[0][0] == 'x' and tab[0][1] == 'x' and tab[0][2] == 'x') or (tab[0][0] == '0' and tab[0][1] == '0' and tab[0][2] == '0'): 
            a = False  
        elif (tab[1][0] == 'x' and tab[1][1] == 'x' and tab[1][2] == 'x') or (tab[1][0] == '0' and tab[1][1] == '0' and tab[1][2] == '0'): 
            a = False  
        elif (tab[2][0] == 'x' and tab[2][1] == 'x' and tab[2][2] == 'x') or (tab[2][0] == '0' and tab[2][1] == '0' and tab[2][2] == '0'): 
            a = False  
        elif (tab[0][0] == 'x' and tab[1][1] == 'x' and tab[2][2] == 'x') or (tab[0][0] == '0' and tab[1][1] == '0' and tab[2][2] == '0'): 
            a = False  
        elif (tab[2][0] == 'x' and tab[1][1] == 'x' and tab[0][2] == 'x') or (tab[2][0] == '0' and tab[1][1] == '0' and tab[0][2] == '0'): 
            a = False  
        else: 
            user = uc() 
            tab[user[0]][user[1]] = 'x' 
            bc(user, tab) 
            for i in table: 
                print(i) 
            print('-------------------------') 
 
table = [ 
    ['*', '*', '*'], 
    ['*', '*', '*'], 
    ['*', '*', '*'] 
] 
 
game(table,user_cord, bot_cord)'''


# Отфильтруйте его, чтобы этот текст можно было нормально прочесть.  
# Предусмотрите вариант, что мусорные слова могли быть написаны без использования запятых. 
 
'''def sort(tx): 
    i = 0 
    while i < len(tx): 
        if 'общем' in tx[i].lower(): 
            del tx[i] 
            del tx[i-1] 
            i -= 2 
        elif ('короче' in tx[i].lower()) or ('ну' in tx[i].lower()) or ('ээ' in tx[i].lower()) or ('кажется' in tx[i].lower()) or ('ясен' in tx[i].lower()) or ('пень' in tx[i].lower()) or ('говоря' in tx[i].lower()): 
            del tx[i] 
            i -= 1 
        i += 1 
 
with open('file_three.txt', 'r+', encoding='utf-8') as ft: 
    text = list(ft.readline().split())  
    sort(text)    
 
with open('file_three.txt', 'w+', encoding='utf-8') as ft: 
    for i in text:  
            ft.write(i + ' ')''' 
 
#Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого плюс 1.  
# Вам нужно сделать две функции:  
# первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.  
# Вторая — которая отфильтрует этот список следующим образом:  
# если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается,  
# его номер заменяется на сумму очков.  
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. 
 
'''from functools import reduce 
 
 
def spisok(lp, n): 
    for i in range(len(lp)): 
        lp[i]= lp[i].upper() 
    sps = list(zip(n, lp)) 
    return sps 
 
def sort(sps, lp, n): 
    spisok_l = sps(lp, n) 
    arr_l = [] 
    arr_n = [] 
    for i in range(len(spisok_l)): 
        count = 0 
        for j in spisok_l[i][1]: 
            count += ord(j) 
        if count % spisok_l[i][0] == 0: 
            arr_l.append(spisok_l[i][1]) 
            arr_n.append(count) 
            arr = list(zip(arr_n, arr_l)) 
    print(reduce(lambda x,y: x+y, arr_n)) 
 
 
language_programm = ['C++', 'C#', 'Kotlin', 'Java', 'PHP', 'Python'] 
nums = [1, 2, 3, 4, 5, 6] 
 
sort(spisok, language_programm, nums)'''