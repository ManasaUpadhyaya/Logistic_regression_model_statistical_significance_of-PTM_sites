import pandas as pd

'''
Thsi script computes the values of the average, minimum and maximum values and appends it into separate dictionaries."
'''
result_check  = {}
results_within_motif = pd.read_csv("Result_table.csv")

dict_evals_fin = {}
for row, column in results_within_motif.iterrows():
    UID = column[1]
    site = column[2]
    eval = column[5]
    key_fin = (UID, site)
    if key_fin in dict_evals_fin:
        dict_evals_fin[key_fin].append(eval)
    if key_fin not in dict_evals_fin:
        dict_evals_fin[key_fin] = [eval]
number_of_evals = {}
for i in dict_evals_fin:
    number_of_evals[i] = len(dict_evals_fin[i])
#print(number_of_evals)

min_eval = {}
for i in dict_evals_fin:
    min_eval[i] = min(dict_evals_fin[i])

max_eval = {}
for i in dict_evals_fin:
    max_eval[i] = max(dict_evals_fin[i])

avg_eval = {}
for i in dict_evals_fin:
    avg_eval[i] = sum(dict_evals_fin[i])/ len(dict_evals_fin)


