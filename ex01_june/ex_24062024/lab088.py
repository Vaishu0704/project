letters=['a','b','d','e','i','j','o','u']

def vowel_filter(letter):
    vowels=['a','e','i','o','u']
    return letter in vowels
result=vowel_filter('a')
print(result)

new_vowel_filter=filter(vowel_filter,letters)
print(list(new_vowel_filter))