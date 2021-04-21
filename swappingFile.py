def swapingFile():
	file_name1 = input("Give the name of the file that you want to swap: ")
	file_name2 = input("Give the name of another file that you want to swap with: ")

	with open(file_name1, "r") as a:
		data_a = a.read()
	with open(file_name2, "r") as b:
		data_b = b.read()

	with open(file_name1, "w") as a:
		a.write(data_b)

	with open(file_name2, "w") as b:
		b.write(data_a)

swapingFile()