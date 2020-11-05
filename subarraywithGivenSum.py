
#Complete this function
def subArraySum(arr, n, sum): 
    #Your code here
    curr_sum=0
    j=0
    for i in range(n):
        curr_sum += arr[i]
        while curr_sum > sum:
            curr_sum -= arr[j]
            j += 1
        if curr_sum == sum:
            print (" ".join([str(j+1),str(i+1)]),end="")
            break
    if curr_sum != sum:
        print (-1,end="")


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            
            subArraySum(A, N, S)
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends