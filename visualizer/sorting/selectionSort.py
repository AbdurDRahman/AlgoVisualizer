def selectionSort(arr):
    
    for i in range(len(arr)):
        min = i
        
        for j in range (i+1,len(arr)):
            if( arr[j] < arr[min]): min = j
        
        yield i ,min 
       
        arr[i] , arr[min] = arr[min] , arr[i]
        
        yield i ,min 

def main():
    
    gen = selectionSort([10,4,3,7,6,3,2,1,0])
    for i in gen :
        print(i)
    

if __name__ == "__main__":
    main()