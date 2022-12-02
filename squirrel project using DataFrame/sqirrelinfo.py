import pandas as pd

data = pd.read_csv('2018_squirrel.csv')
gray_sq = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_sq = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sq = len(data[data["Primary Fur Color"] == "Black"])

print("Grey :", gray_sq)
print("Cinnamon :", cinnamon_sq)
print("Black :", black_sq)

datadict = {"fur color": ["Grey", "Cinnamon", "Black"], "No of squirrels": [gray_sq, cinnamon_sq, black_sq]}
print((datadict))
df = pd.DataFrame(datadict)
df.to_csv("final_squirrel.csv")