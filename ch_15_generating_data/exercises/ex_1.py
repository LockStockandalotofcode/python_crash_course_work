import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)
# ax.plot(x_values, y_values, linewidth=10)

# set chart title and label axes.
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)
# set the size of tick labels.
ax.tick_params(labelsize=14)
# Set the range of each axis.
ax.axis((0, 5_100, 0, 132651000000 ))
ax.ticklabel_format(style='plain')
# Set t

plt.show()