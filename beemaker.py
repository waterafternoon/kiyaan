#just a reminder, this is python 3

import glob
import time
import re
import fileinput
import random

foldername = "bee"
#donefolder = "generatedbeepackets"

createpacket = True
#above lets you toggle actually creating packets. useful if you want to debug or test someting.


#below is the number of questions per category, in the case of q3q, it's the number of categories
#confused about q3q? think about it for a second.
numberofquestions = 32
q1q= numberofquestions


packetsneeded = 1
desireddifficulty = "CC"
#CA = A level
#CB = B level
#CC = C level
#CN = Nationals, apparently there aren't any National packets

packetnameheader = "Bee" + desireddifficulty + "_"

dirpath = ".\\"+ foldername + "\\*"
packlist = glob.glob(dirpath)

alltossups = list()
allbonus = list()
alllightning = list()
alltiered = list()

x=0

print("importing files from this directory:", dirpath)

def id_difficulty(axtext):
	linenumber,linelimit,difficulty = 0,5,'dang'
	for line in axtext:
		if "Bowl" in line:
			difficulty = "errorbowl"
			break
		elif "Bee A" in line: 
			difficulty = "CA"
			break
		elif "Bee B" in line:
			difficulty = "CB"
			break
		elif "Bee C" in line:
			difficulty = "CC"
			break
		elif "National" in line:
			difficulty = "CN"
			break
		elif "Set A" in line: 
			difficulty = "CA"
			break
		elif "Set B" in line:
			difficulty = "CB"
			break
		elif "Set C" in line:
			difficulty = "CC"
			break
		else:
			linenumber = linenumber + 1
			if linenumber >= linelimit:
				result = False
				break#this is to help with debugging. see the first line in this def, dang is the default 
	#	print(line)
	return difficulty	

def extract_tossup(tossup):
	tossup = remove_double(tossup)
	tossup = re.sub(r"\r(?!ANSWER:|\d{1,2}\.)", " ", tossup)
	tossup = remove_double(tossup)
	tossup = re.sub(r"\d{1,69}-\d{1,69}-\d{1,69}.*?(\r|$)", r" \r",tossup)
	#Standin' on your mama's porch \ You told me that it'd last forever
	tossup = remove_double(tossup)
	
	tossuplist = re.findall(r"\d{1,2}\..*?\rANSWER:.*?\r",tossup)
	tossuplist = strip_number(tossuplist)
	
#	appendtest(tossuplist)
	return tossuplist

def presanitize(filepath):
	filehandle=open(filepath,"r")
	filestring=filehandle.read()
	filehandle.close()

	for i in range(5): filestring = re.sub(r"  "," ",filestring)

	filestring = re.sub(r".*Bee.*","",filestring)
	filestring = re.sub(r".*tcpdf.*","",filestring)
	#to be replaced with something like "I'm Van Duong, and Arcadia High School Can't Use This Packet."
	for i in range(5): filestring = re.sub(r"  "," ",filestring)
	filestring = re.sub(r".*Round \d{1,2}","",filestring)
	filestring = re.sub(r"\\\"","\"",filestring)
	filestring = re.sub(r"\x0C","",filestring)
	for i in range(5): filestring = re.sub(r"\n|\r\r|\r\r\r|\r\r\r\r|\r \r",r"\r",filestring)
	for i in range(5): filestring = re.sub(r"\r ",r"\r",filestring)
	for i in range(5): filestring = re.sub("^ ","",filestring)
	for i in range(5): filestring = re.sub(r"::",r":",filestring)
	#so many unnecessary iterations. this def should have been renamed anal_retentive_sanitation().
	return filestring

def remove_double(thestring):
	#double spaces and double lines
	for i in range(7): thestring = re.sub(r"\n|\r\n|\r\r",r"\r", thestring)
	for i in range(7): thestring = re.sub(r"\r \r","\r", thestring)
	for i in range(7): thestring = re.sub("  "," ", thestring)
	return thestring

def strip_number(listofqs):
	listofqs2 = list()
	for item in listofqs:
		item = re.sub(r"^\d{1,2}\.","",item)
		item = re.sub("^ ","",item)
		listofqs2.append(item)
	#that's right, take off those numbers.
	return listofqs2

#the next three functions are for debugging.
#if you've taken liebenau's class, you still need another semester to understand this if you haven't studied by yourself.
def writetest(teststring):
	filehandle=open(".\\testfolder\\ayy.txt","w+")
	filehandle.write(teststring)
	filehandle.close()	
	print("writetest is being used")

def appendtest(testlist):
	filehandle=open(".\\testfolder\\ayy.txt","w+")
	for item in testlist:
		filehandle.write("%s\n\r" % item)
	filehandle.close()	
	print("appendtest is being used")

def listtofile(filename,list):
	tfln = ".\\testfolder\\"+filename+".txt"
	filehandle=open(tfln,"w+")
	for item in testlist:
		filehandle.write("%s\n\r" % item)
	#i have to admit, i copy-pasted the above two lines of code from stackoverflow. I don't know how this works.
	filehandle.close()
	print("listtofile is being used")
	
for filepath in packlist:
#	print("accessing file",filepath,x)
#	print("using the following file as a test")
#	filepath = r".\\testfolder\\nhbb (121).txt"
	textfile = open(filepath,"r+")
	difficulty = id_difficulty(textfile)
	textfile.close()

	if difficulty == desireddifficulty: 
		print("adding this file to question pool",filepath,str(x+1))
		x=x+1
	else: continue
	
	filestring = presanitize(filepath)
	
#	(tossup,bonus,lightning,tiered) = split_cats(filestring)

	tossuplist = extract_tossup(filestring)
	for item in tossuplist: alltossups.append(item)
	
def assign_numbers(packetquestions):
	questionnumber = 1
	numberedquestions = list()
	for x in packetquestions:
		numberedquestions.append(str(questionnumber) + ". " + x)
		questionnumber = questionnumber +1
		if questionnumber >= 24601: print("http://i2.kym-cdn.com/photos/images/original/000/878/073/2a2.gif")
	return numberedquestions
	
numberofpackets = packetsneeded#input("How many packets do you need?")
numberofpackets = int(numberofpackets)
packetnameheader = packetnameheader
	
nop = numberofpackets
samtossups = random.sample(alltossups,q1q*nop)

print("there are "+str(len(alltossups)) + " tossups.")
print(str(len(alltossups)/q1q)+ " packets can be created.")
#appendtest(alltossups)

#listofcreatedfiles = list()
	
for x in range(numberofpackets):
	tempx = x + 1
	if tempx < 10: tempx = "0" + str(tempx)
	else: pass
	filename = ".\\export\\" + str(tempx) + packetnameheader + ".txt"
	filehandle = open(filename,'w+')

	packettossups = samtossups[(x*q1q):((x+1)*q1q)]
	
	packettossups = assign_numbers(packettossups)
	
	if createpacket == True: 
		for item in packettossups: filehandle.write("%s\n" % item)
	else: pass
	filehandle.close()
	
	
if createpacket == True: print("Created " + str(nop) + " packets, leveled " + desireddifficulty)
else: print(desireddifficulty + " packets were processed.\nNo packets have been created. Change createpacket to = True if you want to make packets.")

#I keep on thinking that it's all done and all over now
#You keep on thinking you can save me, save meeee
#My ship is sinking but it's all good and I can go down
#You've got me thinking that the party's all over