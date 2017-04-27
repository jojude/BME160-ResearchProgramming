#!/usr/bin/env python3
# Name : Jude Joseph (jajoseph)
# Group Members : none

class Person:
	"""
	Model simple humans with name and favorite type of pet

	Keyword arguments:
	personName -- the name of that user
	petType -- type of favorite pet
	"""
    def __init__(self, personName, petType):
        self.name = personName;
        self.pet = petType;

    def introduce(self):
        print("Hi there, I am {0}!".format(self.name))
        print("I like {0}!".format(self.pet))


def main():
	"""
	Build a new person object, then introduce him/her
	"""
    userName = input("Hello, what is your name? :")
    pet = input("What is your favorite kind of pet? :")
    thisUser = Person(userName, pet)
    thisUser.introduce()

main()
