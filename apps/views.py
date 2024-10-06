from django.contrib import messages
from django.shortcuts import render


def index(request):
    return render(request, 'cryptography/main.html')


def find_mode(request):
    result = None
    if request.method == 'POST':
        n = int(request.POST['n'])
        a = int(request.POST['a'])
        result = a % n
    return render(request, 'cryptography/find_mode.html', {'result': result})


def find_d(request):
    result = None
    if request.method == 'POST':
        n = int(request.POST['n'])
        e = int(request.POST['e'])
        U = [n, 1, 0]
        V = [e, 0, 1]
        T = [U[0] % V[0], U[1] - (U[0] // V[0]) * V[1], U[2] - (U[0] // V[0]) * V[2]]
        while T[0] != 1:
            U = V
            V = T
            if U[0] % V[0] != 0:
                T = [U[0] % V[0], U[1] - (U[0] // V[0]) * V[1], U[2] - (U[0] // V[0]) * V[2]]
            else:
                messages.add_message(request, messages.INFO, message='Zero division error!')
                break
        if T[-1]:
            result = T[-1]
    return render(request, 'cryptography/find_d.html', {'result': result})


def x2_y10(request):
    result = None
    if request.method == 'POST':
        binary = request.POST['binary'][::-1]
        if not set(binary).issubset({'0', '1'}):
            messages.add_message(request, messages.INFO, message='Binary contains only 0 or 1 !')
        else:
            result = sum(2 ** i * int(binary[i]) for i in range(len(binary)))
    return render(request, 'cryptography/x2_y10.html', {'result': result})


def x8_y10(request):
    result = None
    if request.method == 'POST':
        octal = request.POST['octal']
        if not octal.isdigit():
            messages.add_message(request, messages.INFO, message='Enter valid value!')
        else:
            octal = octal[::-1]
            result = sum(8 ** i * int(octal[i]) for i in range(len(octal)))
    return render(request, 'cryptography/x8_y10.html', {'result': result})


def x16_y10(request):
    result = None
    if request.method == 'POST':
        hexadecimal = request.POST['hexadecimal']
        if not set(hexadecimal).issubset(
                {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd',
                 'e', 'f'}):
            messages.add_message(request, messages.INFO, message='Enter valid hexadecimal!')
        else:
            a, b, c, d, e, f = ' 10', ' 11', ' 12', ' 13', ' 14', ' 15'
            res = ''
            for i in hexadecimal:
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
            result = sum(16 ** i * int(res[i]) for i in range(len(res)))
    return render(request, 'cryptography/x16_y10.html', {'result': result})
