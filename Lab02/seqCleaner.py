#!/usr/bin/env python3
# Name : Jude Joseph (jajoseph)
# Group Members : none

"""
	Basic cleaner model that takes dnaSequence
	changes it all to upper case 

	clean() - finds row of N's in sequence 
			  replaces N's with {numberOfNsFound}
			  returns new cleaned sequence
"""
class Cleaner(str):

	def __new__(self, s):
		return str.__new__(self,s.upper())

	def clean(self):
		count = len(self) - len(self.replace("N", ""))
		cleanSequence = self.replace("N"*count, "{"+str(count)+"}")
		return cleanSequence

def main():
	dnaSequence = input("Enter dna sequence : ")
	newSequence = Cleaner(dnaSequence)
	print(newSequence.clean())

main()