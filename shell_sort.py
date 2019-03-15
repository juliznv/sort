# coding:utf-8
import numpy as np

def shell_sort(unsorted_list,reverse=False):
    ll=len(unsorted_list)
    while ll//2>0:
        ll=ll//2
        for i in range(ll,len(unsorted_list)):
            j=i
            current=unsorted_list[i]
            while j>=ll and current<=unsorted_list[j-ll]:
                unsorted_list[j]=unsorted_list[j-ll]
                j=j-ll
            unsorted_list[j]=current
    return unsorted_list

def test():
    unsorted_list=np.random.randint(0,100,23)
    print(unsorted_list)
    sorted_list=shell_sort(unsorted_list)
    print(sorted_list)

if __name__ == "__main__":
    test()