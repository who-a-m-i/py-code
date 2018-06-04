# -*- coding: utf-8 -*-
'''
Created on 2018年4月30日

@author: LSH8880
'''
class Myseq:
    def __init__(self):
        self.lseq = ["I","II","III","IV"]
    
    def __len__(self):
        return len(self.lseq)
    
    def __getitem__(self,key):
        if 0 <= key < 4:
            return self.lseq[key]

if __name__ == '__main__':
    m = Myseq()
    for i in range(4):
        print(m[i])        
            