import csv
from collections import Counter

with open("data.csv",newline="") as x:
    reader = csv.reader(x)
    filedata = list(reader)
filedata.pop(0)
newdata = []
for y in range(len(filedata)):
    height = filedata[y][1]
    newdata.append(float(height))

k = Counter(newdata)
range = {
    "50-60":0,
    "60-70":0,
    "70-80":0,
}
for height ,x in k.items():
    if 50<float(height)<60:
        range["50-60"]+=x
    elif 60<float(height)<70:
        range["60-70"]+=x
    elif 70<float(height)<80:
        range["70-80"]+=x
print(range)