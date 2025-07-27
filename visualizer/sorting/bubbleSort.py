def bubbleSort(arr):
    change = 0 
    for i in range(len(arr)):

        for j in range(len(arr)-1):
        
            if(arr[j] > arr[j+1]):
                yield j , j+1 , i
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                yield j , j+1 , i
                change += 1 
            
        if (change == 0) : break 
        change = 0

def main():
    arr = [10,4,3,7,6,3,2,1,0]
    gen = bubbleSort(arr)
    for it in gen :
        print(it)
if __name__ == "__main__":
    main()