# Задание 1
s = int(input())  
k = 0
for i in range(2, s // 2+1):
    if (a % i == 0):
        k = k+1
if (k <= 0):
    print("Простое")
else:
    print("Не простое")

# Задание 2
a = float(input())
b = float(input())
c = float(input())

if a > b:
    a,b = b,a
if a > c:
    a,c = c,a
if b > c:
    b,c = c,b
    
print (a, "<", b, "<", c)

# Задание 3
arr = [4, 2, 1, 0, 5]
max = arr[0]  

for number in arr:
    if number > max:
        max = number

print("Наибольшое число:", max)
    
# Задание 4
a = int(input())

if a == 0:
    fibanasi_number = 0
elif a == 1:
    fibanasi_number = 1
else:
    fibanasi_prev = 0
    fibanasi_curr = 1

    for i in range(2, a+1):
        fibanasi_number = fibanasi_prev + fibanasi_curr
        fibanasi_prev = fibanasi_curr
        fibanasi_curr = fibanasi_number

print("Число Фибоначчи", a, "равняется", fib_number)

# Задание 5
b = ['asdsd', 'aqwesdqr', 'aghffghfgh', 'alexander', 'qweqweqgrtgrthtyjtyj', 'islam', 'faf', 'hqeqweqweqwe', 'gg']
di = {}
for word in b:
    if word in di.keys():
        di[word] += 1
    else:
        di[word] = 1
key = max(di, key=di.get)
print(key, di[key])
