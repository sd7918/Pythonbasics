myDict={
    "Fast":"We are pro",
    "code":"i am coder",
    "anotherdict":{'code':'bcc'}
}
#print((myDict.keys()))#returns the only all keys present in your dictionary
#print(myDict.values())#returns the only all values present in your dictionary
#print(myDict.items()) #returns the all (key,values) present in ypor dictionary
print(myDict)
updatedict={
    "Sanju":"friend",
    "sayak":"Friend",
    "code" : " hero"
}
myDict.update(updatedict)
print(myDict)#update the dict values and then print

#print(myDict.get("Fast")) #here two is print same 
#print(myDict["Fast"])

print(myDict.get("Fast2")) #here .get() methods show none because Fast2 is not available in dictionary
print(myDict["Fast2"])     #here throw error because Fast2 is not available in dictionary

