import sys

input = sys.stdin.readline


def isPrime(num):
    for i in range(2, int(num**(1/2))+1):
        if int(num/i)*i == num:
            return False
    return True

n = int(input())
for _ in range(n):
    num = int(input())
    if num == 0 or num == 1 or num == 2:
        print(2)
        continue
    while not isPrime(num):
        num += 1
    print(num)