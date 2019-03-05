
from Bio import SeqIO

seq_file = r'D:\Google Диск\NMD moss\Lloyd\smg1_assembled_transcripts_v1.6_sureNMDtargetsOnly.fasta'
out_file = r'D:\Google Диск\NMD moss\Lloyd\smg1_assembled_transcripts_v1.6_sureNMDtargets_translation_withAUG.txt'


for record in SeqIO.parse(seq_file, 'fasta'):
    print(record)
    messenger_rna = record.seq

    translation1 = messenger_rna.translate()
    translation2 = messenger_rna[1:].translate()
    translation3 = messenger_rna[2:].translate()
    lst_translation = [translation1,translation2,translation3]
    frame_number = ['frame1', 'frame2', 'frame3']
    for i in range(3):
        pep_numb=0
        for pep in lst_translation[i].split('*'):
            if 'M' in pep:
                position = pep.find('M')
                new_seq = pep[position:]
                if len(new_seq) >= 30:
                    pep_numb += 1
                    with open(out_file, 'a') as out:
                        out.write('>' + record.id + '_' + frame_number[i] + ' ' + 'peptide' + str(pep_numb) + '\n')
                        out.write(str(new_seq) + '\n')
