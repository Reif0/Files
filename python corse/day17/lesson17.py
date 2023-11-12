# home work 1
# import random
# list = ["luka siradze","anri zubashvili", "noi tsomaia", "dachi abashelidze", "ako mitiashvili"]
# while license:
#     select_random_num = random.choice(list)
#     question = ("{} answer this cuestion: waht is 1+1: ".format(select_random_num))
#     response = input(question)
#     if response == "2":
#         print("you answered correctly +1 point".format(select_random_num))
#     else:
#        print("you did not answered correctly -1 point".format(select_random_num))
#     list.remove(select_random_num)
# print("all group members have anwsered for today")

            

# home work 2

import random
weird_simbols = "!##%(#)^#"
siblos = "აბგქწეკჯასკჯქწე"
numbers = "215346347347"
weird_simbol_sum = random.choice(weird_simbols) + random.choice(weird_simbols) 
simbols_sum = random.choice(siblos) + random.choice(siblos) 
numbers_sum = random.choice(numbers) + random.choice(numbers) + random.choice(numbers) + random.choice(numbers)
sum = weird_simbol_sum + simbols_sum + numbers_sum
print(sum)




