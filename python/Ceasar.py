
alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "

def decoder(message, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = ".,?'! "
    plain_text = ""
    for letter in message: 
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            plain_text += alphabet[(letter_value + offset) %26]
        else:
            plain_text += letter
    return plain_text
print(decoder("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.", 10))
print(decoder("bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!", 14))



def encoder(message, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = ".,?'! "
    cipher_text = ""
    for letter in message: 
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            cipher_text += alphabet[(letter_value - offset) %26]
        else:
            cipher_text += letter
    return cipher_text


# Solving a Caesar Cipher without knowing the shift value
# can be done with computers.
# below is an example of how one would brute force the Caesar Cipher


for i in range(0,len(alphabet)):
    print(i ,decoder("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.", i))

# print(decoder("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.",7))


# #### The Vigenère Cipher
#  
# This next cipher is the Vigenère Cipher, invented by an Italian cryptologist named Giovan Battista Bellaso 
# in the 16th century, but named after another cryptologist from the 16th century, Blaise de Vigenère.
#             
# The Vigenère Cipher is a polyalphabetic substitution cipher, as opposed to the Caesar Cipher which was a 
# monoalphabetic substitution cipher. What this means is that opposed to having a single shift that is applied 
# to every letter, the Vigenère Cipher has a different shift for each individual letter. The value of the shift 
# for each letter is determined by a given keyword.
#            
#            Consider the message
#            
#                barry is the spy
# 
#            If we want to code this message, first we choose a keyword. For this example, we'll use the keyword
#            
#                dog
#                
#            Now we use the repeat the keyword over and over to generate a keyword phrase that is the same 
# 
# length as the message we want to code. So if we want to code the message "barry is the spy" our _keyword phrase_ is 
# 
# "dogdo gd ogd ogd". Now we are ready to start coding our message. We shift the each letter of our message 
# 
# by the place value of the corresponding letter in the keyword phrase, assuming that "a" has a place value of 
# 
# 0, "b" has a place value of 1, and so forth.
# 
#                         message:       b  a  r  r  y    i  s   t  h  e   s  p  y
#                 
#                  keyword phrase:       d  o  g  d  o    g  d   o  g  d   o  g  d
#                  
#           resulting place value:       4  14 15 12 16   24 11  21 25 22  22 17 5
#       
#             So we shift "b", which has an index of 1, by the index of "d", which is 3. This gives us an place value of 4, which is "e". Then continue the trend: we shift "a" by the place value of "o", 14, and get "o" again, we shift "r" by the place value of "g", 15, and get "x", shift the next "r" by 12 places and "u", and so forth. Once we complete all the shifts we end up with our coded message:
#             
#                 eoxum ov hnh gvb
#                 
#             As you can imagine, this is a lot harder to crack without knowing the keyword. So now comes the hard part. I'll give you a message and the keyword, and you'll see if you can figure out how to crack it! Ready? Okay here's my message:
#             
#                 dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!
#                 
#             and the keyword to decode this message is friends
# 
# 


def vigenere_decoder(cipher_text, keyword):
    letter_pointer = 0
    keyword_final = ''
    for i in range(0,len(cipher_text)):
        if cipher_text[i] in punctuation:
            keyword_final += cipher_text[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1)%len(keyword)
#             print(keyword_final)
    plain_text = ''
    for i in range(0,len(cipher_text)):    
        if not cipher_text[i] in punctuation:
            ln = alphabet.find(cipher_text[i]) - alphabet.find(keyword_final[i])
            plain_text += alphabet[ln % 26]
        else:
            plain_text += cipher_text[i]
    return plain_text

# message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
# keyword = "friends"
message = "keto cookies"
keyword = "hbar"
print(vigenere_decoder(message, keyword))

# Send a message with the  Vigenère Cipher



def vigenere_encoder(plain_text, keyword):
    letter_pointer = 0
    keyword_final = ''
    for i in range(0,len(plain_text)):
        if plain_text[i] in punctuation:
            keyword_final += plain_text[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1)%len(keyword)
    cipher_text = ''
    for i in range(0,len(plain_text)):    
        if plain_text[i] not in punctuation:
            ln = alphabet.find(plain_text[i]) + alphabet.find(keyword_final[i])
            cipher_text += alphabet[ln % 26]
        else:
            cipher_text += plain_text[i]
    return cipher_text

message_for_v = "keto cookies"
keyword = "hbar"

print(vigenere_encoder(message_for_v,keyword))
print(vigenere_decoder(vigenere_encoder(message_for_v, keyword), keyword))

