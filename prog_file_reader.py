f=input("enter name of file:")
n=[]
t=()
def read_number(path):
    try:
        f = open(path, "r")
        for i in f:
            n.append(float(i.strip()))
        print("file path is wrong")
    except FileNotFoundError:
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
        l=0
        for i in n:
            sum += i
            l+=1
        t=('ok',sum,l)
        print(t)
    finally:
        print("done reading")
print(read_number(f))
        