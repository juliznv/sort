# coding:utf-8
import numpy as np
import copy
import time
import sort

def generate_data(n):
    data=[]
    while len(data)!=n:
        tmp=np.random.randint(0,n)
        if tmp not in data:
            data.append(tmp)
    return data

def test(n):
    data=generate_data(n)
    datas=[]
    correct=generate_data(20)
    corrects=[]
    for i in range(7):
        datas.append(copy.deepcopy(data))
        corrects.append(copy.deepcopy(correct))
    print("正确检测:")
    print("原始数据:",correct)
    sort.bubble_sort(corrects[0])
    sort.insertion_sort(corrects[1])
    sort.selection_sort(corrects[2])
    sort.quick_sort(corrects[3],0,19)
    result=sort.merge_sort(corrects[4])
    sort.shell_sort(corrects[5],2)
    sort.heap_sort(corrects[6])
    print("冒泡排序:",corrects[0])
    print("插入排序:",corrects[1])
    print("选择排序:",corrects[2])
    print("快速排序:",corrects[3])
    print("归并排序:",result)
    print("希尔排序:",corrects[5])
    print("堆排序:",corrects[6])

    print()
    print("计算时间检测:")

    start=time.clock()
    sort.bubble_sort(datas[0])
    end=time.clock()
    print("冒泡排序运行时间:",end-start)

    start=time.clock()
    sort.insertion_sort(datas[1])
    end=time.clock()
    print("插入排序运行时间:",end-start)

    start=time.clock()
    sort.selection_sort(datas[2])
    end=time.clock()
    print("选择排序运行时间:",end-start)

    start=time.clock()
    sort.quick_sort(datas[3],0,len(datas[3])-1)
    end=time.clock()
    print("快速排序运行时间:",end-start)

    start=time.clock()
    sort.merge_sort(datas[4])
    end=time.clock()
    print("归并排序运行时间:",end-start)

    start=time.clock()
    sort.shell_sort(datas[5],2)
    end=time.clock()
    print("希尔排序运行时间:",end-start)

    start=time.clock()
    sort.heap_sort(datas[6])
    end=time.clock()
    print("堆排序运行时间:",end-start)
    
if __name__ == "__main__":
    test(10000)