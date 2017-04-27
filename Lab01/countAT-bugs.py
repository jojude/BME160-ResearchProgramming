#!/usr/bin/env python3
# Name: David Bernick(dbernick)
# Group Members: none

"""
Corrections made (3) :
	Line 26 len(self) returns length of dnaString not length(self)
	Line 29 self.count("A") missed quotes 
	Line 36 0.3f format to print digits up to third decimal point  

"""
 
class dnaString (str):
	"""
	Model of dnaString

	s.upper() - gets upper case dna sequence

	def length - returns length of sequence 
	def getAT - returns A to T ratio 
	"""
    def __new__(self,s):
        return str.__new__(self,s.upper()) 

    def length (self):
        return (len(self))

    def getAT (self):
        num_A = self.count("A")
        num_T = self.count("T")
        return ((num_A + num_T)/ self.length() )
 
dna = input("Enter a dna sequence: ")
coolString = dnaString(dna)
 
print ("AT content = {0:0.3f}".format(coolString.getAT()) )