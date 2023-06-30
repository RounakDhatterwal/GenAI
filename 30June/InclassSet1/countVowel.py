def countVowel(str) : 
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in str:
        if(char.lower() in vowels):
            count+=1

    return count

str = "Apple"
vowel = countVowel(str)
print(f"Number of Vowel: {vowel}")
