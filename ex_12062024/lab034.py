#write a program that calcuates and displays the letter
#given numerical score are A,B,C,D,F
#A:90-100,B:80-89,C:70-79,D:60-69,F:0-59
score=int(input('Enter the score\n'))
if score>=90 and score<=100:
    print('Grade is A')
elif score>=80 and score<=89:
    print('Grade is B')
elif score>=70 and score<=79:
    print('Grade is C')
elif score>=60 and score<=69:
    print('Grade is D')
elif score>=0 and score<=59:
    print('Grade is F')
else:
    print('Invalid score')