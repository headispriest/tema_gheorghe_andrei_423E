import pandas as pd
import matplotlib.pyplot as pl
import matplotlib.backends.backend_tkagg
import tkinter

data = pd.read_csv("../data/data.csv")

for col in data.columns:
    pl.figure(figsize=(8, 5))
    pl.plot(data.index, data[col], marker="o", markersize=3, linestyle="-")
    pl.grid(True)
    pl.title(col)

pl.tight_layout()
pl.show()
