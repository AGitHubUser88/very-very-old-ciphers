import random

def getKey(m,key,command):
        
    if command == 'Encrypt':
       key=[]
       mList = []
    
       for h in range(1,m+1): mList += [h]
            
       for i in range(1,m+1):
            
           j = random.choice(mList)
               
           while (j==i): j = random.choice(mList)
               
           if key: key += [(i,j)]
                 
           else:   key = [(i,j)] 
                  
           mList.remove(j)  
            
           return key
       
    if command == 'Decrypt':
        inverse = []
    
        for l in range(1,m+1): 
           for k in key:
               if l == k[1]:
                  inverse +=[(l,k[0])]
        return inverse
   
    else:  print('Not a valid command')


def cryptoSystem(inString, keyList,m):
    
    outString = ''
    splitString = [inString[i:i+m] for i in range(0, len(inString), m)]
 
    for word in splitString:
        counter = 0
        for letter in word:
            outString += word[(keyList[counter][1])-1]
            counter +=1 
            
    return outString        

        
if __name__ == '__main__':
    
    m = 7
    key = []
    message = 'shesellsseashellsbytheseashore'
    
    if len(message)%m >0: print('Enter a number easily divisible by the number of characters in the message'); exit(0)
    
    key = getKey(m,key,'Encrypt')
    
    message = cryptoSystem(message,key,m)
    splitString = [message[i:i+m] for i in range(0, len(message), m)]
    print(message)
    
    key = getKey(m,key,'Decrypt')
    
    message = cryptoSystem(message,key,m)
    print(message)