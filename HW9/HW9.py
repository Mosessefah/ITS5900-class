import os  # importing os module

def process_dir(p, indent):
	try:
	    for item in os.listdir(p):
	        if os.path.isfile("{0}/{1}".format(p, item)):  # to show the files in directory
	            print("\t"*indent, item)
	        elif os.path.isdir("{0}/{1}".format(p, item)):  # to show all folders in directory
	            print("\t"*indent, "\x1b[1;31m{}\x1b[0;0m".format(item))  # to display the directory in red format
	            # process_dir("{0}/{1}".format(path, item), indent+1)
	except Exception:
		print("Not a file or directory.")

path = input("Enter a valid system path:")
print("\x1b[1;31m{}\x1b[0;0m".format(path))  # display user input in red format
process_dir(path, 1)  # importing os module
