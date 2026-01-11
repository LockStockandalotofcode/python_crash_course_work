import matplotlib.pyplot as plt
import matplotlib as mpl

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap='magma', s=10)
# ax.scatter(x_values, y_values, s=10) # simple version
# ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')

plt.show()
# plt.savefig('squares_plot_2.png', bbox_inches='tight')

# plt.colormaps()