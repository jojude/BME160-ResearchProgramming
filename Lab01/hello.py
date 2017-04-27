#!/usr/bin/env python3
# Name : Jude Joseph (jajoseph)
# Group Members : none

"""
This is my first python program, which will print out the
string Hello World when run.

"""
class announcement (str):
	def printAnnouncement(self):
		print(self)

def main():
	student = announcement("Hello World!")
	student.printAnnouncement()

main()
