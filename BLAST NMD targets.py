import os
from Bio.Blast.Applications import NcbiblastnCommandline, NcbiblastpCommandline

'''Делаем BLAST транскриптов NMD на транскриптом Phytozome v12'''


query_file=r'C:\blast\query\smg1_assembled_transcripts_v1.6_broadNMDtargets_translation.fasta'
DB_file=r'C:\blast\db\Physcomitrella_patens.Phypa_V3.pep.all.fasta'
out_file=r'C:\blast\results\broadNMD_againstAllpepPhytozome'

#cmd='makeblastdb -in {0} -dbtype prot'.format(DB_file)
#os.system(cmd)

blast=NcbiblastpCommandline(cmd='blastp', query=query_file, db=DB_file,outfmt=5,out=out_file,word_size=2,evalue=0.001)
stdout,stderr=blast()


