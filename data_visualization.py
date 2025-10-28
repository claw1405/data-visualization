import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9 , 16, 25]

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('ggplot')
fig, ax = plt.subplots()
#ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=2)

#This shows how to use gradients in plyplot
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

#ax.plot(input_values, squares, linewidth=3)

# You can save the fig straight to a file 
plt.savefig('squares_plot.png', bbox_inches='tight')

# Set titles
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of values", fontsize=14)

ax.axis([0, 1100, 0, 1_000_000])
ax.ticklabel_format(style='plain')

ax.tick_params(labelsize=14)

plt.show()