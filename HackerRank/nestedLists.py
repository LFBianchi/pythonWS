def secondWorst(arr):
    grades = {}
    for i in arr:
        grades[i[0]] = i[1]
    arr = sorted(list(set(grades.values())))
    ans = [i for i in grades if grades[i] == arr[1]]
    return sorted(ans)

if __name__ == '__main__':
    
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
        
    for i in secondWorst(arr):
        print(i)
