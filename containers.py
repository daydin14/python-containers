# Exercise 1
from pkg_resources import DefaultProvider


students = ['David', 'Arnaud', 'Iyana', 'Davis',
            'Jquan', 'Matt', 'Danny', 'Irving', 'Eric']
# ^ This is a list
print('\n ### Exercise 1: \n')
print(f'Second student: {students[1]}')
print(f'Last student: {students[len(students)-1]}')

# Exercise 2
print('\n ### Exercise 2: \n')
foods = ('Orange', 'Grapefruit', 'Cherry', 'Peach', 'Lemon',
         'Lime', 'Blueberry', 'Watermelon', 'Grapes',)
# ^ This is a tuple
for food in foods:
    print(f'{food} is a good food.')

# Exercise 3
print('\n ### Exercise 3: \n')
for food in foods:
    if food == foods[-1] or food == foods[-2]:
        print(food)
# This conditional and print statment can be placed in the above for loop from exercise 2

# Exercise 4
print('\n ### Exercise 4: \n')
home_town = {
    'city': 'my home',
    'state': 'jersey',
    'population': '6',
}
# ^ This is a dictionary
print(
    f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

# Exercise 5
print('\n ### Exercise 5: \n')
for key in home_town:
    print(f"{key} = {home_town[key]}")

# Exercise 6
print('\n ### Exercise 6: \n')
cohort = []
for idx, student in enumerate(students):
    cohort.append(
        {
            'Student': {student},
            'fav_food': {foods[idx]}
        }
    )
print(cohort)

# Exercise 7
print('\n ### Exercise 7: \n')

# Exercise 8
print('\n ### Excercise 8: \n')
