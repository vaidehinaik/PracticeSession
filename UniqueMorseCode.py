def uniqueMorseCode(words):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    f_list = []
    for word in words:
        temp = []
        for letter in word.lower():
            o = ord(letter)
            temp.append(morse[o-97])
            # print(temp)
        f_list.append(''.join(temp))
        # print("The final_list is :{}".format(f_list))
    return len(set(f_list))
print("The different transformations are: {}".format(uniqueMorseCode(["gin","gig","msg","zen"])))




