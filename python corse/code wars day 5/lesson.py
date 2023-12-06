# # # home work 1
# def if_chuck_says_so():
#     return 5 > 3 and 5 < 3
# print(if_chuck_says_so())

# # # home work 2
# def are_you_playing_banjo(name):
#     i = 0
#     while i < len(name):
#        if name[i] in "Rr":
#           i += 1
#           return name + " plays banjo"
#        return name + " does not play banjo"
# print(are_you_playing_banjo("riki"))

# # home work 3
# def count_sheeps(sheep):
#     count_sheeps1 = sheep.count(True)
#     return count_sheeps1

# home work 4
def array_plus_array(arr1,arr2):
    result = []
    for i in range(0, len(arr1)):
        result.append(arr1[i] + arr2[i])
    return sum(result)

print(array_plus_array([1, 2, 3], [4, 5, 6]))

# home work 5
def double_char(s):
    a = ""
    for i in s:
        a = a + i*2
    return a  
print(double_char("luka"))      
  
# home work 6
def sum_str(a, b):
   if a == "":
       a = 0
   if b == "":
       b = 0
   return str(int(a) + int(b))

print(sum_str("1","1"))

# home work 7
def add_five(num):
    total = num + 5
    return total










         

        

