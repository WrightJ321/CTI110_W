"""
CTI 110
P1HW1 - Variables
WrightJ
9/5/23
Do some basic output with numbers
1. ask for an int
2. square it and then cube it
3. ask for another int
4. add them and multiply them


"""
# Part one
# Variables, first and second
first = 0
second = 0

print("Enter integer:")
first = int(input()) # take input, then convert it to int
print(first, "squared is", first * first)
print("and", first, "cubed is" , first * first * first,"!!")


# get another int
print("Enter another integer:")
second = int(input())
print(first, "+", second, "=", first + second)
print(first, "*", second, "=", first * second)

# Part Two: MOVIES
# Three variables
# string - movie name
# int - the year of the movie
# float - the gross (in million dollars)
# string - a quote
# print a quote from the movie
name = "Goodfellas"
year = 1990
gross = 47.03 # mil $
quote = "'Fuck you, pay me.'"
# Print out this information
# Then print a movie quote
print("The movie", name, "released in theatres in the year of", year,".")
print(name,"grossed a staggering", gross, "Million dollars.")
print("one of my favorite quotes from", name, "is,", quote)
print("Considering the societal norms of", year,",", name,"was considered a vulgar movie amongst viewers.")

