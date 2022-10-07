language = input('Выберите язык для шифровки:\nrus - русский\neng - английский\n')
sdvig = int(input('Введите число, на которое сдвинется символ '))
direction = int(input(
    'Вы хотите дешифровать или шифровать код?\n1 - Дешифровать\n2 - Шифровать\nВведите цифру!\n'))
ciphercaesar = input('Введите шифр Цезаря на выбранном языке ')
ciphercaesar = ciphercaesar.upper()
alphabeteng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabetrus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
script = ''
if language == 'eng':
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
    print('Ваш шифр:', script)
elif language == 'rus':
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
    print('Ваш шифр:', script)
