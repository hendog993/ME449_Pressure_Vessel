import csv
from pprint import pprint as pr
from matplotlib import pyplot as plt

with open("raw_data.csv", 'r') as master:
    csvout = csv.reader(master)
    csvf = [row for row in csvout]

# Reference data
pressures_ascending = csvf[1][1:9]
zeroed_reference = csvf[1]
pressures_descending = csvf[17][1:9]

pois = .33
youngs = 2e6

# Ascending data. Each variable is the strain gage data
# from 0-400 psig.
a1 =  csvf[31][1:9]
a2 =  csvf[32][1:9]
a3 =  csvf[33][1:9]
a4 =  csvf[34][1:9]
a5 =  csvf[35][1:9]
a6 =  csvf[36][1:9]
a7 =  csvf[37][1:9]
a8 =  csvf[38][1:9]
a9 =  csvf[39][1:9]
a10 =  csvf[40][1:9]
a11 = csvf[41][1:9]

# Descending data
d1 = csvf[45][1:9]
d2 = csvf[46][1:9]
d3 = csvf[47][1:9]
d4 = csvf[48][1:9]
d5 = csvf[49][1:9]
d6 = csvf[50][1:9]
d7 = csvf[51][1:9]
d8 = csvf[52][1:9]
d9 = csvf[53][1:9]
d10 = csvf[54][1:9]
d11 = csvf[55][1:9]

# Ascending first
rosette_A = [a1,a2,a3]
rosette_B = [a4,a5,a6]
rosette_C = [a7,a8,a9]
rosette_D = [a10, a11]

# Rosette A calculations.
def per_col_pres(x):
    col = 0
    while col < 8:
        pr(x[0][col])
        pr(x[1][col])
        try:
            pr(x[2][col])
        except IndexError:
            col += 1
            print("\n")
            continue
        print("\n")
        col += 1


per_col_pres(rosette_A)
per_col_pres(rosette_B)
per_col_pres(rosette_C)
per_col_pres(rosette_D)
