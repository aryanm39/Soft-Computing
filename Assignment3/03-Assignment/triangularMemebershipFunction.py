import matplotlib.pyplot as plt

a = float(input("Enter a : "))
b = float(input("Enter b : "))

m = (a + b) / 2
x = (a,m,b)
y = (0,1,0)

plt.plot(x,y)
plt.show()

x = float(input("Enter The Element : "))
if x <= a:
    mem = 0
elif x > a and x <= m:
    mem = (x - a) / (m - a)
elif x > m and x < b:
    mem = (b - x) / (b - m)
else:
    mem = 0

print("Membership : ",mem)