#Write somethin in a file
fw = open('sample.txt', 'w') #('name_of_file', 'w') #'w' = write
fw.write('writing som stuff in my text file\n')# ('write it now)
fw.writelines('I like bacon\n')
fw.close()

#Read from a file
fr = open('sample.txt', 'r') #('name_of_file', 'r') #'r' = read
#Whenever we read data from a file, we need somewhere to store it(i.e needs a variable)
#bcoz we cant just work with it directly in Python
text = fr.read()
print(text)
fr.close()
