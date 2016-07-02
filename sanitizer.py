#takes a shitload of files and converts them into a readable format, with a little bit of cleaning up to make parsing easier
#sanitization is probably not the right word.

foldername = "bowl"

dirpath = ".\\"+ foldername + "\\*"
packlist = glob.glob(dirpath)

