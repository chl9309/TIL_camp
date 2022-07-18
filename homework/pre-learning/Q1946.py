t = int(input())
i = int(input())
k = 10
print('#',t)
for a in range(1, i+1):
    
    x, y = input().split()
    y = int(y)
    while y > 0:
        if k!=0:
            print(x,end='')
            y -= 1
            k -= 1
        else:
            print(end='\n')
            k=10