import sys

def sumWithFor(n):
    total = 0
    i = 0
    for i in range(n + 1):
        total += i
    return total

def sumWithWhile(n):
    total = 0
    i = 0
    while i <= n:
        total += i
        i+= 1
    return total
        

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write("Provide n as a command line argument.")
        exit()
    n = int(sys.argv[1])
    withSum = sumWithWhile(n)
    print(withSum)
    forSum = sumWithFor(n)
    print(forSum)
