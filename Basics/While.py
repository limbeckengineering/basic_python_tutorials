#while statements will execute over and over until certain condition is met. We call this a loop
i = 0
while i < 10:
	i = i + 1
	#Hint: this will do the same as the line above: i += 1
	print(i)

#A boolean value can be used in a while statement too
b = True
while b == True:
	i = i - 1
	if i == 0:
		b = False
		print("Done")

#Try some while loops of your own
