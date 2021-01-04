# def 函数(a,b,c):# 必选参数
#     和=a+b+c
#     print('这些数字的和是%r'%和)
#     pass
# 函数(1,1,2)

# def 函数求和(*args): # 可变函数
#     r=0
#     for i in args:
#         r+=i
#         pass
#     print(r)
#     pass
# 函数求和(3,5,6)

for i in range(1,10):
    for j in range(1,10):
        print('%r X %r = %r'%(i,j,i*j))
    print(' ')
