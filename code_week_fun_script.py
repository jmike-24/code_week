import random

random.seed(42)

NAMES = ["Анна", "Иван", "Мария", "Фатима", "Олег", "Ли Вэй", "Ахмед", "Елена"]
SURNAMES = ["Иванова", "Петров", "Сидорова", "Аль-Рашид", "Гарсия", "Ли", "Смирнова", "Нуриев"]
FACULTIES = ["МО", "МЭО", "МП", "МЖ", "МИЭП", "ФФЭ", "ФУП", ""]

ORIGINAL = [
    "Мы, народы Объединённых Наций, решив спасти грядущие поколения от бедствия войны, "
    "которая дважды в нашей жизни принесла человечеству невыразимое горе, и вновь утвердить "
    "веру в основные права человека, в достоинство и ценность человеческой личности, "
    "в равноправие мужчин и женщин и в равноправие больших и малых наций.",
    "Все Члены Организации воздерживаются в их международных отношениях от угрозы силой "
    "или её применения как против территориальной неприкосновенности или политической "
    "независимости любого государства, так и каким-либо другим образом, несовместимым "
    "с Целями Объединённых Наций.",
]

EXTRA = ["безусловно", "однако", "таким образом", "кроме того"]

QUESTIONS = [
    {"correct": 0,
     "ru": ("Что такое переменная?", ["Именованная ячейка памяти для значения", "Функция, которая ничего не возвращает", "Тип файла", "Комментарий в коде"]),
     "en": ("What is a variable?", ["A named memory cell that stores a value", "A function that returns nothing", "A file type", "A comment in the code"])},
    {"correct": 0,
     "ru": ("Что делает интерпретатор?", ["Выполняет код построчно", "Сжимает файлы", "Хранит данные на диске", "Рисует графики"]),
     "en": ("What does an interpreter do?", ["Executes code line by line", "Compresses files", "Stores data on disk", "Draws charts"])},
    {"correct": 0,
     "ru": ("Что такое список (list)?", ["Упорядоченная изменяемая коллекция значений", "Одно неизменяемое число", "Текст в кавычках", "Название функции"]),
     "en": ("What is a list?", ["An ordered, mutable collection of values", "A single immutable number", "A quoted text", "A function name"])},
    {"correct": 0,
     "ru": ("Зачем нужна функция?", ["Чтобы многократно выполнять один и тот же блок кода", "Чтобы хранить файлы", "Чтобы подключаться к интернету", "Чтобы менять цвет экрана"]),
     "en": ("Why do we use functions?", ["To run the same block of code many times", "To store files", "To connect to the internet", "To change the screen colour"])},
    {"correct": 0,
     "ru": ("Что делает цикл for?", ["Повторяет действие для каждого элемента последовательности", "Удаляет переменную", "Навсегда останавливает программу", "Создаёт новый файл"]),
     "en": ("What does a for loop do?", ["Repeats an action for each item in a sequence", "Deletes a variable", "Stops the program forever", "Creates a new file"])},
    {"correct": 0,
     "ru": ("Что такое строка (str)?", ["Последовательность символов", "Значение True или False", "Число с плавающей точкой", "Список функций"]),
     "en": ("What is a string (str)?", ["A sequence of characters", "A True or False value", "A floating-point number", "A list of functions"])},
    {"correct": 0,
     "ru": ("Что такое словарь (dict)?", ["Набор пар «ключ — значение»", "Цикл с условием", "Текстовый файл", "Модуль для графиков"]),
     "en": ("What is a dictionary (dict)?", ["A set of key–value pairs", "A loop with a condition", "A text file", "A plotting module"])},
    {"correct": 0,
     "ru": ("Для чего нужен комментарий в коде?", ["Для пояснений, которые интерпретатор пропускает", "Для ускорения программы", "Для подключения библиотек", "Для шифрования данных"]),
     "en": ("What is a comment in code for?", ["Explanations that the interpreter ignores", "Speeding up the program", "Importing libraries", "Encrypting data"])},
    {"correct": 0,
     "ru": ("Что такое библиотека?", ["Готовый набор функций, который подключают в программу", "Папка с документами", "Ошибка в коде", "Тип цикла"]),
     "en": ("What is a library?", ["A ready-made set of functions you import into a program", "A folder with documents", "An error in the code", "A type of loop"])},
    {"correct": 0,
     "ru": ("Какой тип данных хранит целое число?", ["int", "str", "bool", "list"]),
     "en": ("Which data type stores whole numbers?", ["int", "str", "bool", "list"])},
]


def register():
    name = input("Имя: ")
    surname = input("Фамилия: ")
    faculty = input(f"Факультет {FACULTIES}: ")
    name = random.choice(NAMES)
    surname = random.choice(SURNAMES)
    faculty = random.choice(FACULTIES)
    print(f"\nВаши данные в деканате: {name} {surname}, факультет {faculty}")


def quiz():
    score = 0
    total = 0
    for i in range(1, len(QUESTIONS)):
        q = QUESTIONS[i]
        q_lang, a_lang = ("en", "ru") if i % 2 == 0 else ("ru", "en")
        question = q[q_lang][0]
        options = q[a_lang][1]
        order = list(range(len(options)))
        random.shuffle(order)
        print(f"\nВопрос {i+1}/{len(QUESTIONS)}: {question}")
        for n, idx in enumerate(order, 1):
            print(f"  {n}. {options[idx]}")
        answer = int(input("Ваш ответ (номер): ")) - 1
        if answer == q["correct"]:
            score += 1
        else:
            score -= 1
            total += 1
    print(f"\nТвой балл: {score} из {total}")


def corrupt(text):
    words = text.split()
    for i, w in enumerate(words):
        r = random.random()
        if r < 0.12:
            words.pop(i)
        elif r < 0.22:
            words.insert(i, random.choice(EXTRA))
    return " ".join(words)


def print_document():
    print("\nДокумент (Устав ООН, отрывки):")
    lines = [corrupt(p) for p in ORIGINAL]
    for line in lines:
        print(line)
        print()
    return lines


def check(lines):
    if lines == ORIGINAL:
        print("✓ Документ совпадает с оригиналом")
    else:
        bad = sum(a != b for a, b in zip(lines, ORIGINAL))
        print(f"✗ Документ не совпадает с оригиналом, абзацев с ошибками: {bad}")


def main():
    print("Добро пожаловать в электронный деканат!\n")
    register()
    quiz()
    lines = print_document()
    check(lines)


if __name__ == "__main__":
    main()
