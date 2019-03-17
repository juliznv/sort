# coding:utf-8
import numpy as np

def merge_sort(unsorted_list,reverse=False):
    ll=len(unsorted_list)
    if ll<2:
        return unsorted_list
    return merge(merge_sort(unsorted_list[:ll//2]),merge_sort(unsorted_list[ll//2:]))

def merge(left,right):
    sorted_list=[]
    i=0
    j=0
    while i<len(left) or j<len(right):
        if i>=len(left):
            sorted_list.append(right[j])
            j=j+1
        elif j>=len(right):
            sorted_list.append(left[i])
            i=i+1
        elif left[i]<right[j]:
            sorted_list.append(left[i])
            i=i+1
        else:
            sorted_list.append(right[j])
            j=j+1
    return sorted_list

def test():
    unsorted_list=np.random.randint(0,100,8)
    print(unsorted_list)
    sorted_list=merge_sort(unsorted_list)
    print(np.array(sorted_list))

if __name__ == "__main__":
    test()