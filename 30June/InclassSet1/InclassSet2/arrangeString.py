def arrange_lowercase_first(str):
    lowercase = ""
    uppercase = ""
    for char in string:
        if char.islower():
            lowercase += char
        else:
            uppercase += char
    arranged_string = lowercase + uppercase
    return arranged_string

str = "PyNaTive"

string = arrange_lowercase_first(str)

print(string)
