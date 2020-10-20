# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 17:09:50 2020

@author: Saraswati
"""
n=int(input()) # input how many socks
list1=[] # for storing socks color

# input each socks color
for i in range(n):
    r=int(input()) 
    list1.append(r);
    
dict1={} # for storing each unique color socks

# counting number of socks of unique color
for each in list1:
    if each not in dict1:
        dict1[each]=1
    else:
        dict1[each]=dict1[each]+1
        
print(dict1) # display number of socks of unique color

# counting number of paired socks
paired_socks=0
for key in dict1:
    paired_socks=paired_socks+dict1[key]//2
    
print('Total paired socks=', paired_socks) #display number of paired socks