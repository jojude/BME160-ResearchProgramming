#!/usr/bin/env python3
# Name : Jude Joseph (jajoseph)
# Group Members: none

class Person:
	"""
	Simple model for Person bio

	Keyword arguements:
	fullName -- full name of person
	username -- CATS/CruzMail username
	standing -- undergrad or graduate student
	major -- person's major
	goal -- why he/she is taking BME160/L 
	interest -- What problem in molecular biology most interests you
	priorExperience -- person's prior computer programming experience

	"""
	def __init__(self, fullName,username,standing,major,goal,
				interest,priorExperience):
		self.fullName = fullName
		self.username = username
		self.major = major
		self.standing = standing
		self.goal = goal
		self.interests = interest
		self.priorExperience = priorExperience

	def printBio(self):
		print("My name is {0}.".format(self.fullName))
		print("My username is {0}.".format(self.username))
		print("I am a {0}.".format(self.standing))
		print("My major is {0}.".format(self.major))
		print("I'm {0}.".format(self.goal))
		print("I'm interest in {0}!".format(self.interests))
		print("I have prior programming experience using {0}!".format
			(self.priorExperience))


def main():
	fullName = "Jude Allen Joseph"
	username = "jajoseph"
	major = "Bioinformatics"
	standing = "Undergraduate student"
	goal = "taking this class to learn how to write beautiful code in python"
	interests = "utilizing what I have learned to build products that will enhance a persons experience of life"
	priorExperience = "Java, C, Swift and Python"

	""" Build new person object and print their bio """
	thisPerson = Person(fullName,username,standing,major,goal,interests,priorExperience)
	thisPerson.printBio()

main()
