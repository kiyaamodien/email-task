import matplotlib.pyplot as plt
from scipy import stats

x = [14.2, 16.5, 11.8, 15.3, 18.8, 22.5, 19.5]
y = [220, 330, 190, 340, 410, 445, 415]

slope, intercept, r, p, std_err = stats.linregress(x, y)


def myfunc(x):
    return slope * x + intercept


mymodel = list(map(myfunc, x))

plt.xlabel("Temperature")
plt.ylabel("Price in (R)")
plt.title("Soup sales in relation to temperature")
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
