def selectionSort(arr):
    
    for i in range(len(arr)):
        min = i
        yield arr , arr[min]
        
        for j in range (i+1,len(arr)):
            if( arr[j] < arr[min]): min = j
        
        arr[i] , arr[min] = arr[min] , arr[i]
        
        yield arr , arr[i]

def main():
    
    gen = selectionSort([10,4,3,7,6,3,2,1,0])
    for i in gen :
        print(i)
    

main()