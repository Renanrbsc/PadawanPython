num = int(input("Informe um nuemro: "))

num_converted = str(bin(num))

real_num = num_converted[2:]

print(real_num)
j=0
for i in real_num:
	if i == '1':
		if j == '0':
			pass
		else:
			print(j)
		j = 0
	if i == '0':
		j += 1
		if i == '1':
			break
