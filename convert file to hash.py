import os
import subprocess
'''
variables:
        courrentDir : courent directory of program
        n : number input of file number if directory
        l : terminal command  to calculate hash of chosen file
        result : output of command l
        hashOfFile : hash of file in result (number 2 (or 1 in python) element of list) 
        hashInput : input hash from source for compare
'''
print('your directory is:')
courrentDir=os.getcwd()    #get courent directory and save to variable 'courrentDir' 
os.chdir(courrentDir)      #change directory of program to courrent directory
print(courrentDir)         # print courent directory 
print('------------------------------------')
############################################################
#  change directory of program to courent directory and show      
############################################################
ListOfFiles=os.listdir()
print('choose file number:')
for i in range(1,len(ListOfFiles)+1):
    print('   ',i,':',ListOfFiles[i-1])
#show list of files in courent directory with number
try:    
    n=int(input())
    l='certutil -hashfile '+'\"'+ListOfFiles[n-1]+'\"'+' sha256'
    result = subprocess.check_output(l, shell=True, text=True)
    hashOfFile=result.split('\n')[1]
    print(hashOfFile)
    print(' ')
    print('enter your hash:')
    hashInput=str(input())
    print(hashInput==hashOfFile)
    input()
except:
    print('error')
