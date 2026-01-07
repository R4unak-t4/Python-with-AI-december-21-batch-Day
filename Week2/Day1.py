# Dictionary

# Dictionary is enclosed in curly braces

# Dictionary items are stored in key value pairs

# Keys in a single dictionary needs to have different names
# my_dictionary = {
#                  'first name' : 'Raunak',
#                  'last name' : 'Thapa'
#                  }
#
# print(f'my name is {my_dictionary['first name']} {my_dictionary['last name']}')

# For in loop on dictionary
# my_dictionary = {
#                  'first name' : 'Raunak',
#                  'last name' : 'Thapa'
#                  }
# for key,value in my_dictionary.items():
#     print(value)

# .keys()
# var = 'first name'
# var = 'last name'

# .values()
# var = 'Raunak'
# var = 'Thapa'

# Replace
my_dictionary = {
                 'first name' : 'Raunak',
                 'last name' : 'Thapa'
                 }
my_dictionary['last name'] = 'Magar'

# .pop()
# my_dictionary.pop('first name')
# print(my_dictionary)
# print(my_dictionary.pop('first name'))

# del
del my_dictionary['first name']
# print(my_dictionary)

info = {
    'class name':'Classroom',
    'class no' : 11,
    'class area' : 44.5,
    'is class available' : True,
    'students' : ['raunak', 'smriti', 'rohan'],
}
# task take input for class name, class no, class area, is class available and students list and store them in the above manner.

# after storing in dictionary print the class name, class no , class area , print every student's name using loop and print yes if the class available and no if the class is unavailable.

# info = {
#     'class name':'Classroom',
#     'class no' : 11,
#     'class area' : 44.5,
#     'is class available' : True,
#     'students' : ['raunak', 'smriti', 'rohan'],
# }
info1 = {
    'class name': None,
    'class no' : None,
    'class area' : None,
    'is class available' : None,
    'students' : None,
}

class_name = input('Enter class name : ')
class_no = int(input('Enter class number : '))
class_area = float(input('Enter class area : '))
class_availability = bool(input('Enter class availability status : '))
students_ = []
while True:
    student_name = input("Enter student's name : " )
    students_.append(student_name)
    des = input('Do you want to enter more students? (no if you want to exit) : ')
    if des.strip().lower() == 'no':
        break

info1['class name'] = class_name
info1['class no'] = class_no
info1['class area'] = class_area
info1['is class available'] = class_availability
info1['students'] = students_

print(f'Class Name : {info1['class name']}')
print(f'Class no : {info1['class no']}')
print(f'Class area : {info1['class area']}')
if info1['is class available']:
    print('Class is available!')
else:
    print('Class is unavailable!')
print(f'Students in class {info1['class name']}')
for student in info1['students']:
    print(student)



