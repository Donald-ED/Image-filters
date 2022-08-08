'''
	CSCI 120 programming assignment [100pts]
	Assumptions:
		* plain_text only contains letters from 
			the english alphabet
		* we can have both lower and upper case
			letters in the plain_text
		* plain_text can be of any length
		* key is an arbitrary valued integer

	Hint: lookup ord( )	and chr( ) function in Python

'''
def caesar_encrypt(cipher_text,key) -> str:
  key = key % 26
  for i in cipher_text:
    if ord(i) >= 65 and ord(i) <= 90: 
      num = ord(i) + key
      if num > 90:
        print(chr(num - 26), end = '')
      elif num < 65:
        print(chr(num + 26), end = '')
      else:
        print(chr(num), end = '')
    elif ord(i) >= 97 and ord(i) <= 122:
      num = ord(i) + key
      if num > 122:
        print(chr(num - 26), end = '')
      else:
        print(chr(num), end = '')  
    else:
      print(chr(ord(i)), end = '')
  return cipher_text    

  

def caesar_decrypt(cipher_text,key) -> str:
  key = key % 26
  for i in cipher_text:
    if ord(i) >= 65 and ord(i) <= 90:
      num = ord(i) - key
      if num < 65:
        print(chr(num + 26), end = '')
      else:
        print(chr(num), end = '')
    elif ord(i) >= 97 and ord(i) <= 122:
      num = ord(i) - key
      if num < 97:
        print(chr(num + 26), end = '')
      else:
        print(chr(num), end = '')
    else:
      print(chr(ord(i)), end = '')

  return cipher_text

cipher_text = "Attack at Dawn"  #Define the message
key = 412  #Define the key

#encrypt and store cypher text
plain_text = caesar_encrypt(cipher_text,key)
print("\n")
#decrypt and store plain text
decrypted_msg = caesar_decrypt(cipher_text,key)

