import pandas as pd
import matplotlib as plot

wnba = pd.read_csv("../Data Files/wnba.csv")

wnba["Exp_ordinal"] = "Hello?"
for value in wnba["Experience"]:
    if value == "R":
        wnba["Experience"] = 0

print(wnba)
for years in wnba["Experience"]:
    print("Years = ", years)
    if years == 0:
        wnba["Exp_ordinal"] = "Rookie"
    if years > 0 & years < 4:
        wnba["Exp_ordinal"] = "Little Experience"
    if years >= 4 & years < 6:
        wnba["Exp_ordinal"] = "Experienced"
    if years >= 6 & years < 11:
        wnba["Exp_ordinal"] = "Very Experienced"
    if years >= 11:
        wnba["Exp_ordinal"] = "Veteran"

wnba['Pos'].value_counts().plot.bar()
#wnba["Exp_ordinal"].value_counts().iloc[[3,0,2,1,4]].plot.bar()