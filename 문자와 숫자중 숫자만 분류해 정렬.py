import re

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

if __name__ == "__main__":
    Munja=["A37B","23CC","88D9","BB8F","3A9A"]#정렬한 문자열
    number=[]

    for i in range(0,len(Munja)):
        number=re.findall(r'\d+',Munja[i])
    
    print(number)
