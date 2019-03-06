# results BLAST sureNMD against all proteins Phytozome v12
from Bio.Blast import NCBIXML
import pandas as pd

#results file
out_file = r'C:\blast\results\sureNMD_againstAllpepPhytozome'

#parsing BLAST results
result_handle = open(out_file)
blast_records = NCBIXML.parse(result_handle)
results={}
cnt=0

for alignment in blast_records:

    if (len(alignment.alignments))!=0:

        results[alignment.query] = []
        l=alignment.query_letters
        for hit in alignment.alignments: # отбор результатов, с 95% перекрытием
            for hsp in hit.hsps:
                p = hsp.identities
                d = hit.length
                c = hsp.align_length
                if p==l:
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

df.to_excel(r'D:\Google Диск\NMD moss\Lloyd\sureNMD_pepMatches.xlsx')