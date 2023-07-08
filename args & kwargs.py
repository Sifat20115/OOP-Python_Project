def id(*args):#like array
    print(args)
    for i in args :
        print(i)

id(12,13,14)

def display_person(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

display_person(Name="Amir Khan", Age="45")