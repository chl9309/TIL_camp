a = int(input())

for i in range(1, a+1):
    
    x = input()
    y = x[::-1]
    
    if x == y :
        print ('#',i,' ',1)
        
    else:
        print ('#',i,' ',0)
