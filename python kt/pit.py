# 1. Палиндром

text = input("Введите строку для проверки: ")
text = text.lower().replace(' ', '')

if text == text[::-1]:
    print("Это палиндром!")
else:
    print("Это не палиндром.")


# 2. Трехзначное число

number = int(input("Введите трехзначное число: "))
hundreds = number // 100
tens = (number // 10) % 10
ones = number % 10

print(f"сотни - {hundreds}, десятки - {tens}, единицы - {ones}")


# 3. Поиск общих элементов в двух списках

print("Поиск общих элементов в двух списках:")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_elements = list(set(a) & set(b))
print(f"Общие элементы списков: {common_elements}")


# 4. Выравнивание строк

print("Выравнивание строк:")
strings = ["привет", "солнце", "вселенная", "мир"]
max_len = 0

for s in strings:
    if len(s) > max_len:
        max_len = len(s)

aligned = []
for s in strings:
    aligned.append(s + "_" * (max_len - len(s)))

print(f"Исходный список: {strings}")
print(f"Выровненный список: {aligned}")


# 5. Расчет четвертной оценки

print("Расчет четвертной оценки:")
grades = input("Введите оценки через запятую: ").split(',')
grades = [int(grade.strip()) for grade in grades]

filtered_grades = []
for i in range(len(grades)):
    if grades[i] == 2:
        if i + 1 < len(grades) and grades[i + 1] != 2:
            continue
    filtered_grades.append(grades[i])

average = sum(filtered_grades) / len(filtered_grades)
final_grade = round(average)

print(f"Средний балл: {average:.2f}")
print(f"Итоговая оценка за четверть: {final_grade}")


# 6. Викторина

print("Викторина:")

questions = {
    "Как называется столица Франции?": "Париж",
    "Сколько планет в Солнечной системе?": "Восемь", 
    "Как называется жидкость, заполняющая глазное яблоко?": "Слеза"
}

score = 0
total_questions = len(questions)

for question, correct_answer in questions.items():
    print(f"{question}")
    user_answer = input("Ваш ответ: ").strip()
    
    if user_answer.lower() == correct_answer.lower():
        print("Правильно!")
        score += 1
    else:
        print(f"Неправильно. Правильный ответ: {correct_answer}")

print(f"Викторина завершена!")
print(f"Ваш результат: {score} из {total_questions} правильных ответов")
print(f"Процент правильных ответов: {(score/total_questions)*100:.1f}%")


# 7. Игра Скрабл

print("\nИгра Скрабл:")

points = {
    1:'AEIOULNSTR',
    2:'DG', 
    3:'BCMP',
    4:'FHVWY',
    5:'K',
    8:'JX',
    10:'QZ'
}

word = input("Введите слово на английском языке: ").upper()
score = 0

for letter in word:
    for point_value, letters in points.items():
        if letter in letters:
            score += point_value
            break

print(f"Стоимость слова '{word}': {score} очков")


# 8. Объединение списков

print("Объединение списков:")

list1 = [1, 2, 3]
list2 = [11, 22, 33]

result = []
for i in range(len(list1)):
    result.append(list1[i])
    result.append(list2[i])

print(f"Список 1: {list1}")
print(f"Список 2: {list2}") 
print(f"Результат объединения: {result}")


# 9. Удаление элементов по индексам

print("Удаление элементов по индексам:")

numbers = [1, 44, 7, 9, 3, 2, 1, 44]
print(f"Исходный список: {numbers}")

index1 = int(input("Введите первый индекс: "))
index2 = int(input("Введите второй индекс: "))


indexes = sorted([index1, index2], reverse=True)

for index in indexes:
    if 0 <= index < len(numbers):
        numbers.pop(index)

print(f"Результат: {numbers}")


# 10. Подсчет нулей в конце числа

print("Подсчет нулей в конце числа:")

number = input("Введите число: ")
count = 0

for digit in reversed(number):
    if digit == '0':
        count += 1
    else:
        break

print(f"Количество нулей в конце числа: {count}")

# 11. Поиск ближайшего числа

print("Поиск ближайшего числа:")

numbers = [17, 4, 7, 10, 11, 12]
target = int(input("Введите число: "))

closest = numbers[0]
min_diff = abs(target - numbers[0])

for num in numbers[1:]:
    diff = abs(target - num)
    if diff < min_diff:
        min_diff = diff
        closest = num

print(f"Исходный список: {numbers}")
print(f"Ближайшее число к {target}: {closest}")


# 12. Поиск подстроки между ограничителями

print("Поиск подстроки между ограничителями:")

text = input("Введите строку: ")
start = input("Введите начальный символ: ")
end = input("Введите конечный символ: ")

result = text[text.find(start) + 1:text.find(end)]
print(f"Результат: {result}")

