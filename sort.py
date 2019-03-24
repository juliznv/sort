# coding:utf-8

import numpy as np


# 顺序标识符
# asc(Ascending)升序
# desc(Descending)降序
asc=True
desc=False

#seq接受升序/降序标识符

# 冒泡排序
def bubble_sort(unsorted,seq=asc):
    length=len(unsorted)
    for i in range(length):
        for j in range(length-i-1):
            if seq and unsorted[j]>unsorted[j+1]:
                unsorted[j],unsorted[j+1]=unsorted[j+1],unsorted[j]
            elif not seq and unsorted[j]<unsorted[j+1]:
                unsorted[j],unsorted[j+1]=unsorted[j+1],unsorted[j]

# 插入排序
def insertion_sort(unsorted,seq=asc):
    length=len(unsorted)
    for i in range(1,length):
        key=unsorted[i]
        j=i-1
        if seq:
            while j>=0 and unsorted[j]>key:
                unsorted[j+1]=unsorted[j]
                j-=1
            unsorted[j+1]=key
        else:
            while j>=0 and unsorted[j]<key:
                unsorted[j+1]=unsorted[j]
                j-=1
            unsorted[j+1]=key

# 选择排序
def selection_sort(unsorted,seq=asc):
    length=len(unsorted)
    for i in range(length):
        for j in range(i+1,length):
            if seq and unsorted[i]>unsorted[j]:
                unsorted[i],unsorted[j]=unsorted[j],unsorted[i]
            elif not seq and unsorted[i]<unsorted[j]:
                unsorted[i],unsorted[j]=unsorted[j],unsorted[i]

# 快速排序
def quick_sort(unsorted,left,right,seq=asc):
    if left>right:
        return
    i=left
    j=right
    key=unsorted[i]
    while i<j:
        if seq:
            while i<j and unsorted[j]>key:
                j-=1
            if i<j:
                unsorted[i],unsorted[j]=unsorted[j],unsorted[i]
            while i<j and unsorted[i]<key:
                i+=1
            if i<j:
                unsorted[i],unsorted[j]=unsorted[j],unsorted[i]
        else:
            while i<j and unsorted[j]<key:
                j-=1
            if i<j:
                unsorted[i],unsorted[j]=unsorted[j],unsorted[i]
            while i<j and unsorted[i]>key:
                i+=1
            if i<j:
                unsorted[i],unsorted[j]=unsorted[j],unsorted[i]
    unsorted[i]=key
    quick_sort(unsorted,left,i-1,seq)
    quick_sort(unsorted,i+1,right,seq)

# 归并排序
def merge_sort(unsorted,seq=asc):
    length=len(unsorted)
    if length<2:
        return unsorted
    return merge(merge_sort(unsorted[:length//2],seq),merge_sort(unsorted[length//2:],seq),seq)
# 归并结合函数
def merge(l,r,seq):
    _sorted=[]
    i=j=0
    while i<len(l) and j<len(r):
        if (seq and l[i]>r[j]) or (not seq and l[i]<r[j]):
            _sorted.append(r[j])
            j+=1
        else:
            _sorted.append(l[i])
            i+=1
    return _sorted+l[i:]+r[j:]

# 希尔排序
def shell_sort(unsorted,n,seq=asc):
    length=len(unsorted)
    l=length
    while l//n>0:
        l=l//n
        for i in range(l,length):
            c=i
            cv=unsorted[i]
            if seq:
                while c>=l and cv<unsorted[c-l]:
                    unsorted[c]=unsorted[c-l]
                    c=c-l
            else:
                while c>=l and cv>unsorted[c-l]:
                    unsorted[c]=unsorted[c-l]
                    c=c-l
            unsorted[c]=cv
            
# 堆排序
def heap_sort(unsorted,seq=asc):
    length=len(unsorted)
    if seq:
        heap(unsorted,True)
        for i in range(length-1,0,-1):
            unsorted[0],unsorted[i]=unsorted[i],unsorted[0]
            heapify(unsorted,0,i,True)
    else:
        heap(unsorted,False)
        for i in range(length-1,0,-1):
            unsorted[0],unsorted[i]=unsorted[i],unsorted[0]
            heapify(unsorted,0,i,False)
# 构建堆,m为最大/最小堆标识,默认为True最大
def heap(arr,m=True):
    length=len(arr)
    for i in range(length//2,-1,-1):
        heapify(arr,i,length,m)
# 堆调整函数,i为检索,length为调整长度,m为标识
def heapify(arr,i,length,m=True):
    left=2*i+1
    right=2*i+2
    vm=i
    if m:
        if left<length and arr[left]>arr[vm]:
            vm=left
        if right<length and arr[right]>arr[vm]:
            vm=right
    else:
        if left<length and arr[left]<arr[vm]:
            vm=left
        if right<length and arr[right]<arr[vm]:
            vm=right
    if vm!=i:
        arr[i],arr[vm]=arr[vm],arr[i]
        heapify(arr,vm,length,m)