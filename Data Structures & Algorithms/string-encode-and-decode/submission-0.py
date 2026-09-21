class Solution:
    #you are going ot have the lenght of the word stored and then uare     going to go thru that and then code will realize the next word is staritng bc the length of the word will end and the next words length will be written down. 
#For every string, I would store its length, add a separator, and then add the string itself.
#length → separator → string
#I would read the length, use it to know how many characters to take, then repeat until I’ve gone through the entire encoded string.

#encoded = ""

#for every word:
 #   find the length
  #  turn length into a string
   # create: length + ":" + word
    #add that piece to encoded

#return encoded

#decodingg
#While the current character is NOT :, keep moving forward.
#1. Start at i
#2. Read until ":"
#3. Everything before ":" = length
#4. Move i past ":"
#5. Grab length characters
#6. Add that word to your result
#7. Repeat

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for word in strs: 
            length = str(len(word))
            new = length + ":" + word 
            encode += new
        return encode

    def decode(self, s: str) -> List[str]:
        i = 0
        result = [] #dont forget to initialize 

        while i < len(s):
            start = i

            while s[i] != ":":
                i+=1
            
            length = int(s[start:i])
            i+=1
                
            word = s[i:i+length]
            result.append(word)
            i += length
                
        return result
