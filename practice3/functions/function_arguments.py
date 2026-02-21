def greeting(name):#created a function named greeting and parameter name
    print("hello, "+name)
greeting("Ilya")#calling a function and passing argumen "Ilya"
#result:"hello, Ilya"
#we must pass some agrument to greeting function, however, we can give a default parameter value
def func(name="Ilya",surname="Zaitsev"):
    print("nice to meet you "+name+" "+surname)
func("Askar","Akshabaev")#result will be: nice to meet you Askar
func()#this wont cause an error, because we made a default value so result will be: nice to meet you Ilya
#we can pass arguments to a function with a key=value syntax
func(surname="Doe",name="Jane")# if we use this syntax the order of arguments doesnt matter
func(name="Jane",surname="Doe")#result will be same
func("Doe","Jane")
func("Jane","Doe")#different results
func("jane",surname="doe")#we can mix positional and key arguments but positional arguments must come first
