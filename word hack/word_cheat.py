'''
    Journal at Dee's
    Day 1- 6:45 am   18th April 2022

    I wrote this piece of code to solve word puzzle. Currently it can solve 3 and 4 word puzzles.
    I am still trying to improve it to solve 5 and 6 at max. Hopefully i can do it.

    INSTRUCTIONS
    You provide the letters given 

    HOW THE ALGORITHM WORKS
    1.After giving it the letters, It finds combinations of those letters and
    stores it in the #comb list
    2.It filters out words with non duplicate letters and stores
    into a new list #new_comb 
    3.It then compares the new_comb with a list of all words from the nltk library to find a match

    CONS
    It is 98%% effecient since i currently have a list of 273K words as compared to 400k plus words
    which native speakers use.



'''

from time import sleep
from nltk.corpus import words
import nltk
from time import sleep


#given letters
letters = []
comb= []
#get list of words
#nltk.download('words')
all_words= words.words()

#find match 3 letter words 6,8,12,16,20,22

def find_combination3(letters):    
    comb=[]
    for i in letters:
        for j in letters:
            for k in letters:
                comb.append(i+j+k)
                
    #filter comb to remove duplicates
    new_comb=[]
    new_comb.append(comb[5])
    new_comb.append(comb[7])
    new_comb.append(comb[11])
    new_comb.append(comb[15])
    new_comb.append(comb[19])
    new_comb.append(comb[21])

    #check for word
    #print(comb)
    #print(new_comb)
    print(set(comb).intersection(all_words))


def find_combination4(letters):   
    comb=[] 
    for i in letters:
        for j in letters:
            for k in letters:
                for m in letters:
                    
                    
                    comb.append(i+j+k+m)
    
    #for idx,i in enumerate(comb):
    #    print(str(idx)+i)
        
            
    #filter comb to remove duplicates
    new_comb=[]
    new_comb.append(comb[27])
    new_comb.append(comb[30])
    new_comb.append(comb[39])
    new_comb.append(comb[45])
    new_comb.append(comb[54])
    new_comb.append(comb[57])
    new_comb.append(comb[75])
    new_comb.append(comb[78])
    new_comb.append(comb[97])
    new_comb.append(comb[99])
    new_comb.append(comb[108])
    new_comb.append(comb[114])
    new_comb.append(comb[120])
    new_comb.append(comb[135])
    new_comb.append(comb[141])
    new_comb.append(comb[147])
    new_comb.append(comb[156])
    new_comb.append(comb[177])
    new_comb.append(comb[180])
    new_comb.append(comb[198])
    new_comb.append(comb[201])
    new_comb.append(comb[210])
    new_comb.append(comb[216])
    new_comb.append(comb[225])

    #check for word
    #print(comb)
    #print(new_comb)
    print(set(comb).intersection(all_words))


def find_combination5(letters):   
    comb=[] 
    for i in letters:
        for j in letters:
            for k in letters:
                for m in letters:
                    for n in letters:
                        comb.append(i+j+k+m+n)
    

    #check for word
    #print(comb)
    #print(new_comb)
    print(set(comb).intersection(all_words))




def find_combination6(letters):   
    comb=[] 
    for i in letters:
        for j in letters:
            for k in letters:
                for m in letters:
                    for n in letters:
                        for o in letters:
                            comb.append(i+j+k+m+n+o)
    

    #check for word
    #print(comb)
    #print(new_comb)
    print(set(comb).intersection(all_words))


#app
given = input("Please input letters:   ")
for i in given:
    letters.append(i)

if len(given) == 3:
    find_combination3(letters)
elif len(given) == 4:
    find_combination4(letters)
elif len(given) == 5:
        find_combination5(letters)
elif len(given) == 6:
    find_combination6(letters)


sleep(2)
 


