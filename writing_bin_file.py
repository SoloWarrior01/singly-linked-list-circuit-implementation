f = open('ps.bin', 'w+b')
array = [57, 10, 65, 217, 14, 155, 111, 3, 8, 70, 48, 6, 69, 196, 89, 255, 36, 32]
binary_format = bytearray(array)
f.write(binary_format)
f.close()
