# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 16:32:28 2021

@author: liuzihao
URL: http://rosalind.info/problems/lcsm/
在06 确定DNA子序列出现的位置中，我们练习了从DNA序列中寻找给定子序列位置的方法，但是在实际应用中，我们并不能提前知道哪些是有意义的模序，需要通过比较多条序列以找到公共序列。

本题假设模序不发生突变，我们需要在一组DNA序列中找到每个序列共有的最长子序列
目的寻找一组序列中的最长的公共序列
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
----output-----
AC
思路: 共有最长序列的长度，一定不会超过所给序列的最短的序列，所以按以下步骤实现
1, 读入序列，读入后将最短的序列取出
2, 按不同的kmer拆分序列，从k-mer=序列长度 开始拆分（减少计算量），N-K+1 
3, 使用拆分后的kmer序列去匹配其他序列，该k-mer在其他序列中只要出现一次，那么这条k-mer计为True 如果该k-mer完全为True，则将其加入候选共有序列
4, 统计候选序列长度，取出最长序列，如果多个，一并取出，(本例子直接要的最长的,长度一致则全部返回)
5, 如果所有序列一样长，那么将第一条序列最为参考序列
6, 扩展一下可以写一个批量通过overlap拼接序列的脚本挖个坑
"""
import logging
from functools import wraps
import time
from datetime import timedelta

class Share_Motif:
    #得到序列分为参考序列(最短)与待比序列
    @staticmethod
    def get_sequence(fasta):
        tmp_length_lst = []
        sequence = []
        for seq in open(fasta):
            if seq.startswith(">") == False:
                sequence.append(seq.strip())
                tmp_length_lst.append(len(seq))
        #得到最短序列的index, 最短序列有多条时候，默认选择第一条
        inx = tmp_length_lst.index(min(tmp_length_lst))
        if len(str(inx)) > 1 :
            ref = sequence[eval(inx)][0]
        else:
            ref = sequence[inx]
        sequence.remove(ref)
        return (ref,sequence)
    
    #用于获得k-mer的函数
    @staticmethod
    def kmer_get(seq,k_mer):
        k_mer_seq = []
        for nu_seq in range(len(seq) - k_mer + 1):
            k_seq = seq[nu_seq:nu_seq + k_mer]
            if k_seq in k_mer_seq:
                continue
            else:
               k_mer_seq.append(k_seq) 
        return k_mer_seq

    def __init__(self,fasta):
        self.__result = Share_Motif.get_sequence(fasta)
        self.ref = self.__result[0]
        self.sequence = self.__result[1]
    
    def get_sahre(self):
        share = []
        k_szie = list(range(2,len(self.ref) + 1))
        k_szie.reverse()
        for k in k_szie:
            if len(share) != 0:
                break  
            else:
                k_lst =Share_Motif.kmer_get(seq=self.ref,k_mer=k)
                for j in k_lst:
                    lst = []
                    for i in self.sequence:
                        #Y mean k-mer sequence in sequence N: k-mer not in
                        lst.append("Y") if j in i  else lst.append("N")  
                    if set(lst) == {"Y"}:
                        share.append(j)
        return share

#test
def add_log(func):
    '''
    logging start and done.
    '''
    #设定输出格式
    logFormatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    module = func.__module__#类定义所在的模块名称
    name = func.__name__#函数名称
    logger_name = f'{module}.{name}'#日志名
    logger = logging.getLogger(logger_name)#创建一个log
    #设定日志输出级别
    logger.setLevel(logging.INFO)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    logger.addHandler(consoleHandler)

    @wraps(func)
    def wrapper(*args, **kwargs):
        if args and hasattr(args[0], 'debug') and args[0].debug:
            logger.setLevel(10)  # debug

        logger.info('start...')
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        used = timedelta(seconds=end - start)
        logger.info('done. time used: %s', used)
        return result

    wrapper.logger = logger
    return wrapper

@add_log
def main(fasta):
    test = Share_Motif(fasta)
    print(test.get_sahre())


if __name__=='__main__':
    main(fasta = ".//data//10.test_file.txt")
    

##--------output--------##
"""
['TA', 'AC', 'CA']
"""