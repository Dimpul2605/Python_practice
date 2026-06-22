#first

# for num in range (1,6):
#     print("*"*num)

#second
# for num in range(5,0,-1):
#     print("*"*num)

#third
# for row in range (1,6):
#     for num in range (1,row +1):
#         print(num,end="")
#     print()

# fourth pattern
# for row in range(1,6):
#     for num in range(row,6):
#         print(num,end="")
#     print()

#fifth pattern pyramid
# n=5
# for i in range (n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(2*i+1):
#         print("*",end="")
#     print()

#sixth pattern square
# n=5
# for i in range(n):
#     for j in range(1,n+1):
#         print("* ",end="")
#     print()

# seventh pattern rectangle   
n=5
for i in range(n):
    for j in range(1,n+1):
        print(" "*(5-j) +"*"*(2*j-6), end="")
    print()

