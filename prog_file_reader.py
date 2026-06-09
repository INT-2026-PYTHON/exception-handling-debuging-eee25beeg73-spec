f=input("enter name of file")
x=int(input("enter the number of data:"))
s=[]
t=()
for i in range(x):
    c=input("enter the data:")
    s.append(c)
f=s
def read_number(path):
    try:
        l=[]
        for i in path:
            c=float(i)
            l.append(c)
    except FileNotFoundError:
        print("file path is wrong")
        return ('error',f"file not found:{path}",0)
    except PermissionError:
        print("file cannot be read")
        return ('error','file cannot be read',0)
    except ValueError:
        print("a line not number")
        return ('error','invalid number on a line',0)
    except Exception as e:
        return ('error',e,0)
    else:
        sum=0
        n=0
        for i in l:
            sum += i
            n +=1
        t=('ok',sum,n)
        print(t)
    finally:
        print("done reading")
print(read_number(f))
        