import matplotlib.pyplot as plt

# defining labels
activities = ['eat', 'sleep', 'work', 'play']

# portion covered by each label
slices = [3, 7, 8, 6]

# plotting the pie chart
plt.pie(slices, labels=activities, explode = (0, 0, 0.1, 0), shadow=True, autopct='%1.2f%%')
plt.legend()

# showing the plot
plt.savefig(fname="./tests/test.jpg")
