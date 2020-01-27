#! python3

fileObj = open('myText.txt')
contents = fileObj.read()
fileObj.close()

print('\n'+contents+'\n\n')

words = contents.split()

for word in words:
    if word == 'ADJECTIVE':
        print('Enter an adjective')
        adj = input()
    

# print(words)
# fileObj = open('newText.txt', 'w')
# fileObj.write(contents)
# fileObj.close()