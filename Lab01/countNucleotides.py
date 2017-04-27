#!/usr/bin/env python3
# Name : Jude Joseph (jajoseph)
# Group Members : none

"""
	Program returns count of nucleotides in given
	dna sequence and identifies how much of each nucleotide
	is present in the given sequence 
"""

class dnaString(str):
	""" 
	Simple model for dna data extraction

	"""
	def __new__(self, s):
		return str.__new__(self, s.upper())

	""" Retuns length of dna string """
	def length(self):
		return(len(self))

	""" Returns nucleotide count """
	def getNucleotideCount(self):
		num_A = self.count("A")
		num_T = self.count("T")
		num_C = self.count("C")
		num_G = self.count("G")
		return num_A, num_T, num_C, num_G

def main():
	""" Build new dnaString object """
	dna = input("Enter a dna sequence : ")
	coolString = dnaString(dna)

	num_A, num_T, num_C, num_G = coolString.getNucleotideCount()

	print("Your sequence is {0} nucleotides long with the following breakdown of bases :".format
			(coolString.length()))
	print("number As = {0}".format(num_A))
	print("number Cs = {0}".format(num_C))
	print("number Gs = {0}".format(num_G))
	print("number Ts = {0}".format(num_T))

main()