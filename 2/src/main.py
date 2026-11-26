import pandas as pd
# import matplotlib.pyplot as pl
from matplotlib.figure import Figure
import matplotlib.backends.backend_tkagg as tkagg
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Grafice")
root.geometry("1200x800")

data = pd.read_csv("../data/data.csv")

tabs = ttk.Notebook(root)
tabs.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

for col in data.columns:
    tab = ttk.Frame(tabs)
    tabs.add(tab, text=col)

    fig = Figure(figsize=(11, 7), dpi=100)
    pl = fig.subplots()
    pl.plot(data.index, data[col], marker='o', markersize=3, linestyle="-")
    pl.set_title(f"Plot of {col}")
    pl.set_ylabel(col)
    pl.grid(True)
    fig.tight_layout()

    canvas =  tkagg.FigureCanvasTkAgg(fig, master=tab)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Gheorghe are 8 litere
# Andrei are 6 litere
X = 6
Y = 8

tabx = ttk.Frame(tabs)
tabs.add(tabx, text="X")
i = 1
subdata_x = data.head(X)
fig = Figure(figsize=(11, 7), dpi=100)
for col in data.columns:
    if col in ["Durata", "Puls", "Calorii"]:
        pl = fig.add_subplot(1, 3, i)
        pl.plot(subdata_x.index, subdata_x[col], marker='o', markersize=3, linestyle="-")
        pl.set_title(f"Plot of {col}")
        pl.set_ylabel(col)
        pl.grid(True)
        fig.tight_layout()

        i += 1

canvas = tkagg.FigureCanvasTkAgg(fig, master=tabx)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

taby = ttk.Frame(tabs)
tabs.add(taby, text="Y")
i = 1
subdata_y = data.head(Y)
fig = Figure(figsize=(11, 7), dpi=100)
for col in data.columns:
    if col in ["Durata", "Puls"]:
        if i == 1:
            cl = "k"
        else:
            cl = "r"
        pl = fig.add_subplot(1, 2, i)
        pl.plot(subdata_y.index, subdata_y[col], marker='o', markersize=3, linestyle="-", color=cl)
        pl.set_title(f"Plot of {col}")
        pl.set_ylabel(col)
        pl.grid(True)
        fig.tight_layout()

        i += 1

canvas = tkagg.FigureCanvasTkAgg(fig, master=taby)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        


root.mainloop()
    
'''
for col in data.columns:
    pl.figure(figsize=(8, 5))
    pl.plot(data.index, data[col], marker="o", markersize=3, linestyle="-")
    pl.grid(True)
    pl.title(col)

pl.tight_layout()
pl.show()
'''
