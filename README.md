This folder has two .py files, both of which are ready to go, out of the box. 
Those files are named bowlmaker.py and beemaker.py, and they require python 3.

-run 

-By default, this will create A-level bowl packets. These packets won't have any repeating questions.

-These packets will be in the .txt file format in the folder, named Stockholm0, Stockholm1, and so on.

questioncutter.py is a script to extract relevant question formats from otherwise incompatible packets. it creates an exported file.


### Want to change...

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

### Todo
	Reformat the damn README.
	
### Timeline

2016-7-19 Added questioncutter.py