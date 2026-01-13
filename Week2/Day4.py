'''
Write a Python function called count_word_frequency(sentence) that:
Takes a string sentence as input. Ignores case sensitivity (treat "Python" and "python" as the same word). Removes punctuation (.,!?). Returns a dictionary where: Keys are unique words in the sentence
Values are the number of times each word appears
sentence = "Python is great, and Python is fun!"
print(count_word_frequency(sentence))
result : {'python': 2, 'is': 2, 'great': 1, 'and': 1, 'fun': 1}
'''

# def count_word_frequency(sentence):
#     sentence = sentence.replace(',','')
#     sentence = sentence.replace('.','')
#     sentence = sentence.replace('!','')
#     sentence = sentence.replace('?','')
#     words = sentence.split(' ')
#     word_freq = {}
#     for word in words:
#         if word in word_freq:
#             word_freq[word] +=1
#         else:
#             word_freq[word] = 1
#     return word_freq
#
# sentence = "?Python is great, and. Python is fun!"
# print(count_word_frequency(sentence))

'''
Write a Python function called is_balanced(s) that:
Takes a string s containing only parentheses ( and ).
Returns True if the parentheses are balanced, otherwise returns False.
A string is considered balanced if:
Every opening parenthesis has a corresponding closing one.
No closing parenthesis appears before a matching opening one.

Example :
print(is_balanced("(()())"))   # True
print(is_balanced("(()"))      # False
print(is_balanced("())("))     # False
'''

# def is_balanced(paranthesis):
#     count = 0
#     for char in paranthesis:
#         if char == '(':
#             count+=1
#         elif char == ')':
#             count-=1
#         if count < 0:
#             return False
#     return count == 0
# print(is_balanced("(()())"))   # True
# print(is_balanced("(()"))      # False
# print(is_balanced("())("))     # False

'''
Write a function validate_password(password) that:
Minimum length 8
Must contain at least one digit
Must contain at least one uppercase letter
Return True or False
'''
def password_checker(password):
    pass

'''
Write a function common_elements(list1, list2) that:
Returns a list of common elements (no duplicates)
Input: [1,2,3,4], [3,4,5,6]
Output: [3,4]
'''
# def common_elements(list1, list2):
#     common = []
#     for num in list1:
#         if num in list2:
#             common.append(num)
#     return common
# print(common_elements([1,2,3,4], [3,4,5,6]))
'''
Write a function rotate_list(lst, k) that:
Rotates list right by k positions
Example :
    Input: [1,2,3,4,5], k=2
    Output: [4,5,1,2,3]
'''
# def rotate_list(lst, k):
#     for _ in range(k):
#         last = lst.pop()
#         lst.insert(0,last)
#     return lst
# print(rotate_list([1,2,3,4,5], k=2))



