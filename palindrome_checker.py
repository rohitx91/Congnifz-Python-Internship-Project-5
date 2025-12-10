# Level 1 - Task 5
# Palindrome Checker Program

def is_palindrome(text):
    text = text.replace(" ", "").lower()  # remove spaces & lowercase
    return text == text[::-1]

# Main Program
user_input = input("Enter a word or number: ")

if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome!")
else:
    print(f"'{user_input}' is NOT a palindrome.")
