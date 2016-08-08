import glob
import time
import re
import fileinput
import random
import os
import sys

if os.name == 'nt':
    Windows = True
else:
    Windows = False

foldername = "altpackets\\2015 PACE NSC"
if Windows == False: foldername = "altpackets/2015 PACE NSC"

packetnameheader = "_PACE Shuffle"
all_extracted_questions = "question_cutter_all.txt"

automaxpackets = True 
#if true, ignores numberofpackets
#and finds the max amt of packets
#that can be created
numberofpackets = 10

questionsperpacket = 8
createpackets = True

def presanitize(filepath):
	filehandle=open(filepath,"r",encoding="utf8")
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
	filestring = re.sub(r"- Page \d{1,2} of \d{1,2}",r"\r\n",filestring)
	for i in range(5): filestring = re.sub(r"\n|\r\r|\r\r\r|\r\r\r\r|\r \r",r"\r",filestring)
	for i in range(5): filestring = re.sub(r"\r ",r"\r",filestring)
	for i in range(5): filestring = re.sub("^ ","",filestring)
	for i in range(5): filestring = re.sub(r"::",r":",filestring)
	#so many unnecessary iterations. this def should have been renamed anal_retentive_sanitation().
	return filestring

def extract_questions(tossup):
	tossup = remove_double(tossup)
	tossup = re.sub(r"\r(?!ANSWER:|\d{1,2}\.)", " ", tossup)
	tossup = remove_double(tossup)
	tossup = re.sub(r"\d{1,69}-\d{1,69}-\d{1,69}.*?(\r|$)", r" \r",tossup)
	tossup = remove_double(tossup)
#	tossup = re.sub(r"\<.*?\>", " ", tossup)
	tossup = remove_double(tossup)
	
	tossuplist = re.findall(r"\d{1,2}\..*?\rANSWER:.*?\r",tossup)
	tossuplist = strip_number(tossuplist)
	
	tossuplist2 = list()
	for item in tossuplist: 
		item2 = re.sub(r"\<.*?\>", " ", item)
		tossuplist2.append(item2)
#	appendtest(tossuplist)
	return tossuplist2

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

def assign_numbers(packetquestions):
	questionnumber = 1
	numberedquestions = list()
	for x in packetquestions:
		numberedquestions.append(str(questionnumber) + ". " + x)
		questionnumber = questionnumber +1
		if questionnumber >= 24601: print("http://i2.kym-cdn.com/photos/images/original/000/878/073/2a2.gif")
	return numberedquestions

dirpath = ".\\"+ foldername + "\\*"
if Windows == False: dirpath = "./"+foldername+"/*"

packlist = glob.glob(dirpath)
print("using files from this directory:", dirpath)

questionlist = list()

for filepath in packlist:
	print("adding this file to question pool",filepath)
	filestring = presanitize(filepath)
	questions = re.search("- Tossups.*- Bonuses",filestring,flags=re.DOTALL).group(0)
	extracted_questions = extract_questions(questions)
	questionlist.extend(extracted_questions)

aeq_path = ".\\export\\" + all_extracted_questions
if Windows == False: aeq_path = "./export/" + all_extracted_questions

with open(aeq_path,"w+",encoding="utf8") as aeq_handle: 
	for q in questionlist:
		aeq_handle.write("%s\n" % q)
print("exported all", len(questionlist) ,"extracted questions to", aeq_path)

if automaxpackets == True:
	numberofpackets = int(round(len(questionlist)/questionsperpacket,0) - 1)
	print("automatically creating maximum amount of packets:",numberofpackets)

nop = numberofpackets
q1q = questionsperpacket
samtossups = random.sample(questionlist,q1q*nop)
for x in range(numberofpackets):
	namesuffix = x + 1
	if namesuffix < 10: namesuffix = "0" + str(namesuffix)
	else: pass
	filename = ".\\export\\" + str(namesuffix) + packetnameheader + ".txt"
	if Windows == False: filename = "./export/" + str(namesuffix) + packetnameheader + ".txt"
	
	filehandle = open(filename,'w+',encoding="utf8")
	
	fc,sc = 0,0	#0-9, 10-19, 20-29
	packettossups = samtossups[((x*q1q)+fc):((x+1)*q1q+sc)]
	packettossups = assign_numbers(packettossups)
	packet = packettossups
	
	if createpackets == True: 
		for item in packet: filehandle.write("%s\n" % item)
	else: pass
	filehandle.close()