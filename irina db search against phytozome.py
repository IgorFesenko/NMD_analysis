from Bio import SeqIO
from multiprocessing.pool import ThreadPool
import pandas as pd
import re

cnt=0
for record in SeqIO.parse(r'D:\Google Диск\NMD moss\IraGaranina\protein_database.fasta', 'fasta'):
    if re.findall(pattern = 'unknown', string = record.id):
        cnt+=1
        print(record.id, len(record.seq))

print(f"записей незвестных рамок:", cnt)