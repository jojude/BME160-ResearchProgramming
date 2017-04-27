#!/usr/bin/env python3
# Name : Jude Joseph (jajoseph)
# Group Members : none

'''
	Simple sequence cleaning model
	
	parse - takes a fastq sequence and splits it 
	up to distinct parts and returns it in an 
	array format
'''
class fastqSeq():

	def __init__(self, sequence):
		self.seq = sequence

	def parse(self):
		newSeq = self.seq.replace("@","")
		return newSeq.split(":")

def main():
	'''
		Initialize template 
	'''
	file_details = ["Instrument", "Run ID", "Flow Cell ID", "Flow Cell Lane"
					,"Tile Number","X-coord","Y-coord"]

	fastq = input("Enter fastq information : ")
	info = fastqSeq(fastq)
	i = 0

	'''
		Loop through data and print out in correct label as provide
		by the template 
	'''
	for data in info.parse():
		print("{0} = {1}".format(file_details[i],data))
		i +=1

main()