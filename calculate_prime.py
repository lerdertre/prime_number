n = int(input("输入一个正整数n（n>=2）："))
for i in range(2,n):
    if n%i==0:
        print("{}不是素数".format(n))
        break
else:
    print("是素数".format(n))
