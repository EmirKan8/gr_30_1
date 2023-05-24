questions = {
    "Какое животное является символом Австралии? ": "Кенгуру",
    "Какой год был високосным между 2000 и 2010? ": "2004",
    "Какой океан находится между Африкой и Австралией? ": "Индийский",
    "Что такое столица Италии? ": "Рим",
    "Какой город является столицей Франции? ": "Париж"
}

def run_quiz(questions):
    score = 0
    for question, answer in questions.items():
        guess = input(question).lower()
        if guess == answer.lower():
            print("Правильно!")
            score += 1
        else:
            print("Неправильно!")
    print("Вы набрали {}/{} очков.".format(score, len(questions)))

run_quiz(questions)
