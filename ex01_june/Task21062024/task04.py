#Count vowels and consonants in a String
name='Vaishnavi'
name.lower()
vowels=0
consonants=0
for i in name:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vowels=vowels+1
    else:
        consonants=consonants+1
print('Total no.of vowels in a string',vowels)
print('Total no.of consonants in a string',consonants)
