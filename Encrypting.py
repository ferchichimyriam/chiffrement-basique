def caesar(text, shift, mode):
   
# text is what we want to decrypt or encrypt.
# shift is how much we want to shift the letter, can't really explain without showing but basically if we want to encrypt the letter C by moving from 3 letter we'll get F, hope it makes sense...
# mode is whether we want to encrypt or decrypt (for decryption we assume we know the shift and we're just lazy to decrypt it ourselves).

   result = ""

# empty string in which we will put our final output, basic.
   
   for char in text:
       if char.isalpha():
           
# for each character in the text, if the character is a letter...
           
           if char.isupper():
               base = ord('A')
           else:
               base = ord('a')
               
# we check if it's upper or lower, then we set the base to either, the ASCII value of 'A' (65) or 'a' (97).
               
           if mode.lower() == 'encrypt': # in case some idiots type "ENCRYPT" instead of "encrypt".
               direction = shift
           else:
               direction = -shift
               
# basically here, what we're trying to do is to see wether we go "backward" (in case of decrypting), or "forward" (in case of encrypting), if we encrypt C we go forward and we get F, otherwise, we go backward and we get A.
               
           calcul = (ord(char) - base + direction)%26
            
# Okay so this part is tricky, we play with the ASCII values, basically if we have ord("C"), it will give us 67 then we substract it to the base (the base being ord("A"))
# So from here we have the value "2", same value that we add (or substract, considering the mode we chose, but let's pretend we want to encrypt) the shift (let's say 3 in our exercice)
# This give us a total of 5 which is the position of an invisible character but just you wait...! Also! We put everything at modulo 26 to ensure it doesn't go higher than 25 (for example if we choose Z and the shift is 5, we'd get a problem without %26)
            
           result += chr(base+calcul)
# This is where our 5 comes in play! We say that chr(5) wouldn't give us anything, but if we add it to the base, then suddenly we get 5+65..which you guessed, give us 70. now if you print(chr(70)), you get F :-)
       else:
           result += char
            
   return result
            
print(caesar('Miaou', 3, 'encrypt'))

# This is literally a beginner project..(sort of.. I tried to make it understandable..), so yeah, don't go around using this for real word use..
# But at the end of the day, all you need to know is that playing with ASCII values is complicated but extremely useful!!


# if you ever need to check all the ASCII characters you can just do this function:
# for i in range(128):
#     print(f"{i} -> {chr(i)}")

# feel free to correct my code if needed, this is a public code and I aim to help beginner understands!