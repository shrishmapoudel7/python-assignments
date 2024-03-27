pos = -1

def search(list,n):
    global pos

    l=0
    u=len(list)-1

    while l<=u:
        mid=(l+u)//2

        if list[mid]==n:
            return True
        
        else:
            if list[mid]<n:
                pos=mid
                l=mid
            else:
                u=mid

list={4,7,8,12,13}
n=7
if search(list,n):
    print("found at", pos+1)
else:
    print("not found")

        
            