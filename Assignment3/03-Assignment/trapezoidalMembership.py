import matplotlib.pyplot as plt

a = float(input("Enter a : "))
b = float(input("Enter b : "))
c = float(input("Enter c : "))
d = float(input("Enter d : "))

x = (a,b,c,d)
y = (0,1,1,0)

plt.plot(x,y)
plt.show()

x = float(input("Enter The Element : "))
if x <= a:
    mem = 0
elif x > a and x <= b:
    mem = (x - a) / (b - a)
elif x > b and x < c:
    mem = 1
elif x >= c and x <= d:
    mem = (d - x) / (d - c)
else:
    mem = 0

print("Membership : ", mem)