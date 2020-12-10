def avgScore(student):
    result = sum(student_marks[student]) / 3
    return '%.2f' % result

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(avgScore(query_name))
