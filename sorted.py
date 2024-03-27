pos = -1

def search(list, target):
    global pos
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l + u) // 2

        if list[mid] == target:
            pos = mid
            return True
        
        elif list[mid] < target:
            l = mid 

        else:
            u = mid 

    return False

list = [4, 7, 8, 12, 13]
target = 7

if search(list, target):
    print("Found at", pos )
    
else:
    print("Not found")
