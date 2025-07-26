def bubbleSort(arr):
    change = 0 
    for i in range(len(arr)):

        for j in range(len(arr)-1):

            yield arr , j , j+1
        
            if(arr[j] > arr[j+1]):
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                change += 1 
            
            yield arr, j,j+1

        if (change == 0) : break 
        change = 0
def main():
    arr = [10,4,3,7,6,3,2,1,0]
    gen = bubbleSort(arr)
    for it in gen :
        print(it)
main()