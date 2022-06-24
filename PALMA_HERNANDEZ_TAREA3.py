Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
document_actions = Stack()

# The first enters the title of the document
document_actions.push('action: enter; text_id: 1; text: This is my favourite document')
# Next they center the text
document_actions.push('action: format; text_id: 1; alignment: center')
# As with most writers, the user is unhappy with the first draft and undoes the center alignment
document_actions.pop()
# The title is better on the left with bold font
document_actions.push('action: format; text_id: 1; style: bold')
SyntaxError: multiple statements found while compiling a single statement
from collections import deque

# you can initialize a deque with a list 
numbers = deque()

# Use append like before to add elements
numbers.append(99)
numbers.append(15)
numbers.append(82)
numbers.append(50)
numbers.append(47)

# You can pop like a stack
last_item = numbers.pop()
print(last_item) # 47
print(numbers) # deque([99, 15, 82, 50])

# You can dequeue like a queue
first_item = numbers.popleft()
print(first_item) # 99
print(numbers) # deque([15, 82, 50])
SyntaxError: multiple statements found while compiling a single statement
