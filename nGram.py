import nltk
import random
from nltk.corpus import brown
from decimal import *

news = brown.sents(categories='editorial')
global MAX
MAX = 10#len(news) #number of sentences to be processed

def uG():
    global uniCounter   #counts repeats of uniGrams
    global uniGram      #dictionary of biGrams
    global uniGrams     #counts biGrams
    uniCounter = {}
    uniGram = []
    uniGrams = 0

        
    news = brown.sents(categories='editorial')
        
    for x in range (1, MAX, 1):
        
        sent = news[x]
        sent.append('</s>')    #ending sentences with '</s>'
        sent.insert(0, '<s>')  #beginning sentences with '<s>'
        
        for x in range (0,sent.count('.')+1,1):
            try:
                sent.remove('.')   #removing .'s
            except:
                pass
        for x in range (0,sent.count(',')+1,1):
            try:
                sent.remove(',')   #removing ,'s
            except:
                pass
        for x in range (0,sent.count("'")+1,1):
            try:
                sent.remove("'")   #removing ''s
            except:
                pass
        for x in range (0,sent.count('"')+1,1):
            try:
                sent.remove('"')   #removing ''s
            except:
                pass
        x = 0
        for word in sent:
            word = word.lower()  #making all letters lowercase
            sent[x] = word       #so differences dont occur when
            x = x+1              #they shouldn't

        value = '1'
        for x in range (0,len(sent),1):
            try:
                word = sent[x]
                if(word not in uniGram):
                    uniGram.append(word)
                    uniGrams = uniGrams + 1
                if (word in uniCounter):
                    value = uniCounter[word]
                    value = value + 1
                    uniCounter[word] = value
                else:
                    uniCounter[word] = 1
            except:
                    pass
            
    #print uniCounter
    #print uniGram
    #print uniGrams

def genuniGram():
    
    x = 0
    randomuniGrams = ''
    count = 0
    word = "<s>"
    randomuniGrams = str.join(' ', (randomuniGrams, word))
    while (count < 3):
        if (word != '<s>'):
            randomuniGrams = str.join(' ', (randomuniGrams, word))
        rando = random.randint(0, uniGrams-1) #pick random number
        #print rando, len(valueList)
        word = uniGram[rando]
        #print word
        if (word == '</s>'):  #append until end of sentence
            randomuniGrams = str.join(' ', (randomuniGrams, word))
            count = count + 1 #if end, start new sentence
            word = '<s>'
            if(count < 3):
                randomuniGrams = str.join(' ', (randomuniGrams, word))
            
    print randomuniGrams

############################################################################
    
def bG():
    global biCounter    #counts repeats of biGrams
    global biGramArray  #makes dict of bigrams but with multiple values
                        #assigned if the first word in a biGram has multiple
                        #possible second words
    global biGrams      #counts biGrams
    global biGram       #dictionary of biGrams
    biGram = {}
    biCounter = {}
    biGramArray = {}
    biGrams = 0
  
    news = brown.sents(categories='editorial')

    for x in range (1, MAX, 1):

        sent = news[x]
        sent.append('</s>')     #ending sentences with '</s>'
        sent.insert(0, '<s>')   #beginning sentences with '<s>'
        
        for x in range (0,sent.count('.')+1,1):
            try:
                sent.remove('.')   #removing .'s
            except:
                pass
        for x in range (0,sent.count(',')+1,1):
            try:
                sent.remove(',')   #removing ,'s
            except:
                pass
        for x in range (0,sent.count("'")+1,1):
            try:
                sent.remove("'")   #removing ''s
            except:
                pass
        for x in range (0,sent.count('"')+1,1):
            try:
                sent.remove('"')   #removing "'s
            except:
                pass

            
        x = 0
        for word in sent:        #making all letters lowercase
            word = word.lower()  #so differences dont occur when
            sent[x] = word       #they shouldn't
            x = x+1
            
        for x in range (0,len(sent),1):    #for each sentence
            try:
                if sent[x] in biGramArray:
                    biGramArray[sent[x]].append(sent[x+1])   #if word already
                else:                                        #in array add to value
                    biGramArray[sent[x]] = [sent[x+1]]       #if not make it value
                    
                biGram[sent[x]] = sent[x+1]    #make bigram
                biGrams = biGrams + 1          #increase count
                concat = str.join('-', (sent[x], sent[x+1]))
                if (concat in biCounter):
                    value = biCounter[concat]
                    value = value + 1
                    biCounter[concat] = value
                else:
                    biCounter[concat] = 1
            except:
                    pass

    print biGramArray
    #print biGram.keys()
    #print biGram.values()
    #print biCounter
    #print biGram




#must run bG() before genbiGram()
def genbiGram():
    randombiGrams = ''
    count = 0
    valueList = []
    word = '<s>'
    valueList = biGramArray[word]
    
    while(count < 3):    #generate three sentences
        #print biGramArray[word]
        randombiGrams = str.join(' ', (randombiGrams, word))
        valueList = biGramArray[word]
        rando = random.randint(0, len(valueList)-1) #pick random number
        #print rando, len(valueList)
        word = valueList[rando]
        #print word
        if (word == '</s>'):  #append until end of sentence
            randombiGrams = str.join(' ', (randombiGrams, word))
            count = count + 1 #if end, start new sentence
            word = '<s>'
        
    print randombiGrams

#usage findbiProb("but a")
def findbiProb(phrase):
    words = []
    x = 1
    words = phrase.split()
    num = 0
    try:
        num = biCounter.get(str.join('-', (words[0], words[1])))
    except:
        pass
    getcontext().prec = 9
    print num, "in", biGrams
    getcontext().prec = 9
    try:
        rat = Decimal(num)/Decimal(biGrams)
        print "Probability of sequence =", Decimal(rat)
    except:
        pass

#############################################################################    

def tG():
    global triCounter    #counts repeats of triGrams
    global triGramArray  #makes dict of triGrams but with multiple values
                         #assigned if the first word in a triGram has multiple
                         #possible third words
    global triGrams      #counts triGrams
    global triGram       #dictionary of triGrams
    triGram = {}
    triCounter = {}
    triGramArray = {}
    triGrams = 0
  
    news = brown.sents(categories='editorial')

    for x in range (1, MAX, 1):

        sent = news[x]
        sent.append('</s>')     #ending sentences with '</s>'
        sent.insert(0, '<s>')   #beginning sentences with '<s>'
        
        for x in range (0,sent.count('.')+1,1):
            try:
                sent.remove('.')   #removing .'s
            except:
                pass
        for x in range (0,sent.count(',')+1,1):
            try:
                sent.remove(',')   #removing ,'s
            except:
                pass
        for x in range (0,sent.count("'")+1,1):
            try:
                sent.remove("'")   #removing ''s
            except:
                pass
        for x in range (0,sent.count('"')+1,1):
            try:
                sent.remove('"')   #removing ''s
            except:
                pass
            
        x = 0
        for word in sent:        #making all letters lowercase
            word = word.lower()  #so differences dont occur when
            sent[x] = word       #they shouldn't
            x = x+1
            
        for x in range (0,len(sent)-1,1):
            try:
                triGrams = triGrams + 1
                concat = str.join('-', (sent[x], sent[x+1]))
                triGram[concat] = sent[x+2]
                
                if concat in triGramArray:
                    triGramArray[concat].append(sent[x+2])
                else:
                    triGramArray[concat] = [sent[x+2]]
                    
                concat = str.join('-', (concat, sent[x+2]))
                if (concat in triCounter):
                    value = triCounter[concat]
                    value = value + 1
                    triCounter[concat] = value
                else:
                    triCounter[concat] = 1
            except:
                pass

    print triGramArray
    #print triGram.keys()
    #print triGram.values()
    #print triCounter
    #print triGram




#must run bG() and tG() before gentriGram()
def gentriGram():
    rondomtriGrams = ''
    count = 0
    valueList = []
    word1 = '<s>'
    valueList = biGramArray[word1]
    rando = random.randint(0, len(valueList)-1) #pick random number
    #print rando, len(valueList)
    word2 = valueList[rando]
    #print word2
    word = str.join('-', (word1, word2))
    #print word
    
    randomtriGrams = str.join(' ', (word1, word2))
    while(count < 3):    #generate three sentences
        #print triGramArray[word]
        valueList = triGramArray[word]
        rando = random.randint(0, len(valueList)-1) #pick random number
        #print rando, len(valueList)
        word1 = word2
        word2 = valueList[rando]
        word = str.join('-', (word1, word2))
        #print word
        randomtriGrams = str.join(' ', (randomtriGrams, word2))
        if (word2 == '</s>'):  #append until end of sentence
            count = count + 1 #if end, start new sentence
            word1 = '<s>'
            if( count < 3):
                randomtriGrams = str.join(' ', (randomtriGrams, word1))
            valueList = biGramArray[word1]
            rando = random.randint(0, len(valueList)-1) #pick random number
            word2 = valueList[rando]
            word = str.join('-', (word1, word2))


            
            
            
        
    print randomtriGrams
#usage findtriProb("but a way")
def findtriProb(phrase):
    words = []
    x = 1
    words = phrase.split()
    num = 0
    try:
        num = triCounter.get(str.join('-', (words[0], words[1], words[2])))
    except:
        pass
    getcontext().prec = 9
    print num, "in", triGrams
    getcontext().prec = 9
    try:
        rat = Decimal(num)/Decimal(triGrams)
        print "Probability of sequence =", Decimal(rat)
    except:
        pass

###########################################################################

def qG():
    global quadCounter    #counts repeats of quadGrams
    global quadGramArray  #makes dict of quadGrams but with multiple values
                          #assigned if the first word in a quadGram has multiple
                          #possible fourth words
    global quadGrams      #counts quadGrams
    global quadGram       #dictionary of quadGrams
    quadGram = {}
    quadCounter = {}
    quadGramArray = {}
    quadGrams = 0
  
    news = brown.sents(categories='editorial')

    for x in range (1, MAX, 1):

        sent = news[x]
        sent.append('</s>')     #ending sentences with '</s>'
        sent.insert(0, '<s>')   #beginning sentences with '<s>'
        
        for x in range (0,sent.count('.')+1,1):
            try:
                sent.remove('.')   #removing .'s
            except:
                pass
        for x in range (0,sent.count(',')+1,1):
            try:
                sent.remove(',')   #removing ,'s
            except:
                pass
        for x in range (0,sent.count("'")+1,1):
            try:
                sent.remove("'")   #removing ''s
            except:
                pass
        for x in range (0,sent.count('"')+1,1):
            try:
                sent.remove('"')   #removing ''s
            except:
                pass
            
        x = 0
        for word in sent:        #making all letters lowercase
            word = word.lower()  #so differences dont occur when
            sent[x] = word       #they shouldn't
            x = x+1
                
        for x in range (0,len(sent)-1,1):
            try:
                quadGrams = quadGrams + 1
                concat = str.join('-', (sent[x], sent[x+1], sent[x+2]))
                quadGram[concat] = sent[x+3]
                
                if concat in quadGramArray:
                    quadGramArray[concat].append(sent[x+3])
                else:
                    quadGramArray[concat] = [sent[x+3]]
                    
                concat = str.join('-', (concat, sent[x+3]))
                if (concat in quadCounter):
                    value = quadCounter[concat]
                    value = value + 1
                    quadCounter[concat] = value
                else:
                    quadCounter[concat] = 1
            except:
                pass

    #print quadGramArray
    #print quadGram.keys()
    #print quadGram.values()
    #print quadCounter
    #print quadGram


#must run bG(), tG() and qG() before gentriGram()
def genquadGram():
    rondomquadGrams = ''
    count = 0
    valueList = []
    word1 = '<s>'
    valueList = biGramArray[word1]
    rando = random.randint(0, len(valueList)-1) #pick random number
    #print rando, len(valueList)
    word2 = valueList[rando]
    #print word2
    word = str.join('-', (word1, word2))
    #print word
    valueList = triGramArray[word]
    rando = random.randint(0, len(valueList)-1) #pick random number
    #print rando, len(valueList)
    word3 = valueList[rando]
    randomquadGrams = str.join(' ', (word1, word2, word3))
    word = str.join('-', (word1, word2, word3))
    #print word
    
    while(count < 3):    #generate three sentences
        #print quadGramArray[word]
        valueList = quadGramArray[word]
        rando = random.randint(0, len(valueList)-1) #pick random number
        #print rando, len(valueList)
        word1 = word2
        word2 = word3
        word3 = valueList[rando]
        word = str.join('-', (word1, word2, word3))
        #print word
        randomquadGrams = str.join(' ', (randomquadGrams, word3))
        if (word3 == '</s>'):  #append until end of sentence
            count = count + 1 #if end, start new sentence
            word1 = '<s>'
            if(count < 3):
                randomquadGrams = str.join(' ', (randomquadGrams, word1))
            valueList = biGramArray[word1]
            rando = random.randint(0, len(valueList)-1) #pick random number
            word2 = valueList[rando]
            word = str.join('-', (word1, word2))
            valueList = triGramArray[word]
            rando = random.randint(0, len(valueList)-1) #pick random number
            #print rando, len(valueList)
            word3 = valueList[rando]
            word = str.join('-', (word1, word2, word3))
        
    print randomquadGrams

#usage findquadProb("performed in an atmosphere")
def findquadProb(phrase):
    words = []
    x = 1
    words = phrase.split()
    num = 0
    try:
        num = quadCounter.get(str.join('-', (words[0], words[1], words[2], words[3])))
    except:
        pass
    getcontext().prec = 9
    #print words
    print num, "in", quadGrams
    getcontext().prec = 9
    try:
        rat = Decimal(num)/Decimal(quadGrams)
        print "Probability of sequence =", Decimal(rat)
    except:
        pass

    

