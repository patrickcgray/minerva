import nltk
from  urllib.request import urlopen
from  urllib.request import URLError
from bs4 import BeautifulSoup
import re
import random

class Minerva(object):
    def __init__(self):
        self.name = 'Minerva'
        #build this out through conversations and store it in some memory file
        self.interests = []
        self.disinterests = []
        self.user_memory_dict = {1: 'first user memory', 2: 'second user memory'}

    def method_a(self, foo):
        print (self.x + ' ' + foo)

    def choose_interest(self):
        if self.interests:
            print(random.choice(self.interests))
        else:
            print (None)
    def choose_disinterest(self):
        if self.disinterests:
            print(random.choice(self.disinterests))
        else:
            print (None)

    #def add_to_user_memory(self, user_id, data_to_add)


def soupify_url(url):
    try:
        html = urlopen(url).read()
    except URLError:
        print ("error in soupifying")
        return 
    except ValueError:
        print ("error in soupifying")
        return
    except httplib.InvalidURL:
        print ("error in soupifying")
        return
    except httplib.BadStatusLine:
        print ("error in soupifying")
        return
            
    return BeautifulSoup(html) 

def build_noun_list(input_string):
    tokens = nltk.word_tokenize(input_string)
    tagged = nltk.pos_tag(tokens)
    nouns = []
    print (tagged)
    count = 1
    for item in tagged:
        if item[1] == 'NN' or item[1] == 'NNS':
            print ('item[0] is ')
            print (str(count) + 'noun is: ')
            count += 1
            nouns.append(item[0])
    return nouns

def stripAllTags( html ):
    if html is None:
        return None
    return ''.join(BeautifulSoup(html).findAll(text = True))

def mainMinerva():
    print ('Ask or tell me something por favor')
    print ('*** Just type "exit" in order to quit')
    while (1<2):
        user_input = input("Type here: ")
        if user_input == 'exit':
            break
        else:
            nouns = build_noun_list(user_input)
            print ('')
            print ('the nouns list')
            print (nouns)
            print ('')
            print ('you used ' + str(len(nouns)) + ' nouns')
            if len(nouns) > 0:
                soup = soupify_url('http://dictionary.reference.com/browse/' + nouns[0]) 
                dndata_tags = soup.findAll('div',{'class':'dndata'})
                print(dndata_tags)
                text = dndata_tags[0]
                print ('I find ' + nouns[0] + ' most interesting. Did you know that they are ' + re.sub('<[^<]+?>', '', str(text)))
                
            if 'who' or 'what' or 'when' or 'where' or 'why' or 'how' in user_input:
                print ('you asked a question')
            
            print ('you said: ' + user_input)

mainMinerva()
