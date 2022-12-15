import pandas as pd
sites_table = pd.read_csv("PTM_Table.csv", low_memory=False)
dict_sites_PTM = {}
for row, column in sites_table.iterrows():
    UID = column[2]
    site_pos = int(column[0].split("-")[1]) # this is the variable that holds the site for each row
    if UID in dict_sites_PTM:
        dict_sites_PTM[UID].append(site_pos)
    if UID not in dict_sites_PTM:
        dict_sites_PTM[UID] = [site_pos] # dictionary of all PTM sites from the deconv_jmp table(renamed to PTM table here

# the dict_sites_PTM, the key is the UID and the value is the list of the positions/PTM sites for each UID

interpro_result = pd.read_table("interproscan_results.tsv", sep = "\t")
#interpro_result.columns = ["Protein_accession", "Sequence_MD5_Digest", "Length", "Analysis", "Signature_accession", "Description", "Start_pos", "End_pos", "E-Val", "Status", "Date", "Interpro_anno", "Interpro_anno_2"]
interpro_result_pos = {}
for row, column in interpro_result.iterrows():
    UID = column[0].split("|")[1]
    start = int(column[6])
    stop = int(column[7])
    eval = column[8]
    if eval != "-":
        pos_list = (start, stop, eval)
        if UID in interpro_result_pos:
            interpro_result_pos[UID].append(pos_list)
        if UID not in interpro_result_pos:
            interpro_result_pos[UID] = [pos_list] # this dictionary holds the start, stop and evalue for each motif entry
# the interpro_result dictionary is the UID as the key, and the start stop and evalue for each motif entry as the value

result_appended = []
for UID_PTM in interpro_result_pos: # the two dictionaries are looped through to find the PTM sites within the start and stop positions of the motifs
    if UID_PTM in dict_sites_PTM:
        list_pos = dict_sites_PTM[UID_PTM]
        for pos in list_pos:
            for result_pos in interpro_result_pos[UID_PTM]:
                if pos in range(result_pos[0], result_pos[1]):
                    result = []
                    result.append(UID_PTM)
                    result.append(pos)
                    result.append(result_pos[0])
                    result.append(result_pos[1])
                    result.append(result_pos[2])
                    result_appended.append(result)
# result appended is the list of the UID, pos and the start position, stop position and e-value of the motif the site falls into.
result_df = pd.DataFrame(result_appended)
result_df.columns = ["UID","Site_position","Motif_start_pos", "Motif_stop_pos","E-value"]
result_df.to_csv("Result_table.csv") # final .csv file with the above mentioned columns.
