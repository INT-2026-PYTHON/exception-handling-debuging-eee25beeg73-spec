n=int(input("enter the number of elemnets:"))
l=[]
for i in range(n):
    x=int(input("enter the element:"))
    l.append(x)
def safe_get(items, index):
    for i in range(len(items)):
        try:
            return ('ok',items[index])
        except IndexError:
            return ('error','index out of range')
        except TypeError:
            return ('error','index must be int')
        except Exception as e:
            return('error',e)
r=int(input("enter the index:"))
s=safe_get(l,r)
print(s)        
