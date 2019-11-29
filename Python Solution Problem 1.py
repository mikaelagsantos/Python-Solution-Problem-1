from matplotlib import pyplot as plt
def f(n):
    if n < 9:
        return n * n - 7
    return f(n-10)

x_values = []
y_values = []

for i in range(0,100):
    x_values.append(i)
    y_values.append(f(i))
    
print('The x values are: \n', x_values)
print('The y values are: \n', y_values)

plt.stem(x_values, y_values, use_line_collection=True)

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('Graph for function f(n)')
plt.show()

