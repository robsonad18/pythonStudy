import pandas as pd
from tabulate import tabulate

list = [
  ["Produto", "Preco", "Qtde"],
  ["Iphone", 6000, 50],
  ["Ipad", 1000, 15],
  ["Airpod", 2000, 100]
]

dis_products = {
  "Produto": ["Iphone","Ipad","Airpod"],
  "Preco":[6000, 10000, 2000],
  "Qtde":[50,15,100]
}

table = pd.read_csv("base.csv")
print(tabulate(table[["CustomerID","idade"]].head(), headers="keys", tablefmt="fancy_grid"))

table.head(1000).to_html("view_front.html")