import matplotlib.pyplot as plot

input_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plot.style.use('ggplot')
fig, ax = plot.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plot.cm.Blues, s=10)

ax.axis([0, 5100, 0, 1_000_000])

ax.set_title("Cubed Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of values", fontsize=14)

plot.savefig('cubes_plot.png', bbox_inches='tight')

plot.show()