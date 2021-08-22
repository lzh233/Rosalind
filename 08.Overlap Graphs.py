# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 11:41:28 2021

@author: lzh233

URL: http://rosalind.info/problems/grph/

背景
  图论以图为研究对象，图是由若干给定的点及连接两点的线所构成的图形，这种图形通常用来描述某些事物之间的某种特定关系，用点代表事物，用连接两点的线表示相应两个事物间具有这种关系。
一个图是一个有序的二元组<V，E>，记作G，其中：
(1) V = {v1, v2, ..., vn}是有限非空集合，称为顶点集，其元素称为顶点或结点。
(2) E = {e1, e2, ..., em}是有限集合，称为边集，E中每个元素都有V中的结点对与之对应，称为边。
        边e既可以是有向的，也可以是无向的。有向边与有序结点对<u,v>对应，这时称u为e的起点，v为e的终点。无向边与无序结点对<u,v>对应，u，v称为e的两个端点。
当一个图的所有顶点都有名称时，可以用邻接表（adjacency list）的方式表示该图，邻接表每一行是两个顶点的名称，通过一个边连接在一起。

对重叠图（overlap graph）来说，Ok（k是正整数）代表被有向边连接的两个字符串（即顶点）s和t，s串最后k个字符与t串开头k个字符相同，且t和s不相等。
重叠图的思路常被应用在在基因组组装中
测序时，我们得到的测序数据相较于整个基因组而言是极小的；
我们的任务是将这些小片段连接起来；序列之间的联系因为重复序列的存在变得非常复杂，通过overlap最终都会构建Graph，各种相关算法会从Graph中得到最优路径，从而得到最初的contig。 
作者：未琢 https://www.bilibili.com/read/cv2023521/?from=readlist 出处：bilibili

思路:
目的：判断具有重叠区域的序列，设定大于3个碱基(也可以自己设定标准)重叠为具有overlap的序列
首先判断重叠区域：
取出前三个碱基依次和其他序列的后三个碱基比较
"""
import re
import copy

class Overlap:
    @staticmethod
    def get_fasta(fatsa,overlap_size):
        seq_name_lst = []
        sequence_lst = []
        #读取序列名构建字典的key
        for line in open(fatsa):
            if re.search(r'^>',line) != None:
                seq_name_lst.append(line.strip().strip(">"))
            else:
                sequence_lst.append(line.strip()[0:overlap_size] + line.strip()[-overlap_size:])

    #得到开始和结尾序列的列表
        start_seq = []
        end_seq = []
        for i in sequence_lst:
            start_seq.append(i[0:overlap_size])
            end_seq.append(i[-overlap_size:])
        
        return [seq_name_lst,start_seq,end_seq]

    def __init__(self,fatsa,overlap_size):
        self.overlap_size = 3
        self.__result = Overlap.get_fasta(fatsa,overlap_size = self.overlap_size)
        self.seq_s =  self.__result[1]
        self.seq_e =  self.__result[2]
        self.seq_name = self.__result[0]
    

    def get_overlap_graph(self):
        for i in range(len(self.seq_e)):
            for j in range(len(self.seq_s)):
                #https://www.cnblogs.com/blogofzxf/p/10896191.html
                #copy.deepcopy()
                end = copy.deepcopy(self.seq_s)
                end[i] = ""
                if self.seq_e[i] == end[j]:
                    print(self.seq_name[i],self.seq_name[j])



if __name__ == '__main__':
    test = Overlap(fatsa=".//data//08.test_file.txt",overlap_size=3)
    test.get_overlap_graph()

##--------------output---------------##
"""
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
"""
