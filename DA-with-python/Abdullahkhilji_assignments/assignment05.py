# Q1: Working with Lists

numbers = [10, 20, 15, 8, 25, 30, 12, 7]

total = 0

print("All numbers:")

for number in numbers:
    print(number)
    total = total + number

print("Sum:", total)

print("Even numbers:")

for number in numbers:
    if number % 2 == 0:
        print(number)


# Q2: Dictionary Basics

student = {
    "name": "Abdullah",
    "age": 20,
    "course": "Artificial Intelligence",
    "marks": [70, 80, 60]
}

print("Student Details:")

for key in student:
    print(key, ":", student[key])

total = 0

for mark in student["marks"]:
    total = total + mark

average = total / 3

print("Average:", average)

if average >= 50:
    print("Passed")
else:
    print("Failed")


# Q3: List of Dictionaries

employees = [
    {"name": "Ali", "department": "IT", "salary": 50000},
    {"name": "Sara", "department": "HR", "salary": 60000},
    {"name": "Ahmed", "department": "Finance", "salary": 55000}
]

print("\nEmployee Details:")

highest_salary = 0
highest_employee = ""
total_salary = 0

for employee in employees:
    print("Name:", employee["name"])
    print("Department:", employee["department"])
    print("Salary:", employee["salary"])
    print()

    total_salary = total_salary + employee["salary"]

    if employee["salary"] > highest_salary:
        highest_salary = employee["salary"]
        highest_employee = employee["name"]

print("Highest Salary Employee:", highest_employee)
print("Highest Salary:", highest_salary)
print("Total Salary:", total_salary)


# Q4: While Loop with User Input

numbers = []

print("\nEnter numbers one by one.")
print("Enter -1 to stop.")

while True:
    number = int(input("Enter number: "))

    if number == -1:
        break

    numbers.append(number)

print("List:", numbers)

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

print("Largest number:", largest)
print("Smallest number:", smallest)


# Q5: Word Frequency Counter

sentence = input("\nEnter a sentence: ")

words = sentence.split()

frequency = {}

for word in words:

    if word in frequency:
        frequency[word] = frequency[word] + 1

    else:
        frequency[word] = 1

print("Word Frequency:")

for word in frequency:
    print(word, ":", frequency[word])


# Q6: Multiplication Table

print("Multiplication Table:")

for i in range(1, 6):

    for j in range(1, 6):
        print(i * j, end=" ")

    print()