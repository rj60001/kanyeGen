import random

def kanyeGen(length):
	words = ["woop", "de", "scoop", "poop", "diddy", "foop"]
	lyric = ""
	if length != 0:
		lyric = kanyeGen(length-1)
	num = random.randint(0, 5)
	lyric += " "+words[num]
	return lyric
	
