def binary_search(array ,target , start , end ):
    if end>=start:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            return binary_search(array,target,start,mid-1)
        else:
            return binary_search(array,target,mid+1,end)
    else:
        return -1
def main():
    array=[1,8,9,25,45,89,96]
    target=96
    res= (binary_search(array,target,0,len(array)-1))
    if res!=-1:
        print(f"The {target} is present at {res}")
    else:
        print(f"The {target} is not present in the array")
main()