# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 09:06:06 2021
@author: liuzihao

模拟mRNA翻译成蛋白质的过程
#how
#拆分，后根据密码子表匹配
input :AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
output :MAMAPRTEINSTRING
"""
import re

class Protein:
    def __init__(self):
        self.__pro_dic = {'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A', 'CGU':'R', 'CGC':'R',

    'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R', 'UCU':'S', 'UCC':'S',

    'UCA':'S', 'UCG':'S', 'AGU':'S', 'AGC':'S', 'AUU':'I', 'AUC':'I',

    'AUA':'I', 'UUA':'L', 'UUG':'L', 'CUU':'L', 'CUC':'L', 'CUA':'L',

    'CUG':'L', 'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G', 'GUU':'V',

    'GUC':'V', 'GUA':'V', 'GUG':'V', 'ACU':'T', 'ACC':'T', 'ACA':'T',

    'ACG':'T', 'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 'AAU':'N',

    'AAC':'N', 'GAU':'D', 'GAC':'D', 'UGU':'C', 'UGC':'C', 'CAA':'Q',

    'CAG':'Q', 'GAA':'E', 'GAG':'E', 'CAU':'H', 'CAC':'H', 'AAA':'K',

    'AAG':'K', 'UUU':'F', 'UUC':'F', 'UAU':'Y', 'UAC':'Y', 'AUG':'M',

    'UGG':'W','UAG':'', 'UGA':'', 'UAA':''}
    def get_protein(self,seq):
        seq = seq.upper()
        #while len(seq) % 3 != 0:
        #    seq = seq[:len(seq) - 1]
        
        #split string by re
        seq = re.findall(r".{3}",seq)
        prot_dt = []
        for codon in seq:
            prot_dt.append(self.__pro_dic[codon])
        #list 2 string
        prot_dt = "".join(prot_dt)
        return prot_dt

def main():
    a = Protein()
    AA = a.get_protein(seq="AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA")
    print(AA)
if __name__ == '__main__':
    main()


