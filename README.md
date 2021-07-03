# Ciphers
A compolation of cipher algorithms in different languages

## Ceasars Cipher (Mono-alphabatic, symetric)

This is a classic cipher called a Caesar Cipher. The cesaar cipher.
You take your message, something like "hello" and then you shift all 
of the letters by a certain offset. For example, chose an offset of 3 
and a message of "hello". Code the message by shifting each letter 3 
places to the left (with respect to the alphabet). So "h" becomes "e",
"e" becomes, "b", "l" becomes "i", and "o" becomes "l". Then the coded message is "ebiil"

## Vigenere Cipher (Polyalphabetic, Symetric)

Unvented by an Italian cryptologist named Giovan Battista Bellaso in the 16th century, but named after another cryptologist from the 16th century, Blaise de Vigenère.
            
The Vigenère Cipher is a polyalphabetic substitution cipher, as opposed to the Caesar Cipher which was a monoalphabetic substitution cipher. What this means is that opposed to having a single shift that is applied to every letter, the Vigenère Cipher has a different shift for each individual letter. The value of the shift for each letter is determined by a given keyword.

Consider the message

barry is the spy
If we want to code this message, first we choose a keyword. For this example, we'll use the keyword
dog
Now we use the repeat the keyword over and over to generate a keyword phrase that is the same 
length as the message we want to code. So if we want to code the message "barry is the spy" our _keyword phrase_ is 
"dogdo gd ogd ogd". Now we are ready to start coding our message. We shift the each letter of our message 
by the place value of the corresponding letter in the keyword phrase, assuming that "a" has a place value of 
0, "b" has a place value of 1, and so forth.

                         message:       b  a  r  r  y    i  s   t  h  e   s  p  y
                 
                  keyword phrase:       d  o  g  d  o    g  d   o  g  d   o  g  d
                  
           resulting place value:       4  14 15 12 16   24 11  21 25 22  22 17 5
       
So we shift "b", which has an index of 1, by the index of "d", which is 3. This gives us an place value of 4, which is "e". Then continue the trend: we shift "a" by the place value of "o", 14, and get "o" again, we shift "r" by the place value of "g", 15, and get "x", shift the next "r" by 12 places and "u", and so forth. Once we complete all the shifts we end up with our coded message:             

    eoxum ov hnh gvb
                
As you can imagine, this is a lot harder to crack without knowing the keyword.


## RSA

## DSA

## Elliptic Curve
