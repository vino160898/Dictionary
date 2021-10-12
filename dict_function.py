marks={}
marks['Tamil']=55
marks['Hindi']=66
print(marks)
#del marks        #--> permanently delete
marks.clear()     #--> empty {}
print(marks)
d=dict([(1,'kathir'),(2,'kavin'),(3,'vijay')])
print(d)
print(d[1])       # kathir
print(d.get(1))   # kathir
#print(d[123])     # not present in this key, so accoring error
print(d.get(123)) # not present in this key, but not accoring error
print(type(d[1])) # sting
print(type(d))    # dict
print(d.pop(1))   # kathir
print(d.popitem()) #last pair --> (3,'vijay') 
print(type(d.popitem()))  #Tuple
print(d.keys())          #   dict_keys([1,2,3])
print(type(d.keys()))    # dict_keys 
print(d.values())        # dict_values(['kathir','kavin','vijay'])
print(type(d.values()))  # dict_values
print(d.items())         # dict_items ([(1,'kathir'),(2,'kavin'),(3,'vijay')])
print(type(d.items()))   # dict_items

d2=d.copy()
print(id(d2))    #-->different memory
print(id(d))     #-->different memory

d.setdefault(1,'arul')  #existing key , so not changing
d.setdefault(4,'arul')  #new key ,So add this pair
print(d)
d3=dict([(3,'vinoth'),(4,'raja')]) 
d.update(d3)     #Existing key accept this value and updating
print(d)
