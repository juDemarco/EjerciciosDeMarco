import random

def simple_list():
    lista_dicts=[]
    
    for n in range(10):
        dict={"id":n,"age":random.randint(1,100)}
        lista_dicts.append(dict)
    return lista_dicts    
    pass

def sort_list(dicts):
    nueva_lista=sorted(dicts, key=lambda k: k["age"])
    return nueva_lista
    pass
