# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 13:31:15 2021

@author: liuzihao
思路：先按照提取序列，后提取按照位置提取每条序列的对应位置的碱基，最后计数
"""

import re
class Consensus:
    #extracting sequence from fasta
    """
    All sequence should has same length
    """
    @staticmethod
    def read_sequcence(fasta):
        seq = []
        for line in open(fasta):
            if re.search(r'^>',line) == None:
                seq.append(line.strip().upper())
        return seq

    def __init__(self,fasta):
        self.sequence = Consensus.read_sequcence(fasta)
        self.seq_nubmer = len(self.sequence)
        self.seq_length = len(self.sequence[0])
        self.base = ["A","C","G","T"]
    
    def get_consensus(self):
        seq_tmp = []
        seq3 = []
        #extracting base from sequence by index
        for base in range(self.seq_length):
            for seq in range(self.seq_nubmer):
                seq_tmp.append(self.sequence[seq][base])

                if len(seq_tmp) == self.seq_nubmer:
                    seq3.append(seq_tmp)
                    seq_tmp = []
        del seq_tmp

        # frequence of each base in seq3
        count_dic_tmp = {}
        count_lst = []
        for con in seq3:
            for con_base in self.base:
                count_dic_tmp[con_base] = con.count(con_base)
                if len(count_dic_tmp) == len(self.base):
                    count_lst.append(count_dic_tmp)
                    count_dic_tmp = {}
        del count_dic_tmp

        #sequence of Consensus
        con_seq = ""
        for i in count_lst:
            #Find the max values' key
            res = max(i, key=lambda x: i[x])
            con_seq = con_seq + res
        #save sequence of Consensus
        fd = open('result.txt','w')
        fd.write(f"{con_seq}\n")
        
        fd_seq = open('Consensus.seq','w')
        fd_seq.write(f">Consensus\n{con_seq}")
        fd_seq.close()
        
        
        #Convert data
        """
        A:	5	1	0	0	5	5	0	0
        C:	0	0	1	4	2	0	6	1
        ......
        """
        count_restlt = {}
        lst_tmp = []

        for base in self.base:
            for j in count_lst:
                lst_tmp.append(j[base])
                if len(lst_tmp) == len(count_lst):
                    lst_tmp.insert(0,f"{base}:")
                    count_restlt[base] = lst_tmp
                    lst_tmp = []
        del count_lst
        
        #save detail data (count table)
        for i in self.base:
            r1 = [str(b) for b in count_restlt[i]]
            r1 ="\t".join(r1)
            fd.write(f"{r1}\n")
        fd.close()
        
        return con_seq

if __name__=='__main__':
     a = Consensus(fasta=".//data//07.test_file.fasta")
     seq = a.get_consensus()
     print(f"Consensus: {seq}")

##----------otuput-----------##
"""
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
"""