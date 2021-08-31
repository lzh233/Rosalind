#设定蛋白字典
codon_table = {'GCU':'A', 'GCC':'A', 'GCA':'A', 
                'GCG':'A', 'CGU':'R', 'CGC':'R',
                'CGA':'R', 'CGG':'R', 'AGA':'R', 
                'AGG':'R', 'UCU':'S', 'UCC':'S',
                'UCA':'S', 'UCG':'S', 'AGU':'S', 
                'AGC':'S', 'AUU':'I', 'AUC':'I',
                'AUA':'I', 'UUA':'L', 'UUG':'L', 
                'CUU':'L', 'CUC':'L', 'CUA':'L',
                'CUG':'L', 'GGU':'G', 'GGC':'G', 
                'GGA':'G', 'GGG':'G', 'GUU':'V',
                'GUC':'V', 'GUA':'V', 'GUG':'V', 
                'ACU':'T', 'ACC':'T', 'ACA':'T',
                'ACG':'T', 'CCU':'P', 'CCC':'P', 
                'CCA':'P', 'CCG':'P', 'AAU':'N',
                'AAC':'N', 'GAU':'D', 'GAC':'D', 
                'UGU':'C', 'UGC':'C', 'CAA':'Q',
                'CAG':'Q', 'GAA':'E', 'GAG':'E', 
                'CAU':'H', 'CAC':'H', 'AAA':'K',
                'AAG':'K', 'UUU':'F', 'UUC':'F', 
                'UAU':'Y', 'UAC':'Y', 'AUG':'M',
                'UGG':'W','UAG':'Stop', 'UGA':'Stop', 
                'UAA':'Stop'}
import re
class Orf:
     @staticmethod
     def get_fasta(fasta):
         with open(fasta) as seq:
             seq_lst = [seq.strip() for seq in seq.readlines() if seq.startswith(">") == False]
             seq1 = " ".join(seq_lst)
             seq2 = seq1[::-1].replace("A","t").replace("G","c").replace("C","g").replace("T","a").upper().replace("T","U")
             seq1 = seq1.replace("T","U")
             return seq1,seq2


a = Orf.get_fasta(".//data//11.test_file.txt")
print(a)