#simple solution 

def isAnagram1(str1,str2):
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()

    return sorted(str1) == sorted(str2)

# solution interviewer looking for by appying the logic
def isAnagram2(str1,str2):
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()
    
    if len(str1) != len(str2):
        return False
    
    count1 = {}
    count2 = {}
    
    for letter in str1:
        if letter in count1:
            count1[letter] += 1
        else:
            count1[letter] = 1
            
    for letter in str2:
        if letter in count2:
            count2[letter] += 1
        else:
            count2[letter] = 1
    
    return count1 == count2


