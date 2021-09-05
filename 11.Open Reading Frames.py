#- * - UTF-8 - * -#
"""
搜索给定序列中所有可能的开放阅读框(ORF)
开放阅读框:是DNA序列中具有编码蛋白质潜能的序列，结束于终止密码子连续的碱基序列,结构基因的正常核苷酸序列，从起始密码子到终止密码子的阅读框可编码完整的多肽链，其间不存在使翻译中断的终止密码子
在mRNA序列中，每三个连续碱基(即三联“ 密码子”） 编码相应的氨基酸。其中有一个起始密码子AUG和三个终止密码子UAA，UAG，UGA。核糖体从起始密码子开始翻译，
沿着mRNA序列合成多肽链并不断延伸，遇到终止密码子时，多肽链的延伸反应终止。由于读写位置不同，ORF有六种可能性。(正反各三种)
起始密码子: ATG >> AUG
终止密码子: TAA >> UAA
            TAG >> TUG
            TGA >> UGA
思路:
1 首先得到两条链 给定的链和反向互补
2 分别按照不同的阅读方式拆分
3 匹配密码子，终止密码子用*替代，最后使用正则取匹配
"""
import re
import logging


CONDON_TABLE = {'GCU':'A', 'GCC':'A', 'GCA':'A', 
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
                'UGG':'W','UAG':'*', 'UGA':'*', 
                'UAA':'*'}
BASE_TABLE = {"A":"t",
              "T":"a",
              "G":"c",
              "C":"g"}
class Orf:
    @staticmethod
    def get_seq(fasta):
        with open(fasta) as fsa:
            seq_lst = [seq.strip() for seq in fsa.readlines() if seq.startswith(">") == False ]
        seq_lst = " ".join(seq_lst)
        #得到反向互补序列
        seq_res = seq_lst[::-1]
        for base in ["A","T","G","C"]:
           seq_res = seq_res.replace(base,BASE_TABLE[base])
        return seq_lst,seq_res.upper()
    
    def __init__(self,fasta):
        self._result = Orf.get_seq(fasta)
        self.seq = self._result[0].replace("T","U")
        self.seq_r = self._result[1].replace("T","U")
        self.lst = []
        self.lst_r = []
        
        for i in range(0,4):
            self.lst.append(re.findall(r".{3}",self.seq[i:]))
            self.lst_r.append(re.findall(r".{3}",self.seq_r[i:]))
       
        for i in range(len(self.lst)):
            for j in range(len(self.lst[i])):
                self.lst[i][j] = CONDON_TABLE[self.lst[i][j]]
                self.lst_r[i][j] = CONDON_TABLE[self.lst_r[i][j]]
        
        self.pro = ["".join(pro) for pro in self.lst]
        self.pro_r = ["".join(pro) for pro in self.lst_r]
    
    def get_orf(self):
        orf_seq = []
        for ano in  self.pro:
            orf = re.findall(r"M[A-Z]{0,}\*{1}",ano)
            orf_seq.append(orf)
        
        for ano_r in  self.pro_r:
            orf_r = re.findall(r"M[A-Z]{0,}\*{1}",ano_r)
            orf_seq.append(orf_r)
        return orf_seq


    
def main():
    a = Orf(fasta=".//data//11.test_file.txt")
    orf = []
    for seq in a.get_orf():
        seq = "".join(seq)
        if seq == '':
            continue
        else:
           orf.append(seq.strip("*"))
    for s in set(orf):
        print(s)

if __name__ == "__main__":
    main()

"""
有一条不知道怎么输出，以后在解决吧 MTPRLGLESLLE 不知道怎么用正则从MGMTPRLGLESLLE提取出来....
"""





