#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:37:41 2019

@author: graceziegler
"""
#Student Number: 20064252
import random
import time 
#Create lists of sizes 500, 1000, 5000, 10000
#S1=500, S2=1000, S3=5000, S4=10,000

listS1 = [] 
#makes a list of 500 values, only the even values from 0 to 1000
for i in range (0, 1000, 2):
    listS1.append(i)

random.shuffle(listS1)

listS2 = []

for i in range(0, 2000, 2):
    listS2.append(i)
    
random.shuffle(listS2)

listS3 = []

for i in range(0, 10000, 2):
    listS3.append(i)

random.shuffle(listS3)

listS4 = [] 

for i in range(0, 20000, 2):
    listS4.append(i)
    
random.shuffle(listS4)

#createK will create a list, retrieving half its values from the specified list
#and add the equivalent amount of random values that are
#not in the specified list 

def createK(listS):
    listK = [] 
    i = 0
    #while the length of list k is less than or equal to
    #half of the list size, add items from the list S 
    while(len(listK) <= 24):
        listK.append(listS[i])
        i += 1
   
    #add the odd numbers from the range so that they are not
    #the same as the values from listS
    for num in range(0, 24):
        if num % 2 != 0:
            listK.append(num)
    
    random.shuffle(listK)

    
    return listK
    

#Algorithm A
#Linear Search
   
def algA(x, list):
    for i in range(len(list)):
        if(list[i] == x):
            return True

    return False

#Merge sort
    
#Merge sort
def mergeSort(list):
    if(len(list) > 1):
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        i = 0
        j = 0
        k = 0

        mergeSort(left)
        mergeSort(right)

        while(i < len(left) and j < len(right)):
            if(left[i] < right[j]):
                list[k] = left[i]
                i+=1

            else:
                list[k] = right[j]
                j+=1
            
            k+=1

        while(i < len(left)): 
            list[k] = left[i] 
            i+=1
            k+=1
          
        while(j < len(right)): 
            list[k] = right[j] 
            j+=1
            k+=1

        return list

    return 0
        
#Algorithm B, with binary search 
def algB(item, list):
    if(len(list) == 0):
        return False

    low = 0
    high = len(list)-1

    while(low <= high):
        mid = (low+high)//2

        if(item > list[mid]):
            low = mid+1 

        elif(item < list[mid]):
            high = mid-1

        else:
            return True

    return False    

def main(): 
 
    #define total times
    totTimeA500 = 0
    totTimeB500 = 0
    totTimeA1k = 0
    totTimeB1k = 0
    totTimeA5k = 0
    totTimeB5k = 0
    totTimeA10k = 0
    totTimeB10k = 0
    
    #make a k list for each value of n 
    listKS1 = createK(listS1)
    listKS2 = createK(listS2)
    listKS3 = createK(listS3)
    listKS4 = createK(listS4)
    
    #when n is 500
    while(totTimeA500 <= totTimeB500):
        startA = time.time()
        #loop through each value in the K list
        #search for it in the list n=500
        for i in range(0, len(listKS1)):
            algA(i, listS1)
            
        endA = time.time()
        
        sortList1 = mergeSort(listS1)
        startB = time.time()
        for i in range(0, len(listKS1)):
            algB(i, sortList1)
            
        endB = time.time()
        
        totTimeA500, totTimeB500 = (endA-startA), (endB-startB)
        
        if(totTimeA500 > totTimeB500):
            break
        
    print("When list S has 500 integers")
    #print("\n")
    print("Algorithm A: ")
    print(totTimeA500)
    #print("\n")
    print("Algorithm B: ")
    print(totTimeB500)
    #print("\n")
    print("the length of k is: ")
    print(len(listKS1))
    print("\n")
    
    #when n=1000
    while(totTimeA1k <= totTimeB1k):
        startA = time.time()
        #loop through each value in the K list
        #search for it in the list n=500
        for i in range(0, len(listKS2)):
            algA(i, listS2)
            
        endA = time.time()
        
        sortList2 = mergeSort(listS2)
        startB = time.time()
        for i in range(0, len(listKS2)):
            algB(i, sortList2)
            
        endB = time.time()
        
        totTimeA1k, totTimeB1k = (endA-startA), (endB-startB)
        
        if(totTimeA1k > totTimeB1k):
            break
        
    print("When list S has 1000 integers")
    #print("\n")
    print("Algorithm A: ")
    print(totTimeA1k)
    #print("\n")
    print("Algorithm B: ")
    print(totTimeB1k)
    #print("\n")
    print("the length of k is: ")
    print(len(listKS2))
    print("\n")
    
    while(totTimeA5k <= totTimeB5k):
        startA = time.time()
        #loop through each value in the K list
        #search for it in the list n=500
        for i in range(0, len(listKS3)):
            algA(i, listS3)
            
        endA = time.time()
        
        sortList3 = mergeSort(listS3)
        startB = time.time()
        for i in range(0, len(listKS3)):
            algB(i, sortList3)
            
        endB = time.time()
        
        totTimeA5k, totTimeB5k = (endA-startA), (endB-startB)
        
        if(totTimeA5k > totTimeB5k):
            break
        
    print("When list S has 5000 integers")
    #print("\n")
    print("Algorithm A: ")
    print(totTimeA5k)
    #print("\n")
    print("Algorithm B: ")
    print(totTimeB5k)
    #print("\n")
    print("the length of k is: ")
    print(len(listKS3))
    print("\n")
    
    while(totTimeA10k <= totTimeB10k):
        startA = time.time()
        #loop through each value in the K list
        #search for it in the list n=500
        for i in range(0, len(listKS4)):
            algA(i, listS4)
            
        endA = time.time()
        
        sortList4 = mergeSort(listS4)
        startB = time.time()
        for i in range(0, len(listKS4)):
            algB(i, sortList4)
            
        endB = time.time()
        
        totTimeA10k, totTimeB10k = (endA-startA), (endB-startB)
        
        if(totTimeA10k > totTimeB10k):
            break
        
    print("When list S has 10000 integers")
    #print("\n")
    print("Algorithm A: ")
    print(totTimeA10k)
    #print("\n")
    print("Algorithm B: ")
    print(totTimeB10k)
    #print("\n")
    print("the length of k is: ")
    print(len(listKS4))
    
    
    
    
main()
            
        
        
        
    
