
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
