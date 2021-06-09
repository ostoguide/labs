import math
#50

print("Задача 50")

a1 = float(input("Введите а1: "))
b1 = float(input("Введите b1: "))
c1 = float(input("Введите c1: "))
a2 = float(input("Введите a2: "))
b2 = float(input("Введите b2: "))
c2 = float(input("Введите c2: "))
eps = 0.0001

if math.fabs(a1*b2 - a2*b1) >= eps:
    x = (b1*c2 - b2*c1)/(a1*b2-a2*b1)
    y = (c1*a2 - c2*a1)/(a1*b2 - a2*b1)
    print("x =", x)
    print("y =", y)
else:
    print("Не виконується умова")

#51
a = int(input("Введите коэффициент a: "))
b = int(input("Введите коэффициент b: "))
c = int(input("Введите коэффициент c: "))

D = b * b - 4 * a * c

if D > 0:
    t1 = (-b) - math.sqrt(D) / 2*a
    t2 = (-b) + math.sqrt(D) / 2*a
    if t1 >= 0:
        x1 = math.sqrt(t1)
        x2 = -math.sqrt(t1)
        print("Корни уравнения: x1 =", x1, "x2 =", x2)
    if t2 >= 0:
        x3 = math.sqrt(t2)
        x4 = -math.sqrt(t2)
        print("x3 = ", x3, "x4 = ", x4)
elif D == 0:
    x1 = -b/2*a
    x2 = -(-b/2*a)
    print("Корни уравнения: x1 =", x1, "x2 =", x2)
elif D < 0:
    print("Корни уравнения отсутствуют")
#60
print("Задача 60")
x = float(input("Введите х: "))
y = float(input("Введите y: "))
u : float

menu = input("Выберите график:\n1 - a\n2 - б\n3 - в\n4 - г\n5 - д\n6 - е\n")
if menu == "1":
    if -2 <= x <= -1 or 1 <= x <= 2 and 1 <= y <= 2:
            u = 0;
    else:
        u = x
if menu == "2":
    if y <= x/2 and math.pow(y,2) >= 1 - math.pow(x,2):
        u = -3
    else:
        u = math.pow(y,2)
if menu == "3":
    if (x*x) + (y - 1)*(y - 1) < 1 and y < (- x*x + 1):
        u = x - y
    else:
        u = x*y + 7
if menu == "4":
    if -1 <= x <= 0 or 0.3 <= x <= 1 and 0.3 <= y < 1:
        u = math.pow(x,2) - 1
    else:
        u = math.sqrt(math.fabs(x-1))
if menu == "5":
    if y > -x and ((x*x) + (y*y)) < 1 and y > x:
        u = math.sqrt(math.fabs(math.pow(x,2) - 1))
    else:
        u = x+y
if menu == "6":
    if (x*x+y*y)<=1 and (y-x)>=0 and (y+x)>=0:
        u = x + y
    else:
        u = x - y
print("u =", u)

#61
x = float(input("Введите десятичное число:"))
x_c = x
if x >= 0:
    x = math.floor(x)
    x1 = math.floor(x)
if x <= 0:
    x = math.ceil(math.fabs(x))
    x1 = math.ceil(x)
x_c1 = int(x_c)
print("Целая часть: ", x)
print("Округлённое до ближайшего целого: ", x1)
print("Число без дробной части:", x_c1)

#70

print("Задача 70")
hour = int(input("Введите часы:"))
minute = int(input("Введите минуты:"))

full_circle = 720
t = 60 * hour + minute 

sovp = round(full_circle * (round(t / (full_circle / 11)) + 1) / 11 - t)

curh = (hour * 30 + minute // 2) % 360
curm = minute * 6
x = (270 + curh) % 360
t1 = (360 + x - curm) % 180
print("Стрелки будут перпендикулярны через",t1*2//11,"минут(ы)")

print("Стрелки совпадут через ",sovp, "минут(ы)")





 