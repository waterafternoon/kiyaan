#this has to be edited based on what you want.
#edit foldername, nonmatchfolder, and keyword
#the two folders must be in the same folder as this python file
#files should probably be text files. pdf files will probably not work.

import glob
import re
import os
import time

foldername = "bowl"
nonmatchfolder = "bee"

keyword = 'Bowl'

dirpath = ".\\"+ foldername + "\\*"
packlist = glob.glob(dirpath)

print("sorting non-matching files out of", foldername, "into", nonmatchfolder, "keyword being", keyword)
time.sleep(5)
def nhbb_sifter(packlist,keyword):
	x = 0
	deletelist = list()
	
	for packfile in packlist:
		
		x = x+1
		print("accessing ",packfile,"file "+str(x))
		axtext = open(packfile,"r")
		matching = check_nhb(axtext,keyword)
		
		if matching == True: 
			print("matching keyword")
		elif matching == False: 
			deletelist.append(packfile)
			print("not matching: adding ",packfile, "to delete list")
		else:
			print("Ooops. Something went wrong on ",packfile,matching)
			break
		time.sleep(.01)
	return deletelist

def check_nhb(axtext,keyword):
	linenumber,linelimit,result = 0,5,'fuck'
	for line in axtext:
		if keyword in line:
			result = True
			break
		elif keyword not in line:
			linenumber = linenumber + 1
			if linenumber >= linelimit:
				result = False
				break
		else: break #this is to help with debugging. see the first line in this def, fuck is the default and passes to matching, passing to else
	return result
			
movelist = nhbb_sifter(packlist,keyword)

print("moving files without keyword",keyword,"to",nonmatchfolder)
time.sleep(3)

for packfile in movelist:
	filename = re.sub(r".*?\\","",packfile)
	newfilepath = ".\\" + nonmatchfolder + "\\" + filename
	
	print("not matching keyword", keyword + ",", "moving to", nonmatchfolder, ":",  newfilepath)
	os.rename(packfile, newfilepath)
	time.sleep(0.05)
	
print("done. nothing happened? try making sure the folders have the right names. also, keyword is case-sensitive.")

"""
Stay when you think you want me
Pray when you need advice
Hey, keep your sickness off me (i'm trying to get through)

Blame all your weakness on me
Shame that i'm so contrite
Hey, keep your fingers off me (why can't I get through?)
"""