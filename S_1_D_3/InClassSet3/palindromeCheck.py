def palindrome(string):
    return string == string[::-1]

string = "madam"
if palindrome(string):
    print("The word madam is a palindrome.")
else:
    print("The word madam is not a palindrome.")
    