def mergeSort(arr):
    
    if len(arr) <= 1:
        yield arr
        return

    yield arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    yield from mergeSort(left)
    yield from mergeSort(right)

    merged = []
    l_count = r_count = 0
   
    while l_count < len(left) and r_count < len(right):
        
        if left[l_count] < right[r_count]:
        
            merged.append(left[l_count])
            l_count += 1
        
        else:
       
            merged.append(right[r_count])
            r_count += 1

    merged.extend(left[l_count:])
    merged.extend(right[r_count:])

    arr[:len(merged)] = merged

    yield arr




def main():
    
    arr = [5, 4, 3, 2, 1]
    gen = mergeSort(arr)
    for i in gen :
        print(i)

if __name__ == "__main__":
    main()
        