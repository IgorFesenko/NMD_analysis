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
lst_pep = ''

# potein database
prot_database = ''

# output
out_table = pd.DataFrame(columns=['Sequence', 'Proteins'])

# create list of peptides
with open(lst_pep) as input_file:
    peptides = set([i.strip() for i in input_file.readlines()])

out_table.append(map(CheckPep, peptides))

print(out_table.head(5).to_string())
