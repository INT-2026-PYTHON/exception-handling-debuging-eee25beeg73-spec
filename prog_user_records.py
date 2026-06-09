l=[
   {"name": "Alice", "age": "25",   "score": "88.5"},
   {"name": "Bob",   "age": "abc",  "score": "70"},
   {"name": "Carol", "age": "30"},                       # missing "score"
   "not a dict",                                          # wrong type
   {"name": "Dan",   "age": "40",   "score": "55.5"},
]
def process_records(records):
    c=[]
    er=[]
    for i in range(len(records)):
        try:
            rec=records[i]
            name=rec['name']
            score=float(rec['score'])
            age=int(rec['age'])
        except (KeyError,TypeError,ValueError) as e:
            er.append((i,type(e).__name__,str(e)))
        else:
            c.append({"name":name,"age":age,"score":score})
    return c,er
def process_strict(records):
    c_r,e_r=process_records(records)
    print("\nclean record:\n",c_r)
    if e_r:
        f=len(e_r)
        print("\nerror log:\n",e_r)
        raise RuntimeError(f"{f} records failed to process")
    return c_r,e_r
clean,error=process_strict(l)
