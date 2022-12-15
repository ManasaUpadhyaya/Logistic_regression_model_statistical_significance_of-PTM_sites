'''

The script can be used to produce the graphs in the supplementary section
Matplotlib is the library used
The present script plots the minimum_eval for each ranks of motifs
The script can be changed by calling different columns to generate graphs for other parameters like average and maximum evalue too
'''

import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
final_list = []
deconv = pd.read_csv("with_ranks_updated.csv")


# list_average = deconv["Average_eval"]
# plt.plot(list_average)
# plt.show()
l = []
for idx, i in enumerate(deconv["Motif_ranks"]):
    if i == 1:
        l.append(deconv["Minimum_eval"][idx])
l_2 = []
for idx, i in enumerate(deconv["Motif_ranks"]):
    if i == 2:
        l_2.append(deconv["Minimum_eval"][idx])
l_3 = []
for idx, i in enumerate(deconv["Motif_ranks"]):
    if i == 3:
        l_3.append(deconv["Minimum_eval"][idx])
l_4 = []
for idx, i in enumerate(deconv["Motif_ranks"]):
    if i == 4:
        l_4.append(deconv["Minimum_eval"][idx])


fig, axs = plt.subplots(4)
axs[0].plot(l)
axs[1].plot(l_2)
axs[2].plot(l_3)
axs[3].plot(l_4)
plt.xlabel("Number of Datapoints in each class of Motif_ranks")
plt.ylabel("Minimum eval")
plt.show()


# count = 0

# for row, column in deconv.iterrows():
#     list_motif_ranks = []
#     if column[19] <= 2:
#         list_motif_ranks.append(1)
#     elif column[19] >2 and column[19] <=4 :
#         list_motif_ranks.append(2)
#     elif column[19] >4 and column[19] <= 6:
#         list_motif_ranks.append(3)
#     else:
#         list_motif_ranks.append(4)
#     final_list.append(list_motif_ranks[0])
#
#
# deconv["Motif_ranks"] = final_list
# deconv.to_csv("with_ranks_updated.csv")
