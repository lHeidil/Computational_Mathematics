import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import numpy as np

def power_law(x, a, b):
    return a * np.power(x, -b)

df = pd.read_csv("https://norvig.com/google-books-common-words.txt", delim_whitespace=True, header=None)

index_list = df.index.to_numpy(dtype=float) + 1
freq_list = df[1].to_numpy(dtype=float)

plt.loglog(index_list, freq_list, label='given data')

popt, pcov = curve_fit(power_law, index_list, freq_list, p0=[1, 1], bounds=[[1e-3, 1e-3], [1e20, 50]])

plt.plot(index_list, power_law(index_list, *popt), label='power law')
plt.legend()
plt.show()