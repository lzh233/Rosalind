#- * - UTF-8 - * -#
"""
RNA剪切:
RNA剪接（RNA splicing）是指从DNA模板链转录出的最初转录产物中除去内含子，并将外显子连接起来形成一个连续的RNA分子的过程。
本题提供了fasta文件: 其中第一条序列是完整的DNA序列，后面的为内含子序列，
本题的思路是使用for和while删除内含子序列，配合while是因为python只会匹配到第一个符合条件的字符串
"""
import re
PROTEIN = {'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A', 'CGU':'R', 'CGC':'R',
                  'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R', 'UCU':'S', 'UCC':'S',
                  'UCA':'S', 'UCG':'S', 'AGU':'S', 'AGC':'S', 'AUU':'I', 'AUC':'I',
                  'AUA':'I', 'UUA':'L', 'UUG':'L', 'CUU':'L', 'CUC':'L', 'CUA':'L',
                  'CUG':'L', 'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G', 'GUU':'V',
                'GUC':'V', 'GUA':'V', 'GUG':'V', 'ACU':'T', 'ACC':'T', 'ACA':'T',
                'ACG':'T', 'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 'AAU':'N',
                'AAC':'N', 'GAU':'D', 'GAC':'D', 'UGU':'C', 'UGC':'C', 'CAA':'Q',
                'CAG':'Q', 'GAA':'E', 'GAG':'E', 'CAU':'H', 'CAC':'H', 'AAA':'K',
                'AAG':'K', 'UUU':'F', 'UUC':'F', 'UAU':'Y', 'UAC':'Y', 'AUG':'M',
                'UGG':'W','UAG':'*', 'UGA':'*', 'UAA':'*'}

class Splicing:
    @staticmethod
    def get_fasta(fasta):
        with open(fasta) as fd:
            seq_lst = [seq.strip() for seq in fd.readlines() if seq.startswith(">") == False]
        seq = seq_lst[0]
        introns = seq_lst[1:]
        return seq,introns
    
    def __init__(self,fasta):
        self.seq =  Splicing.get_fasta(fasta)[0]
        self.introns = Splicing.get_fasta(fasta)[1]
    
    def get_splicing_seq(self):
        for intr in self.introns:
            while self.seq.find(intr) != -1:
                self.seq = self.seq[0:self.seq.find(intr)] + self.seq[self.seq.find(intr) + len(intr): ]      
        #翻译(暂时不考虑起始密码子，默认给定的序列都是ATG开头)
        self.seq = self.seq.replace("T","U")
        self.seq = re.findall(r".{3}",self.seq)
        pro_seq = ""
        for seq in self.seq:
            if seq not in ['UAG', 'UGA', 'UAA']:
                pro_seq += PROTEIN[seq]
            else:
                break
        return pro_seq


def main():
    a1 = Splicing(fasta=".//data//13.test_file.txt")
    protein = a1.get_splicing_seq()
    print(protein)

if __name__ == "__main__":
    main()