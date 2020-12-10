def runnerUp(arr):
    return sorted(list(set(arr)))[-2]

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    print(runnerUp(arr))
