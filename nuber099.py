
file_handle = open('number.txt', 'r')

Write_in = open('CZnumber1.txt', mode='w')
line = file_handle.readline()
print(line)
Write_in.write('[')
while line:
    for i in range(0, 100):
        if i >= 10:
            number = line[:7] + str(i) + '68'
        else:
            number = line[:7] + '0' + str(i) + '68'
        print(number)
        Write_in.write('"' + number + '"' + ',')
    line = file_handle.readline()
Write_in.write(']')
file_handle.close()
Write_in.close()
