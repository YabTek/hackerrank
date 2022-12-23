if __name__ == '__main__':
    n = int(input())
    lst = []    
    for _ in range(n):
        line = input().split()
        
        if line[0] == 'insert':
            lst.insert(int(line[1]),int(line[2]))
        if line[0] == 'append':
            lst.append(int(line[1]))
        if line[0] == 'sort':
            lst.sort()
        if line[0] == 'remove':
            lst.remove(int(line[1]))
        if line[0] == 'reverse':
            lst.reverse()
        if line[0] == 'pop':
            lst.pop()     
        if line[0] == 'print':
            print(lst)