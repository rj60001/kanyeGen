import random

def lyricGen(length):
	words = ["woop", "de", "scoop", "poop", "diddy", "foop"]
	lyric = ""
	if length != 0:
		lyric = lyricGen(length-1)
	num = random.randint(0, 5)
	lyric += " "+words[num]
	return lyric

def paragraphGen(length):
	paragraph = ""
	if length != 0:
		paragraph = paragraphGen(length-1)
	paragraph += ""+lyricGen(1)+"\n"
	return paragraph

def songGen(length = random.randint(3, 13), paragraphLength = random.randint(1, 15)):
	song = ""
	if length != 0:
		song = songGen(length-1)
	song += paragraphGen(paragraphLength)+"\n\n"
	return song
