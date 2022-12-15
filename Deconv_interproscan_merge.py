'''
This script combines the original PTM table(deconv_maps)with the interproscan results table to make the final result table.
Each row has the maximum, minimum and the average evalues for each site falling within a motif
The final file was renamed back to final_table.jmp, the commented portion is the code for adding observation and motif ranks
'''


import pandas as pd
import math
deconv_df = pd.read_csv("Deconv_MAPS.csv")

from add_eval_parameters import dict_evals_fin, min_eval, max_eval, avg_eval, number_of_evals

new_df_values = []
for i in dict_evals_fin:
    temp = []
    temp.append(i[0])
    temp.append(i[1])
    number = number_of_evals[i]
    temp.append(number)
    average = avg_eval[i]
    temp.append(average)
    minimum = min_eval[i]
    temp.append(minimum)
    maximum = max_eval[i]
    temp.append(maximum)
    new_df_values.append(temp)


new_df = pd.DataFrame(new_df_values)
new_df.columns = ["UID_2","POS", "Number_of_motifs", "Average_eval", "Minimum_eval", "Maximum_eval"]

merged_df = pd.merge(deconv_df, new_df,  how='left', left_on=['UID', 'NP'], right_on = ['UID_2', "POS"])
dropped_df = merged_df.dropna(subset = ['UID_2'])

dropped_df.to_csv("Updated_deconv_dropped.csv") # 512015 # 76,478

#for row, column in deconv.iterrows():
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



