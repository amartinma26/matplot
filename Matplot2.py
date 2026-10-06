import matplotlib.pyplot as plt
import pandas as pd

try:
    df = pd.read_csv("precios_consolas.csv")
except FileNotFoundError:
    print("Ez da fitxategia aurkitu")

valioak = [df["Xbox"].mean(), df["PS5"].mean(), df["Switch"].mean(), df["PC"].mean()]

x = df.columns.drop("dia")
plt.bar(x, valioak)
plt.show()

kontxolak = df[["Switch", "PS5", "Xbox"]]

for kontxola in kontxolak:
  egunak = (df["PC"] > df[kontxola]).sum()

  if egunak > 0:
    print(f"{kontxola}: {egunak} egun egon da PCa baino garestiagoa.")



balioMin = df[["Xbox", "PS5", "Switch"]].min(axis=1)
min_ps5 = (df["PS5"] == balioMin).sum()
min_switch = (df["Switch"] == balioMin).sum()
min_xbox = (df["Xbox"] == balioMin).sum()


print(f"PS5-> {min_ps5} egun merkeagoa kontxolen artean")
print(f"Switch -> {min_switch} egun merkeagoa kontxolen artean ")
print(f"Xbox -> {min_xbox} egun merkeagoa kontxolen artean")


        


