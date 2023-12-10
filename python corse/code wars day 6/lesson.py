# home work 1
def find_average(numbers):
    if numbers == []:
        return 0
    return sum(numbers) / len(numbers)
print(find_average([2,2]))

# home work 2
def expression_matter(a, b, c):
    num = [
        a * (b + c),
        a * b * c,
        a + b * c,
       (a + b) * c,
        a + b + c
    ]
    return max(num)

print(expression_matter(2,10,1))

# home work 3
def hoop_count(n):
    
    for i in range(n):
        if n >= 10:
            return "Great, now move on to tricks"
        return "Keep at it until you get it"
    
print(hoop_count(11))

# home work 4
def between(a,b):
    return list(range(a,b + 1))

# home work 5
def abbrev_name(name):
    words = name.split(" ")
    letters = [word[0].upper() for word in words]
    return ".".join(letters)

# home work 6
def dna_to_rna(dna):
    return dna.replace("T","U")
print(dna_to_rna("TTT"))

# home work 7
def opposite(number):
  return number * -1
print(opposite(5))
    




    


