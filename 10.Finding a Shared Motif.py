# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 16:32:28 2021

@author: liuzihao

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
"""

