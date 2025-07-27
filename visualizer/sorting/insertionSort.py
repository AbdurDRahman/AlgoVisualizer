def insertionSort(arr):
    for i in range(1,len(arr)):

        j = i - 1  
        key = arr[i]
        
        yield j , i

        while(j >= 0  and (arr[j] > key) ):
    
            arr[j+1]  = arr[j]
            j = j - 1 
    
        arr[j+1] = key 
        yield j+1, i 

        

def main():
    gen = insertionSort([10,4,3,7,6,3,2,1,0])
    for i in gen :
        print(i)
if __name__ == "__main__":
    main()