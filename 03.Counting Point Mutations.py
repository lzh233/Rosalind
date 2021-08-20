# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 22:01:35 2021

@author: lzh
在信息论中，两个等长字符串之间的汉明距离（英语：Hamming distance）是两个字符串对应位置的不同字符的个数。
换句话说，它就是将一个字符串变换成另外一个字符串所需要替换的字符个数。
例如：

1011101与1001001之间的汉明距离是2。
2143896与2233796之间的汉明距离是3。
"toned"与"roses"之间的汉明距离是3。
"""

def hmm(seq1,seq2):
    hmm_dis = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            hmm_dis += 1
    return hmm_dis


if __name__ == '__main__':           
      dis = hmm(seq1="ATGCCC",seq2="ATCCCG")  
      print(dis)