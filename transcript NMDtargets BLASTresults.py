# results BLAST sureNMD against all transcripts Phytozome v12
from Bio.Blast import NCBIXML
import pandas as pd



out_file = r'C:\blast\results\sureNMD_againstPhytozome'

result_handle = open(out_file)
blast_records = NCBIXML.parse(result_handle) #парсируем результаты бласт
results={}
cnt=0

for alignment in blast_records:
    #print(alignment)
    if (len(alignment.alignments))==0: # записываем уникальные транскрпты
        with open(r'D:\Google Диск\NMD moss\Lloyd\sureNMD_nomatches.txt', 'a') as out:
            out.write(str(alignment.query)+'\n')

    else:
        results[alignment.query] = []
        l=alignment.query_letters
        for hit in alignment.alignments: # отбор результатов, с 95% перекрытием
            for hsp in hit.hsps:
                p = hsp.identities
                d = hit.length
                c = hsp.align_length
                if (c/l)*100>=80:
                    print('****Alignment****')
                    print('sequence:', hit.title, 'query:', alignment.query)
                    print('identities:', p, 'length query:', l, 'aligments length:', c)
                    print('Hit length:', d)
                    print('e value:', hsp.expect)
                    print(hsp.query[0:100] + '...')
                    print(hsp.match[0:100] + '...')
                    print(hsp.sbjct[0:100] + '...')
                    results[alignment.query].append(hit.title)




df = pd. Series(results)

df.to_excel(r'D:\Google Диск\NMD moss\Lloyd\sureNMD_Matches.xlsx')