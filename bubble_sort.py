# coding:utf-8

import numpy as np

def bubble_sort(unsorted_list,reverse=False):
    ll=len(unsorted_list)
    for i in range(ll):
        for j in range(ll-i-1):
            if reverse:
                if unsorted_list[j]<unsorted_list[j+1]:
                    unsorted_list[j],unsorted_list[j+1]=unsorted_list[j+1],unsorted_list[j]
            else:
                if unsorted_list[j]>unsorted_list[j+1]:
                    unsorted_list[j],unsorted_list[j+1]=unsorted_list[j+1],unsorted_list[j]
    return unsorted_list

def test():
    unsorted_list=np.random.randint(0,100,20)
    print("Unsorted list:",unsorted_list)
    sorted_list=bubble_sort(unsorted_list)
    print("Ascending bubble sorted list:",sorted_list)
    sorted_list=bubble_sort(unsorted_list,True)
    print("Descending bubble sorted list:",sorted_list)

if __name__ == "__main__":
    test()
