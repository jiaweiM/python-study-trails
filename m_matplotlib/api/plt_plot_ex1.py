import matplotlib.pyplot as plt

fig = plt.figure()
fig.suptitle("No axes on this figure")

fig, ax_lst = plt.subplots(2, 2)
plt.show()
