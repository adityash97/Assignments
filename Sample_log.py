# Problem Statement.
# Identify all the section in the sample log and create separate file for each section with the section name as file name.  

# Note: A new section begins when a row start with the word show and ends till another row beginning with show is found which is the beginning of new section.

#     Identify all the IP address in the log and replace with random valid IP address
#     Identify all MAC Id and ESS Id in the log and replace by random valid MAC ids 
import re
from ipaddress import IPv4Address
from random import getrandbits
from generate_mac import generate_mac
file = open("/Users/aditya/Downloads/sample_log.txt",'r') 
indexNos = {} #storing line no of "show**"

# replacing ip address with random ip address
def replaceIp(data):
    newData = []
    fstring = data
    patternIp = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})') 
    lst=[] 
    counter = 0
    for line in fstring: 
        counter+=1
        bits = getrandbits(32)
        addr = IPv4Address(bits)
        addr_str = str(addr)
        if(patternIp.search(line) != None):
            ip =  patternIp.search(line)
            lst.append((patternIp.search(line),counter)) 
            newData.append(line.replace(ip.group(),addr_str)) #replaceing with  "addr_str"
            
        else:
            newData.append(line)

    replaceMac(newData) #calling replace mac
# Replaceing mac address with random address
def replaceMac(data):
        
        print("Replaceing Mac")
        newData = []
        fstring = data
        patternMac = re.compile(r'\b[a-f0-9]{2}(?:([:-]?)[a-f0-9]{2}(?:\1[a-f0-9]{2}){4}|(?:\.?[a-f0-9]{2}){5})\b', re.IGNORECASE)
        for line in fstring: 
            if(patternMac.search(line) != None):
                mac = patternMac.search(line) 
                newData.append(line.replace(mac.group(),generate_mac.total_random())) #replacing with random mac

            else:
                newData.append(line)

        # print(newData)
        name = list(indexNos.keys()) #taking keys 
        saveOutput(newData,name[0]) #taking first key from name
        # newSuperData = []

# Saving output to new file
def saveOutput(data,filename):
    print("Saving output")
    url = "/Users/aditya/Downloads/"+filename+".txt"
    f = open(url,'a')
    string = ""
    for i in data:
        string+=i
    f.write(string)
    f.close()
    indexNos = {} #making indexNos empty.

        


# finding names "show **" and appending all data into data
lst = []    #to store names  "show **"
data  = []  #data is here from file
for i in file:
    if("show" in i):
        # print(i)
        lst.append(i) #taking only "show **"
    data.append(i) # taking data in data list

newLst = [] #removing '\n ' from lst,contains all "show **"
for i in lst:
    newLst.append(i.strip('\n ')) #removing '\n' from data

# ['show switches', 'show country', 'show country trail']
print("Data (only 'show'): ",newLst)

file.close() #file closed



#iterating for all "show **" and finding in given log file

for show in range(len(newLst)-1): 
    firstName = ""
    secondName = ""
    counter = 0
    secondCount = 0 #for first show
    firstCount = 0  #for second show
    file = open("/Users/aditya/Downloads/sample_log.txt",'r') 
    for i in file:
        counter +=1
        first = re.match(r'\b('+newLst[show]+')', i) 
        second = re.match(r'\b('+newLst[show+1]+')', i)
        # finding first "show"
        if(first != None ):
            # print("first",first.start(),"counter ",counter)
            firstName = first.group()
            if(firstCount == 0):
                indexNos[firstName] = counter
                firstCount+=1
                first = None
        # finding second "show"
        if(second != None):
            # print(second.start(),"counter ",counter)
            secondName = second.group()
            if(secondCount == 0):
                indexNos[secondName] = counter
                secondCount+=1
                second = None
        # writing stopping condition
        keys = list(indexNos.keys())
        if(len(keys) == 2):
            break
    # print(indexNos) #printing indexes
    keys = list(indexNos.keys())
    if(len(keys) == 2):
        replaceIp(data[indexNos[firstName]-1:indexNos[secondName]])  #calling function,giving specific data to replaceIp [1:4]
        # replace Mac will be called by replaceIp internally
        indexNos = {}
    file.close() #fileclosed







