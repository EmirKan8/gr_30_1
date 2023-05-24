glasnie = 'ауоыиэяюёеaeiouАУОЫИЭЯЁЕAEIOU'
coglasnie='qwrtpsdfghjklzxcvbnmбвгджзйклмнпрстфхцчшщ'
while True:
    glasnie2 = 0
    coglasnie2 = 0
    button = input("Введите слово:Если хотите завершить программу напишите exit:").lower()
    if button == "exit" or button == "выход":
        print("Программа завершилось")
        break
    letters = len(button)
    for i in button:
        if i in glasnie:
            glasnie2 += 1
        elif i in coglasnie:
            coglasnie2 += 1
    print(f"Слово: {button}")
    print(f"Количество букв: {letters}")
    print(f"Согласные буквы: {coglasnie2}")
    print(f"Гласные буквы: {glasnie2}")
    print(f'Гласные/Согласные: {round(glasnie2 / len(button) * 100, 2)}%'f': {round(coglasnie2 / len(button) * 100, 2)}%')



