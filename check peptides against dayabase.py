'''This script check the uniques of identified peptides'''
from Bio import SeqIO
import re
import pandas as pd

def CheckPep(pep):
    # create dictionary for obtained results
    pep_dict = {}
    pep_dict[pep] = []
    print('analysing...', pep)
    # searching the matches in database
    for seq in SeqIO.parse(prot_database, 'fasta'):
        if re.findall(pattern=pep, string=str(seq.seq)):
            pep_dict[pep].append(seq.id) # add proteins id in dictionary
    return pep_dict

# list of peptides
lst_pep = r'C:\Users\IGOR_F\YandexDisk\NMD moss\proteome\proteome two repetition\PEAKS\pep_list_smg.txt'

# potein database
prot_database = r'C:\Users\IGOR_F\YandexDisk\NMD moss\db_for_search\Physcomitrella_patens.Phypa_V3.pep.all_chloro_mito+sureNMD_AUG.fasta'

# output
out_file =r'C:\Users\IGOR_F\YandexDisk\NMD moss\proteome\proteome two repetition\PEAKS\uniq_peps_sureNMD_smg.xlsx'
results = pd.DataFrame({'Seq':{}, 'Proteins':{}})

# create list of peptides
with open(lst_pep) as input_file:
    peptides = set([i.strip() for i in input_file.readlines()])


pp = list(map(CheckPep, peptides))
for record in pp:
    for key, val in record.items():
        results = results.append({'Seq': key,'Proteins':','.join(val)}, ignore_index=True)

results.to_excel(out_file)