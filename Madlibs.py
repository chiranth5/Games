# Joining strings

# My first project is ______
# project1 = Madlibs

# Ways to print it
# 1.print(" My first project is " +project1)
# 2.print(f" My firstt project is {project1}")
# 3.print(" My first project is {} ".format(project1))

adj = input("Adjective: ")
verb1 = input("Verb 1: ")
verb2 = input("Verb 2: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming  is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like your {famous_person}!"

print(madlib)