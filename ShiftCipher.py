def shiftCipher(cryptoList, inString, key, command):
    """
	To avoid writing 2 functions with repeating code for encryption and decryption to accomodate such a small difference in mathematical calculation,
	we define the following switch variable to accept a custom parameter to command the program to either encrypt or decrypt.
	
	NOTE: Since the C based switch statment does not exist for Python the switcher variable is used
	"""

    switcher = {
        'Encrypt': key*1,
        'Decrypt': key*-1
    }
    
	"""Initialize returning variable"""
    outString = ''  
    
	"""
	    For each value in the string, get its numerical value, add the key value to it and return the new value
		For decryption, there will be a negative value added since this rule is defined in the switcher variable
		
		If addition results in a value that exceeds the range of the min and max number in the list. Use modular division to divide by the amount of items in the list to capture the remaining value beyond the max list and reset the count to that remaining number to avoid calcualting a number in the list that does not exist 
	"""
    if inString is not None:
        for char in inString:
            i = 0
            
            while(True):
                if char == cryptoList[i][0]:
                   outString += cryptoList[ ( ( cryptoList[i][1] ) + ( switcher.get( command, "N/A" ) ) ) % len(cryptoList) ][0]
                   break
                else:
                    i+=1
    else:
		Print("Input string is empty, please input a string value")
    
	return outString
    
	
if __name__ == '__main__':

	"""
	Define an array of all letters of the alphabet with an associated numerical value
	"""
    alphaNumList = [
                 ('a', 0 ),('b', 1 ),('c', 2 ),('d', 3 ),('e', 4)
                ,('f', 5 ),('g', 6 ),('h', 7 ),('i', 8 ),('j', 9)
                ,('k', 10),('l', 11),('m', 12),('n', 13),('o', 14)
                ,('p', 15),('q', 16),('r', 17),('s', 18),('t', 19)
                ,('u', 20),('v', 21),('w', 22),('x', 23),('y', 24)
                ,('z', 25)
              ]
    """
	The key will be added numeric value of the letter and the output will be the letter to the newly corresponding number 
	"""
	key = 11
    
	"""Hard code and print a sample plaintext message"""
	
    message = 'wewillmeetatmidnight'
    print('Original Plain:',message)
    
	"""Convert message to lower case to manage case sensitivity"""
    message = message.lower()
    
	"""Print Encrypted Cipher and Decrypted Plain Text"""
    message = shiftCipher(alphaNumList, message, key, "Encrypt")
    print('Encrypted Cipher:',message)
    
    message = shiftCipher(alphaNumList, message, key, "Decrypt")
    print('Decrypted Cipher:',message)
    
    
    """
	If someone who has the analytical background to detect a shift cipher is being used for encryption, they can easily run the decrypt algorithm and retrieve the plain text
	"""
    