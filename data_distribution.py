import numpy as np
import matplotlib.pyplot as plt

marks = np.array([12, 99, 65, 85, 42])
names = np.array(["Andy", "Martin", "Zahara", "Vuyo", "Ziyaad"])
plt.xlabel("Students")
plt.ylabel("Mark (%)")
plt.title("Student marks")
plt.bar(names, marks)
plt.show()
