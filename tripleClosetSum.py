
# arr    : list of integers denoting the elements of the array
# target : as specified in the problem statement
import sys
def threeSumClosest (arr, target):
    i=0
    j=2
    arr.sort()
    sum1=0
    close=sys.maxsize
    for i in range(len(arr)-2):
        j=i+1
        k=len(arr)-1
        sum1=0
        while (j<k):
            sum1=arr[i]+arr[j]+arr[k]
            if(abs(target-sum1)<abs(target-close)):
                close=sum1
            elif(abs(target-sum1)==abs(target-close)):
                if sum1>target:
                    close=sum1    
            if target>sum1:
                j+=1
            else:
                k-=1
               
    return(close)            
            
        
    





t = int (input ())
for tc in range (t):
    n, target = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    
    print (threeSumClosest (arr, target))
    

