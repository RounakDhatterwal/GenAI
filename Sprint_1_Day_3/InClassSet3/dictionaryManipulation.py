def add(disc, name, age):
    disc[name] = age

def update(disc, name, age):
    if name in disc:
        disc[name] = age
    else:
        print("Invalid name entered.")    

def delete(disc, name):
    del disc[name]        

disc = {}
print(disc)

add(disc,"john",25)
update(disc,"john",26)
print(disc)
delete(disc,"john")
print(disc)

