# -*- coding: utf-8 -*-
"""
所给：6个不超过20000的非负整数，分别对应于一个群体中在某基因位点上不同基因型组合的夫妻数目。六个整数对应的基因型分别如下：

A:AA-AA 1

B:AA-Aa 1

C:AA-aa 1

D:Aa-Aa 3/4

E:Aa-aa 1/2

aa-aa 
需得：下一代表现显性性状的期望数，假设每对夫妻只有两个后代 
作者：未琢 https://www.bilibili.com/read/cv2030564/?from=readlist 出处：bilibili
"""
def get_answer(a,b,c,d,e):
    total = a+b+c+d+e
    return (a/total*1 + b/total*1 + c/total*1 + d/total*0.75 + e/total*0.5)*2*total
#test
test = get_answer(1,0,0,1,0)
print(test)