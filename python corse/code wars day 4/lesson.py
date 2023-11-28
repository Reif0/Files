# home work 1
def replace(text):
    return text.replace("t","T")

# home work 2
def find_average(nums):
    # jami
    summation = sum(nums)
    # raodenoba
    amount = len(nums)
    # dayofastan gamklaveba
    if len(nums) == 0:
        return 0
    # jami gayofili cifrebis raodenobaze
    return summation / amount
# print(find_average([1,2,4,8]))

#home work 3
def replace_dots(s): 
    return s.replace(".","-")

# print(replace_dots("l.u.k.a"))

# home work 4
def add_length(str_):
    #your code here
    str_ = str_.split()
    result = []
    for word in str_:
        result.append(word + " " +  str(len(word)))
    return result 

# home work 5 
def find_needle(haystack):
    for index in range(len(haystack)):
        if haystack[index] == "needle":
            return "found the needle at position ".format(index)
        return "there is not needle at all"

# print(find_needle("h"))

# home work 6
def uni_total(s):
    return sum([ord(char) for char in s])

# home work 7
def is_digit(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

print(is_digit(1))

# home work 8
def smash(words):
    return " ".join(words)







      
