# home work 1
# option 1
def greet(name):
    name_list = []
    name_list.append(name)
    greeting = "Hello,{} how are you doing today?".format(*name_list)
    return greeting


# option 2
def greet(name):
    return f"Hello, {name} how are you doing today?"
