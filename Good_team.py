''' 
Good Team

you are given n people of different skill values. you have to build a team of k people. 
team goodness is decided by the difference between the maximum skill value and the minimum skill value. you want to form a team such that the difference between the maximum skill value and the minimum skill value is minimum. you have 
to tell what is the difference between the maximum skill value and the minimum skill value of that
'''
def minDiff(arr,n,k):
    result = +2147483647
    arr.sort()
    for i in range(n-k+1):
        result = int(min(result, arr[i+k-1] - arr[i]))
    return result
p=int(input())
for i in range(0,p):
    x = list(map(int, input().split()))
    n,k=x[0],x[1]
    arr = list(map(int, input().split()))
    print(minDiff(arr, n, k))