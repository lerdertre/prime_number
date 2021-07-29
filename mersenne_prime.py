p = int(input("输入一个正整数p："))
# 运算2^n-1，计算梅森素数
m=2**p-1
print("将要计算{}是不是梅森素数".format(m))
for i in range(2,m):
    if m%i==0:
        print("{}不是素数".format(m))
        break
else:
    print("{}是素数".format(m))
