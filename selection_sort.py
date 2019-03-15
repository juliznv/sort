# coding:utf-8
import time
import numpy as np

def selection_sort(unsorted_list,reverse=False):
    for i in range(len(unsorted_list)):
        for j in range(i+1,len(unsorted_list)):
            if reverse:
                if unsorted_list[i]<unsorted_list[j]:
                    unsorted_list[i],unsorted_list[j]=unsorted_list[j],unsorted_list[i]
            else:
                if unsorted_list[i]>unsorted_list[j]:
                    unsorted_list[i],unsorted_list[j]=unsorted_list[j],unsorted_list[i]

    return unsorted_list

def test():
    unsorted_list=np.random.randint(0,100,20)
    print("unsorted list:",unsorted_list)
    sorted_list=selection_sort(unsorted_list)
    print("Ascending selection sorted list:",sorted_list)
    sorted_list=selection_sort(unsorted_list,True)
    print("Descending selection sorted list:",sorted_list)


'''
if __name__ == "__main__":
    test()
'''