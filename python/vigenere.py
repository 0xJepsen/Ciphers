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
