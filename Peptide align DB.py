from Bio import SeqIO
from multiprocessing.pool import ThreadPool
import pandas as pd
import re

def getSequence(pep):
    cnt = 0
    print('analysing', pep)
    for seq in SeqIO.parse(r'C:\Users\IGOR_F\YandexDisk\moss_data\Physcomitrella_patens.Phypa_V3.pep.all.fa\Physcomitrella_patens.Phypa_V3.pep.all.fasta', 'fasta'):
        if re.findall(pattern=pep, string=str(seq.seq)):
            cnt+=1
            #print('FOUND', seq.id)
            if cnt>1:
                break
    if cnt == 1:
        print('Unique')
        return pep






# MaxQuant results
df = pd.read_csv(r'C:\Users\IGOR_F\YandexDisk\NMD moss\proteome\evidence.txt', sep ='\t')
out_pep = set(df['Sequence'])

'''res=df[pd.isnull(df['Accession'])]
pep_lst=list(res['Peptide'])
out_pep=set()
for i in pep_lst:
    res1=re.findall(pattern=r'[ABCDEFGHIJKLMNOPQRSTUVWXYZ]\w*', string=i)
    pep=''.join(res1)
    out_pep.add(pep)'''

print('Анализируем пептиды: ',len(out_pep))


if __name__ == '__main__':
    pool = ThreadPool(4)
    pp = pool.map(getSequence, out_pep)
    pool.close()
    pool.join()

    print('начинаем запись в файл')

    with open(r'C:\Users\IGOR_F\YandexDisk\NMD moss\proteome\ISP_peptides.txt', 'w') as T:

        for i in pp:
            T.write(str(i) + '\n')


print('FINISH')