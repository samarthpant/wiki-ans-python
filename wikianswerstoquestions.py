# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 01:49:46 2019

@author: 500052370
"""

import wikipedia

while True:
    inp=input("Question to be asked:")
    #wikipedia.set_lang("es")  #set the output lang to spansih
    ans=wikipedia.summary(inp,sentences=2) #wikipedia answer to the question(only first4 sentences)
    
    print(ans)