d={1:'Ram',2:'Mukesh',3:'Suresh'}
for k,v in d.items():
    print(k,"->",v)

print(d.setdefault(3,'Tarun'))
print(d.setdefault(4,'Tarun'))
print(d)
