
def quickSort(arr , left = 0 , right = None):
    

    if(right == None): right = len(arr) - 1
    if(left >= right): return  

    partitionIndex = partition(arr , left , right)
    
    yield left , partitionIndex , right 
    
    yield from quickSort(arr , left , partitionIndex - 1)
    yield from quickSort(arr , partitionIndex + 1 , right)

    yield left , partitionIndex , right 


    


def partition(arr , left  , right ):

    pivot = arr[right]
    lesser = left 

    for i in range(left , right):
    
        if(arr[i] < pivot):
    
            arr[lesser],arr[i] = arr[i],arr[lesser]
            lesser += 1 
    
    arr[lesser] , arr[right] = arr[right] , arr[lesser]
    
    return lesser

def main():
    arr = [7,1,2,4,5,3,10,8,6]
    
    gen  = quickSort(arr)
    
    for i in gen :
    
        print(arr[i[0]:i[1]:] , arr[i[1]:i[1]+1:] , arr[i[1]+1:i[2]+1:] )
    
    print(arr)

main()