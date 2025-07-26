def mergeSort(arr):
    if(len(arr) <= 1): return arr 
    
    mid = int(len(arr)/2) 
    return merge( mergeSort(arr[:mid:]) , mergeSort(arr[mid::]))


def merge( left , right):
    arr = [] 
    l_count = 0 
    r_count = 0 

    while(l_count < len(left) and r_count < len(right)):
        if(left[l_count] < right[r_count]):
            arr.append(left[l_count])
            l_count += 1 
            continue 
        
        arr.append(right[r_count])
        r_count += 1 

    if(l_count >= len(left)) :
       
        left = right 
        l_count = r_count
    
    while(l_count < len(left)):
       
        arr.append(left[l_count])
        l_count += 1 
    
    return arr 


def main():
    
    arr = [5, 4, 3, 2, 1]

    print(mergeSort(arr))

main()

        