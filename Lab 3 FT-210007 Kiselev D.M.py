language = input('Выберите язык для шифровки:\nrus - русский\neng - английский\n')
a = ['eng', 'rus'] #Список языков
s = 0
while language not in a: #Проверка, какой яззык ввели | Диалоговый режим с пользователем и обработкой ошибок ввода
    print('Вы ввели неверное значение!\n')
    language = input('Выберите язык для шифровки:\nrus - русский\neng - английский\n')

k = 0
while k != 1: #Проверка, чтобы ввели число, на которе сдвинется символ | Диалоговый режим с пользователем и обработкой ошибок ввода
    try:
        sdvig = int(input('Введите число, на которое сдвинется символ '))
    except ValueError:
        print('Вы ввели не число!\nПробуйте снова\n')
    else:
        k += 1
        sdvig = sdvig
d = 0
while d != 1: #Проверка, чтобы ввели число Шифровка/Дешифровка | Диалоговый режим с пользователем и обработкой ошибок ввода
    try:
        direction = int(
            input('Вы хотите дешифровать или шифровать код?\n1 - Дешифровать\n2 - Шифровать\nВведите цифру!\n'))
    except ValueError:
        print('Вы ввели не число!\nПробуйте снова\n')
    else:
        d += 1
        direction = direction
ciphercaesar = input('Введите шифр Цезаря на выбранном языке ')
alphabeteng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabetrus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ciphercaesar = ciphercaesar.upper()
script = ''
if language == 'eng': #Шифровка англ языка
    for line in ciphercaesar:
        if direction == 2:
            num = alphabeteng.find(line)
            num2 = num + sdvig
            if line in alphabeteng:
                script = script + alphabeteng[num2]
            else:
                script = script + line
        elif direction == 1:
            num = alphabeteng.find(line)
            num2 = num - sdvig
            if line in alphabeteng:
                script = script + alphabeteng[num2]
            else:
                script = script + line
    if script == ciphercaesar: #Проверка, если ввели шифр не на том языке | Диалоговый режим с пользователем и обработкой ошибок ввода
        print('Вы ввели что то неверно!\nВводите шифр Цезаря на английском языке')
    else:
        print('Ваш шифр:', script)
elif language == 'rus': #Шифровка рус языка
    for line in ciphercaesar:
        if direction == 2:
            num = alphabetrus.find(line)
            num2 = num + sdvig
            if line in alphabetrus:
                script = script + alphabetrus[num2]
            else:
                script = script + line
        elif direction == 1:
            num = alphabetrus.find(line)
            num2 = num - sdvig
            if line in alphabetrus:
                script = script + alphabetrus[num2]
            else:
                script = script + line
    if script == ciphercaesar: #Проверка, если ввели шифр не на том языке | Диалоговый режим с пользователем и обработкой ошибок ввода
        print('Вы ввели что то неверно!\nВводите шифр Цезаря на русском языке')
    else:
        print('Ваш шифр:', script)

