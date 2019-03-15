# coding:utf-8
import time
import numpy as np

def insertion_sort(unsorted_list,reverse=False):
    for i in range(1,len(unsorted_list)):
        val=unsorted_list[i]
        j=i-1
        if reverse:
            while j>-1 and unsorted_list[j]<val:
                unsorted_list[j+1]=unsorted_list[j]
                j=j-1
            unsorted_list[j+1]=val
        else:
            while j>-1 and unsorted_list[j]>val:
                unsorted_list[j+1]=unsorted_list[j]
                j=j-1
            unsorted_list[j+1]=val
    return unsorted_list


def test():
    unsorted_list=np.random.randint(0,100,10)
    print("Unsorted list:",unsorted_list)
    start = time.clock()
    sorted_lsit=insertion_sort(unsorted_list)
    end=time.clock()
    print("Ascending insertion sorted list:",sorted_lsit)
    print("Running time:%ss"%(end-start))
    start = time.clock()
    sorted_lsit=insertion_sort(unsorted_list,True)
    end = time.clock()
    print("Descending insertion sorted list:",sorted_lsit)
    print("Running time:%ss"%(end-start))
'''
if __name__ == "__main__":
    start = time.clock()
    test()
'''