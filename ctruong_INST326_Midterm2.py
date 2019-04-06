def encrypt(plaintext, password):  #function for returning encrypted text

#retaining only alphabets (letters) from the plaintext. symbols (!) deleted. For loop adds only letters
        for char in password:
            if char.islower():
                plaintext=''.join(x for x in plaintext if x.isalpha())
#join method opposite of split, brings string together (in this case, if its alphabet)

                passwordList = [] #storing password as list of chars
                result='' #variable to store the final output result

#iterates through password characters and storing them in passwordList as int, translated to 0 for 'a'
                for p in password:
                        passwordList.append(ord(p)-ord('a'))
#counter variable2
                count=0
                length=len(passwordList)

#iterating over the plaintext and adding corresponding password char.
                plaintext = "DIMITRI"
                password = "pass"
                for i in range(len(plaintext)):
                    print(plaintext[i], ord(plaintext[i]), " - ", password[i % len(password)],
                          ord(password[i % len(password)]) - 97)

            else:
                print('Please enter a number')


#test case
print(encrypt("OBJECT!","abcd"))