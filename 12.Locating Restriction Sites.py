#- * - UTF-8 - * -#
"""
确定限制酶酶切位点
所给：一条长度不超过1kb的DNA序列
需得：这条序列上长度在4-12nt间的回文序列的位置和长度，以任意顺序输出
限制性核酸内切酶是可以识别并附着特定的脱氧核苷酸序列，并在每条链中特定部位的两个脱氧核糖核苷酸之间的磷酸二酯键进行切割的一类酶，简称限制酶。
限制酶识别DNA序列中的回文序列，回文序列是一种旋转对称结构，在轴的两侧序列相同而反向，特点是在该段的碱基序列的互补链之间正读反读都相同。
限制酶的生理作用是限制酶降解外源DNA，维护宿主遗传稳定的保护机制。限制酶在几乎所有细菌的种、属中都有发现，是细菌防御噬菌体侵染的机制。 

思路：
给定序列与反向互补序列中相同的部分就是限制酶酶切位点,同时还要考虑到序列相对的位置是一致的，
"""
BASE = {"A":"t",
        "T":"a",
        "G":"c",
        "C":"g"}

class Restriction:
    @staticmethod
    def get_fasta(fasta):
        with open(fasta) as fd:
            seq = [seq.strip() for seq in fd.readlines() if seq.startswith(">") == False][0]
        seq_r = seq[::-1]
        for base in BASE.keys():
            seq_r = seq_r.replace(base,BASE[base])
        return seq,seq_r.upper()
    
    @staticmethod
    def get_kmer(k_len,seq):
        k_num  = len(seq) - k_len + 1
        k_lst = [seq[k:k + k_len] for k in range(k_num)]
        return enumerate(k_lst)
    
    def __init__(self,fasta,min_nt,max_nt):
        self.seq = Restriction.get_fasta(fasta)[0]
        self.seq_r = Restriction.get_fasta(fasta)[1]
        self._min_nt = min_nt
        self._max_nt = max_nt
        self.k_len = [k_len for k_len in range(self._min_nt,self._max_nt + 1) if k_len %2 == 0]

    def get_restriction(self):
        with open(".//result//12.result.txt","w") as fd:
            fd.write(f"start\tlength(bp)\tsequence\n")
            for nt in self.k_len:
                for index_seq,k_seq in Restriction.get_kmer(k_len = nt,seq = self.seq):
                    for index_seq_r,k_seq_r in Restriction.get_kmer(k_len = nt,seq = self.seq_r):
                        if k_seq == k_seq_r and -(index_seq + len(k_seq)) == (index_seq_r - len(self.seq_r)):
                            fd.write(f"{index_seq + 1}\t{len(k_seq)}\t{k_seq}\n")
                            
                

def main():
    a1 = Restriction(fasta = ".//data//12.test_file.txt",min_nt = 4,max_nt = 12)
    a1.get_restriction()

if __name__ == '__main__':
    main()

