# coding:utf-8
#
import numpy as np

def heapify(arr,i,al):
    left=2*i+1
    right=2*i+2
    vmax=i
    print(left,right,al)
    if left<al and arr[left]>arr[vmax]:
        vmax=left
    if right<al and arr[right]>arr[vmax]:
        vmax=right
    if vmax!=i:
        arr[i],arr[vmax]=arr[vmax],arr[i]
        heapify(arr,vmax,al)

def max_heap(arr):
    al=len(arr)
    for i in range(al//2,-1,-1):
        heapify(arr,i,al)


def heap_sort(arr):
    al=len(arr)
    max_heap(arr)
    for i in range(al-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,0,i)
    return arr

def test():
    unsorted_list=np.random.randint(0,100,7)
    print(unsorted_list)
    sorted_list=heap_sort(unsorted_list)
    print(sorted_list)

test()
