first=input()
second=input()
first_len=len(first)
second_len=len(second)
d=-1

def location(a,b):
    for i in range(first_len):
        if first[i] ==second[0]:
            if first[i+1]==second[1]:
                return i
    d=i
        


k=location(first,second)

print(k)