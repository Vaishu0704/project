from collections import Counter
mylist=[2,3,4,5,6,8,7,6,5,18]
shoe_counter=Counter(mylist)
print(shoe_counter)
a=int(input('Enter the no.of shoes\n'))
t=0
for _ in range(1,a+1):
    size=int(input('Enter the size of the shoe\n'))
    amt=int(input('Enter the amount of the shoe\n'))
    if shoe_counter.get(size,0)>0:
        t=t+amt
        shoe_counter[size]-=1

    else:
        print(f'Size{size} is not available or out of  stock')
print(t)