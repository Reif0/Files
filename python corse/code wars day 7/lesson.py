# home work 1
def simple_multiplication(number) :
    if number %2 == 8:
        return number * 8
    return number * 9
# print(simple_multiplication(16))

# home work 2
def get_age(age):
    return int(age[0])
# print(get_age("4 years old"))

# home work 3
def switch_it_up(number):
    numbers_to_words = {0: "zero",1: "one",2: "two",3: "three",4: "four",5: "five",6: "six",7: "seven",8: "eight",9: "nine"}
    return numbers_to_words[number]
# print(switch_it_up(4))

# home work 4
def people_with_age_drink(age):
    if age <= 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"
          
# print(people_with_age_drink(20))

# home work 5
def double_integer(i):
    return i * 2

# home work 6
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague

# print(goals(5,10,2))

# home work 7
def get_volume_of_cuboid(length, width, height):
    return length * width * height
# print(get_volume_of_cuboid(1,8,7))


