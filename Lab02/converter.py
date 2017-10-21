#!/usr/bin/env python3
# Name : Jude Joseph (jajoseph)
# Group Members : none

short_AA = {
            'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
            'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
            'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', 
            'ALA': 'A', 'VAL': 'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'
            }

long_AA = {value:key for key,value in short_AA.items()}

RNA_codon_table = {
# Second Base
# U             C             A             G
#U
'UUU': 'Phe', 'UCU': 'Ser', 'UAU': 'Tyr', 'UGU': 'Cys',
'UUC': 'Phe', 'UCC': 'Ser', 'UAC': 'Tyr', 'UGC': 'Cys',
'UUA': 'Leu', 'UCA': 'Ser', 'UAA': '---', 'UGA': '---',
'UUG': 'Leu', 'UCG': 'Ser', 'UAG': '---', 'UGG': 'Trp',
#C 
'CUU': 'Leu', 'CCU': 'Pro', 'CAU': 'His', 'CGU': 'Arg',
'CUC': 'Leu', 'CCC': 'Pro', 'CAC': 'His', 'CGC': 'Arg',
'CUA': 'Leu', 'CCA': 'Pro', 'CAA': 'Gln', 'CGA': 'Arg',
'CUG': 'Leu', 'CCG': 'Pro', 'CAG': 'Gln', 'CGG': 'Arg',
#A
'AUU': 'Ile', 'ACU': 'Thr', 'AAU': 'Asn', 'AGU': 'Ser',
'AUC': 'Ile', 'ACC': 'Thr', 'AAC': 'Asn', 'AGC': 'Ser',
'AUA': 'Ile', 'ACA': 'Thr', 'AAA': 'Lys', 'AGA': 'Arg',
'AUG': 'Met', 'ACG': 'Thr', 'AAG': 'Lys', 'AGG': 'Arg',
#G
'GUU': 'Val', 'GCU': 'Ala', 'GAU': 'Asp', 'GGU': 'Gly',
'GUC': 'Val', 'GCC': 'Ala', 'GAC': 'Asp', 'GGC': 'Gly',
'GUA': 'Val', 'GCA': 'Ala', 'GAA': 'Glu', 'GGA': 'Gly',
'GUG': 'Val', 'GCG': 'Ala', 'GAG': 'Glu', 'GGG': 'Gly'
}

dnaCodonTable = {key.replace('U','T'):value for key, value in RNA_codon_table.items()}


'''
	Converter model to take input and classify what the user is looking for 
	The convert() function checks if the user inputted a RNA codon or DNA 
	as well as if they are looking for an amino acid letter or 3 letter combination
'''
class Converter():

	def __init__(self,seq):
		self.sequence = seq
		
# private helper methods
	def printOut(self,result):
		print("{0} = {1}".format(self.sequence,result))

	def isNotAA(self):
		if self.sequence in short_AA.keys():
			return False
		return True

#translation functions
	def getAA(self):
		if(len(self.sequence) > 1):
			return short_AA.get(self.sequence.upper(), "Unknown")
		else:
			return long_AA.get(self.sequence, "Unknown")

#conversion function to print out correct translation
	def convert(self):
		if(len(self.sequence) > 1 and self.isNotAA()):
			if("U" in self.sequence):
				self.printOut(RNA_codon_table.get(self.sequence, "Unknown"))
			else:
				self.printOut(dnaCodonTable.get(self.sequence, "Unknown"))
		else:
			self.printOut(self.getAA())

def main():
	sequence = input ("Enter codon or AA : ")
	converter = Converter(sequence)
	converter.convert()

main()

