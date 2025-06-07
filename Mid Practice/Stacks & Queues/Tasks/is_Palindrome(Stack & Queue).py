def is_palindrome_stack(word):
    stack = []
    # Push each character onto the stack
    for char in word:
        stack.append(char)
    # Pop each character from the stack and construct a new word
    reversed_word = ""
    while stack:
        reversed_word += stack.pop()
    # Compare original word with the reversed word
    return word == reversed_word
from collections import deque

def is_palindrome_queue(word):
    queue = deque()
    # Enqueue each character into the queue
    for char in word:
        queue.append(char)
    # Dequeue each character from the queue and construct a new word
    reversed_word = ""
    while queue:
        reversed_word += queue.popleft()
    # Compare original word with the reversed word
    return word == reversed_word

word = "radar"
print(is_palindrome_queue(word))  # Output: True

word = "radar"
print(is_palindrome_stack(word))  # Output: True
