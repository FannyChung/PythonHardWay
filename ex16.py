from sys import argv

script ,filename =argv

print "We're going to erase %r." %filename
print "If you don't want that, hic (^C)"
print "If you do want that,hit RETURN"

raw_input("?")

print "Opening the file..."
target=open(filename,'w')

print "Truncating the file GoodBye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1=raw_input("Line1: ")
line2=raw_input("line2:")
line3=raw_input("line3")

print "I'm going to write these to the file"

target.write(line1+"\n")
target.write("%s\n"%line2)
target.write(line3)
target.write("\n")

print "And finally we close it"
target.close()