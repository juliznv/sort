# coding:utf-8
import numpy as np

def quick_sort(unsorted_list,left,right):
    if left>=right:
        return
    i=left
    j=right
    key=unsorted_list[left]
    while i<j:        
        while i<j and unsorted_list[j]>=key:
            j-=1
        if i<j:
            unsorted_list[i]=unsorted_list[j]
            i+=1
        while i<j and unsorted_list[i]<key:
            i+=1
        if i<j:
            unsorted_list[j]=unsorted_list[i]
            j-=1
    unsorted_list[i]=key
    quick_sort(unsorted_list,left,i-1)
    quick_sort(unsorted_list,i+1,right)



def test():
    unsorted_list=np.random.randint(0,100,20)
    print(unsorted_list)
    quick_sort(unsorted_list,0,19)
    print(unsorted_list)

test()