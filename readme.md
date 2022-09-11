# Algorithm Course

## Algorithmic Toolbox

test locally to see the error (W1)

stress test, no one right solution gives two different answer (W1)

### Week 1

**intro.**

```py
import sys

for line in sys.stdin:
  tokens = line.split()
  a = int(tokens[0])
  b = int(tokens[1])
  print(a+b)

input = sys.stdin.readline()
# input = input()
tokens = input.split()
a = int(tokens[0])
b = int(tokens[1])
print(a+b)
```

**Maximum Pairwise Product:**

first attempt, to mush time

```py
import sys


def MaxPairWiseProduct(arr):
    result = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i]*arr[j] > result):
                result = arr[i]*arr[j]
    return result


def main():
    n = sys.stdin.readline()
    arr = sys.stdin.readline()
    result = MaxPairWiseProduct(list(map(int, arr.split())))
    print(result)


if __name__ == '__main__':
    main()
```

better

```py
import sys


def MaxPairWiseProduct(arr):
    m1 = -1
    m2 = -1
    # must type the -1 condition first
    for i in range(len(arr)):
        if (m1 == -1) or (arr[i] > arr[m1]):
            m1 = i

    for i in range(len(arr)):
        if ((m2 == -1) or (arr[i] > arr[m2])) and (i != m1):
            m2 = i
    print(f"\n{m1}, {m2}")
    return arr[m1]*arr[m2]


def main():
    n = sys.stdin.readline()
    arr = sys.stdin.readline()
    result = MaxPairWiseProduct(list(map(int, arr.split())))
    print(result)


if __name__ == '__main__':
    main()
```

with the stress test

```py
import sys
from random import randint


def MaxPairWiseProduct(arr):
    result = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i]*arr[j] > result):
                result = arr[i]*arr[j]
    return result


def MaxPairWiseProductFast(arr):
    m1 = -1
    m2 = -1
    # must type the -1 condition first
    for i in range(len(arr)):
        if (m1 == -1) or (arr[i] > arr[m1]):
            m1 = i

    for i in range(len(arr)):
        if ((m2 == -1) or (arr[i] > arr[m2])) and (i != m1):
            m2 = i
    print(f"\n{m1}, {m2}")
    return arr[m1]*arr[m2]


def main():
    while True:
        value = randint(2, 10)
        print(value)
        a = []
        for i in range(value):
            a.append(randint(0, 10))

        for i in a:
            print(str(i), end=" ")

        res1 = MaxPairWiseProduct(a)
        res2 = MaxPairWiseProductFast(a)
        if res1 != res2:
            print(f"\nWrong answer: {res1} {res2}")
            break
        else:
            print("\nok")

    n = sys.stdin.readline()
    arr = sys.stdin.readline()
    result = MaxPairWiseProduct(list(map(int, arr.split())))
    print(result)


if __name__ == '__main__':

    main()
```
