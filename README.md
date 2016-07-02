This folder has three .py files, one of which is ready to go, out of the box. 
That file is named bowlparser.py. It can technically be used to create bee packets, but it requires a lot of reworking.
Running bowlparser.py requires a few things beforehand.

1. Download python 3. Don't download Python 2.

2. Have Windows. 

	2a.If you're considering running this on any apple product, do the following:

	2b.trade it in for a pc, you spoiled little princess.

	2c.seriously though Jason or Srivaths or someone i don't know, the script should still work.
	
3.Open up your terminal or command prompt. On windows, it's cmd.exe

4.Navigate to this folder within the command prompt, then run the file with:
	python bowlparser.py
	
5.By default, this will create 2 A-level bowl packets. These packets won't have any repeating questions.

6. These packets will be in the .txt file format in this folder, named Stockholm0, Stockholm1, and so on.







6.Want to change...

the number of tossups?
	change q1q =

the number of bonus-questions?
	change q2q =

the number of lightning CATEGORIES?
	change q3q =

the number of tiered questions?
	change q4q =

the amount of packets produced?
	change packetsneeded = 

the level of the packets?
	change desireddifficulty = 

the fileprefix to something other than Stockholm?
	change packetnameheader = 