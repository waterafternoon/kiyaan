import glob
import time
import re
import fileinput
import random

foldername = "altpackets\\2015 PACE NSC"
packetnameheader = "Camioneto" + "_"
all_extracted_questions = "question_cutter_all.txt"

dirpath = ".\\"+ foldername + "\\*"
packlist = glob.glob(dirpath)

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
	
	tossuplist = re.findall(r"\d{1,2}\..*?\rANSWER:.*?\r",tossup)
	tossuplist = strip_number(tossuplist)
	
#	appendtest(tossuplist)
	return tossuplist

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

print("using files from this directory:", dirpath)
questionlist = list()

for filepath in packlist:
	print("adding this file to question pool",filepath)
	filestring = presanitize(filepath)
	questions = re.search("- Tossups.*- Bonuses",filestring,flags=re.DOTALL).group(0)
	extracted_questions = extract_questions(questions)
	questionlist.extend(extracted_questions)

aeq_path = ".\\export\\" + all_extracted_questions
with open(aeq_path,"w+",encoding="utf8") as aeq_handle: 
	for q in questionlist:
		aeq_handle.write("%s\n" % q)
print("exported all extracted questions to", aeq_path)