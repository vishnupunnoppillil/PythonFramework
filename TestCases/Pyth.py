class MyClass:
    def Sum(self,a,b):
        c=a+b
        print(c)

x=MyClass()
x.Sum(1,9)

class listStudy:
    my_list=["sasi","soman","raju"]
    print(my_list)
    my_list[2]="thankaraj"
    print(my_list)
    for val in my_list:
        print(val)
    my_list.append("qwerty")
    my_list.remove(my_list[0])
    print(my_list)