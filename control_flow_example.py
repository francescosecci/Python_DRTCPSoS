condition1 = False
condition2 = False
condition3 = True


if condition1:
	print "a"
elif condition2:
	print "b"
elif condition3:
	print "c"
else:
	print "d"
print "\n\n\n"

#---------------------------------------------------------------------#


a_list = ["The", "cat", "is", "on", "the", "table."]

for i in a_list:
	print i + "\n"


for j in range(5):
	print j
#riscrivere slides

print "\n\n\n"




#---------------------------------------------------------------------#

x = 0

while x < 5:
	if x == 3:
		x = x + 1
		continue
	print x
	x = x + 1



x = 0

while x < 5:
	if x == 3:
		break
	print x
	x = x + 1

