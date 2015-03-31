#! /usr/bin/env python3

import nltk
from  urllib.request import urlopen
from  urllib.request import URLError
from bs4 import BeautifulSoup
import re
import random
from wordnik import *

### starting wordnik API ###

apiUrl = 'http://api.wordnik.com/v4'
apiKey = 'f4581649e01134254d6c3259d6607bfb6c3ef144f0deba6ec'
client = swagger.ApiClient(apiKey, apiUrl)
wordApi = WordApi.WordApi(client)

###

### main chatbot class ###

class Minerva(object):
    def __init__(self):
        self.name = 'Minerva'
        #build this out through conversations and store it in some memory file
        self.interests = []
        self.disinterests = []
        self.user_memory_dict = {1: 'first user memory', 2: 'second user memory'}

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

###

### helping functions ###

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
    #print (tagged)
    count = 1
    for item in tagged:
        if item[1] == 'NN' or item[1] == 'NNS':
            #print ('item[0] is ')
            #print (str(count) + 'noun is: ')
            count += 1
            nouns.append(item[0])
    return nouns

def stripAllTags( html ):
    if html is None:
        return None
    return ''.join(BeautifulSoup(html).findAll(text = True))

###

### primary function to run Miss M ###

def run_minerva():
    print ('*** Just type "goodbye" in order to quit\n')
    print ('Hello there! What is on your mind?\n')
    while (1<2):
        user_input = input()
        if user_input == 'goodbye' or user_input == 'bye':
            print("So long! I'll miss you!")
            break
        else:
            nouns = build_noun_list(user_input)
            #print ('')
            #print ('the nouns list')
            #print (nouns)
            #print ('')
            #print ('you used ' + str(len(nouns)) + ' nouns')
            if len(nouns) > 0:
                #soup = soupify_url('http://dictionary.reference.com/browse/' + nouns[0]) 
                #dndata_tags = soup.findAll('div',{'class':'dndata'})
                #print(dndata_tags)
                definitions = wordApi.getDefinitions(nouns[0])
                def1 = definitions[0].text
                #text = dndata_tags[0]
                print ('Did you know that ' + nouns[0] + ' is ' + str(def1))
                print('')
                example_results = wordApi.getExamples(nouns[0])
                chosen_example = random.choice(example_results.examples)
                print(chosen_example.text)
                print('')
            else:
                print('Oh yeah? Tell me more!\n')
            #print ('you said: ' + user_input)

###

### calling Madam M ###

def main(argv=None):
    run_minerva()

if __name__ == "__main__":
    main()

###
