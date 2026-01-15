# use matplotlib.pyplot as plt to make a die-rolling visualisation.

import matplotlib.pyplot as plt

from die import Die

die = Die()
results = []
results = [die.roll() for roll_num in range(1000)]

# Analyzing results.
frequencies = []
poss_results = range(1, die.num_sides+1)
frequencies = [results.count(value) for value in poss_results]

plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()
ax.plot(results, frequencies, linewidth=10)
# ax.scatter(results, frequencies, edgecolors='none', s=10)
plt.show()
# print("Length of results and frequencies:")
# print(len(results))
# print(len(frequencies))