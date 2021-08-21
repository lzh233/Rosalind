# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 13:31:15 2021

@author: liuzihao
"""
import re
class Consensus:
    @staticmethod
    def read_sequcence(fasta):
        seq = []
        for line in open(fasta):
            if (re.search(r'^>',line) == None):
                seq.append(line.strip().upper())
        return seq

    def __init__(self,fasta):
        self.sequence = Consensus.read_sequcence(fasta)
        self.seq_list_length = len(self.sequence)
        self.seq_length = len(self.sequence[0])
        self.base = ["A","C","G","T"]
    
    def get_consensus(self):
        seq_tmp = []
        seq3 = []
        #提取各个位置的碱基
        for base in range(self.seq_length):
            for seq in range(self.seq_list_length):
                seq_tmp.append(self.sequence[seq][base])

                if len(seq_tmp) == self.seq_list_length:
                    seq3.append(seq_tmp)
                    seq_tmp = []
        
        del seq_tmp
        #统计各个碱基出现的频次
        count_dic = {}
        count_lst = []
        for con in seq3:
            for con_base in self.base:
                count_dic[con_base] = con.count(con_base)
                if len(count_dic) == len(self.base):
                    count_lst.append(count_dic)
                    count_dic = {}
        del count_dic
        #得到Consensus序列
        con_seq = ""
        for i in count_lst:
            res = max(i, key=lambda x: i[x])
            con_seq = con_seq + res
        fd = open('result.txt','a')
        fd_seq = open('Consensus.seq','a')
        
        fd_seq.write(">Consensus\n")
        fd_seq.write(f"{con_seq}")
        
        fd.write(f"{con_seq}\n")
        #计数结果转换，并将结果写入文件
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

        for i in self.base:
            r1 = [str(b) for b in count_restlt[i]]
            r1 =" ".join(r1)
            fd.write(f"{r1}\n")
        fd.close()
        fd_seq.close()
        return con_seq

def main():
    a = Consensus(fasta="07.test_file.fasta")
    seq = a.get_consensus()
    print(f"Consensus: {seq}")
if __name__=='__main__':
    main()

