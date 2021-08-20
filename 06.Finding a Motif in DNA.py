# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 15:06:06 2021
@author: liuzihao

确定DNA中Modif序列出现的位置，模体（Motif）是指序列中局部的保守区域，或者是一组序列中共有的一小段序列模式。
更多的时候是指有可能具有分子功能、结构性质或家族成员相关的任何序列模式。在蛋白质、DNA、RNA序列中都存在
思路: 将dna拆分成k-mer的形式，后将Motif序列与k-mer比对，k-mer对应的索引即为motif序列在序列中出现的位置,由于python的索引从零开始因此最后结果要+1

input:
GATATATGCATATACTT
ATAT
output:
2 4 10
"""
def get_motif(seq,motif_seq):
    seq = seq.upper()
    motif_seq = motif_seq.upper()
    k_mer = len(motif_seq)
    k_mer_nu = len(seq) - len(motif_seq) + 1
    #get k-mer seq
    k_lst = []
    for k in range(k_mer_nu):
        k_lst.append(seq[k:k_mer + k])
    #list for save the index of motif_seq
    mot_index = []
    for inx,val in enumerate(k_lst):
        #enumerate(list) return [(index,list[0]),(index,list[2]),......]
        if val == motif_seq:
            mot_index.append(inx + 1)

    return mot_index

if __name__ == '__main__':
    a = get_motif(seq = "GATATATGCATATACTT",motif_seq="TATA")
    print(a)
