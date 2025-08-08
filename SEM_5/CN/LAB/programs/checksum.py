print("SENDER - ")
word = input("Enter the word: ")
hexcode= []

if len(word)%2 == 0:
    for i in range (int(len(word)/2)):
        hexcode.append(hex(ord(word[2*i])) + hex(ord(word[2*i+1])))
else:
    hexcode.append("00"+hex(ord(word[0])))
    for i in range (1,int(len(word)/2)+1):
        hexcode.append(hex(ord(word[2*i-1])) + hex(ord(word[2*i])))
print("Hex strings for the input: ")
for i in range (len(hexcode)):
    hexcode[i].replace('0x',"")
    print(hexcode[i])

sum = "0000"
for i in range (len(hexcode)):
    hexcode1 = str(hexcode[i]).replace("0x","")
    temp = int(sum,16) + int(hexcode1,16)
    sum = hex(temp)

sum = str(sum.replace("0x",""))
print("Sum: ",sum)
if len(sum)>4:
    n = len(sum)-4
    sum1 = (sum[0:n])
    sum2 = (sum[n:])
    temp = int(sum1,16) + int(sum2,16)
    sum = hex(temp)
comp = int("FFFF",16) - int(sum,16)
sum = hex(comp)
print("The checksum is: ",sum )
x = sum

print("RECEIVER - ")
word = input("Enter the word: ")
hexcode = []

if len(word)%2 == 0:
    for i in range (int(len(word)/2)):
        hexcode.append(hex(ord(word[2*i])) + hex(ord(word[2*i+1])))
else:
    hexcode.append("00"+hex(ord(word[0])))
    for i in range (1,int(len(word)/2)+1):
        hexcode.append(hex(ord(word[2*i-1])) + hex(ord(word[2*i])))
print("Hex strings for the input: ")
for i in range (len(hexcode)):
    hexcode[i].replace('0x',"")
    print(hexcode[i])

sum = "0000"
for i in range (len(hexcode)):
    hexcode1 = str(hexcode[i]).replace("0x","")
    temp = int(sum,16) + int(hexcode1,16)
    sum = hex(temp)

sum = str(sum.replace("0x",""))
print("Received Checksum: ",sum)
if len(sum)>4:
    n = len(sum)-4
    sum1 = (sum[0:n])
    sum2 = (sum[n:])
    temp = int(sum1,16) + int(sum2,16)
    sum = hex(temp)
y = sum
comp = int("FFFF",16) - int(sum,16)
sum = hex(comp)

final = hex(int(x,16) + int(y,16))
print("1's complement: ", final[2:])
if final[2:] == 'ffff':
    print("Data received: valid")
else:
    print("Data received: invalid")