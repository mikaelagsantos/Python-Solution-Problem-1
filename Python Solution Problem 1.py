from matplotlib import pyplot as plt
def f(n):
    if n < 9:
        return n * n - 7
    return f(n-10)

x = []
y = []

for i in range(1,100):
    x.append(i)
    y.append(f(i))
    
print(x)
print(y)

plt.plot(x, y)

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('Graph for function f(n)')
plt.show()

