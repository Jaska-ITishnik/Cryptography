# Create your tests here.


# python code first of all

# ******************************************************************************************************

# 2 - task
# n>0 и a<0 найти b=a mod n

# n = int(input('Enter divisor n: '))
# a = int(input('Enter divisible a: '))
# res = a % n
# while res < 0:
#     res += a
# print(res)

# ******************************************************************************************************

# 3 - task (e*d)modn=1 задана e и n найдите d?

# print('(e*d)modn=1 задана e и n найдите d?')
# sleep(2)
# n = int(input('Enter n: '))
# e = int(input('Enter e: '))
# U = [n, 1, 0]
# V = [e, 0, 1]
# T = [U[0] % V[0], U[1] - (U[0] // V[0]) * V[1], U[2] - (U[0] // V[0]) * V[2]]
# while T[0] != 1:
#     U = V
#     V = T
#     T = [U[0] % V[0], U[1] - (U[0] // V[0]) * V[1], U[2] - (U[0] // V[0]) * V[2]]
# print(f"Result d = {T[-1]}")

# ******************************************************************************************************

# 4 - task X2- >Y10
# '11010110'

# x2 = (input('Enter X2: '))[::-1]
# print(sum(2 ** i * int(x2[i]) for i in range(len(x2))))

# ******************************************************************************************************

# 4 - task X8- > Y10
# 110010111101
# x8 = input('Enter X8: ')[::-1]
# res = ''
# while x8 > 2:
#     res += f"{x8 % 2}"
#     x8 = x8 // 2
# res = (res + str(x8))
# print(sum(8 ** i * int(x8[i]) for i in range(len(x8))))

# ******************************************************************************************************

# x16 = input('Enter x16: ')
a, b, c, d, e, f = ' 10', ' 11', ' 12', ' 13', ' 14', ' 15'
res = ''
for i in x16:
    if i.lower() == 'a':
        res += a
    elif i.lower() == 'b':
        res += b
    elif i.lower() == 'c':
        res += c
    elif i.lower() == 'd':
        res += d
    elif i.lower() == 'e':
        res += e
    elif i.lower() == 'f':
        res += f
    else:
        res += i
res = res.split()[::-1]
# print(sum(16 ** i * int(res[i]) for i in range(len(res))))

# ******************************************************************************************************

