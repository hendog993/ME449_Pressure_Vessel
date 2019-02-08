import csv
from matplotlib import pyplot as plt
import numpy as np
from pprint import pprint as prt

"""
File objectives: For each pressure reading, for each rosette,
calculate the principal stresses.

Each rosette is an object. Each instance has
"""


# Section to open new data.
with open("raw.csv","r") as master:
    csv_file_object = csv.reader(master)
    data = [row for row in csv_file_object]
    master.close()

var = np.transpose(data)

ascending_A = var[1][2:5], var[2][2:5], var[3][2:5],var[4][2:5], \
              var[5][2:5], var[6][2:5], var[7][2:5], var[8][2:5]

ascending_B = var[1][6:9], var[2][6:9], var[3][6:9],var[4][6:9], \
              var[5][6:9], var[6][6:9], var[7][6:9], var[8][6:9]

ascending_C = var[1][10:12], var[2][10:12], var[3][10:12],var[4][10:12], \
              var[5][10:12], var[6][10:12], var[7][10:12], var[8][10:12]

ascending_D = var[1][14:17], var[2][14:17], var[3][14:17],var[4][14:17], \
              var[5][14:17], var[6][14:17], var[7][14:17], var[8][14:17]

descending_A = var[1][19:22], var[2][19:22], var[3][19:22],var[4][19:22], \
               var[5][19:22], var[6][19:22], var[7][19:22],var[8][19:22]

descending_B = var[1][23:27], var[2][23:27], var[3][23:27],var[4][23:27], \
               var[5][23:27], var[6][23:27], var[7][23:27],var[8][23:27]

descending_C = var[1][27:30], var[2][27:30], var[3][27:30],var[4][27:30], \
               var[5][27:30], var[6][27:30], var[7][27:30],var[8][27:30]

descending_D = var[1][31:33], var[2][31:33], var[3][31:33],var[4][31:33], \
               var[5][31:33], var[6][31:33], var[7][31:33],var[8][31:33]


