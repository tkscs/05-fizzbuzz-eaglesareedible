maxnumber = 15
r = 3
s = 5
for i in range(1, 16):
    if i ==maxnumber:
        print('fizzbuzz')
    elif i % r ==0:
        print('fizz')
    elif i % s ==0:
        print('buzz')
    else:
        print(i)