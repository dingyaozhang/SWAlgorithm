#!/usr/bin/python
__author__ = "FirstName LastName"
__email__ = "first.last@yale.edu"
__copyright__ = "Copyright 2021"
__license__ = "GPL"
__version__ = "1.0.0"

### Usage: python hw1.py -i <input file> -s <score file>
### Example: python hw1.py -i input.txt -s blosum62.txt
### Note: Smith-Waterman Algorithm

import argparse
import pandas as pd
import numpy as np



### Implement your Smith-Waterman Algorithm
def runSW(inputFile, scoreFile, openGap, extGap):
    ### calculation
    ### write output
    pairmat = pd.read_csv(scoreFile,delim_whitespace=True) # datamat.loc['A','A']

    
    inputdata = pd.read_table(inputFile, header = None)
    seq1 = np.array(inputdata)[0][0]
    seq2 = np.array(inputdata)[1][0]




    print("-----------\n|Sequences|\n-----------\nsequence1")
    print(seq1)
    print("sequence2")
    print(seq2)
    print("--------------\n|Score Matrix|\n--------------")

    
    len1 = len(seq1)+1
    len2 = len(seq2)+1

    #score matrix 
    score_matrix = np.zeros([len1,len2])

    #matrix keeps the trace for traceback
    frommat = pd.DataFrame(score_matrix).astype(object)
    for i in range(frommat.shape[0]):
        for j in range(frommat.shape[1]):
            frommat.iloc[i,j] = []


    #build score matrix 
    for i in range(len1-1):
        i = i+1
        for j in range(len2-1):
            j = j+1
            scoretemp = np.array([])
            
            #diagonal match score
            scoretemp = np.append(scoretemp, pairmat.loc[seq1[i-1],seq2[j-1]] + score_matrix[i-1,j-1]) 
            
            #i j gap score
            inums = np.array(range(i))
            jnums = np.array(range(j))
            iscores = score_matrix[inums,j] + (extGap*(np.flip(inums)) + openGap)
            jscores = score_matrix[i,jnums] + (extGap*(np.flip(jnums)) + openGap)
            scoretemp = np.append(scoretemp, iscores)
            scoretemp = np.append(scoretemp, jscores)
            
            #each previous location
            posi = np.array([i-1])
            posi = np.append(posi, inums)
            posi = np.append(posi, np.zeros(j)+i).astype(int)
            posj = np.array([j-1])
            posj = np.append(posj, np.zeros(i)+j)
            posj = np.append(posj, jnums).astype(int)
            posorder = np.array(-1)
            posorder = np.append(posorder, np.array(range(i)))
            posorder = np.append(posorder, np.array(range(j)))
            posorder = np.argsort(posorder)
            scoretemp = scoretemp[posorder]
            posi  = posi[posorder]
            posj  = posj[posorder]

            # finish score matrix & build traceback matrix 
            maxvalue = np.max(scoretemp)
            if maxvalue > 0:
                score_matrix[i,j] = maxvalue
                maxwhere = np.where(scoretemp == maxvalue)[0]
                alist = list()
                for x in range(maxwhere.shape[0]):
                    x = maxwhere[x]
                    alist.append([posi[x], posj[x]])
                frommat.iloc[i,j] = alist
                
            else:
            	frommat.iloc[i,j] = []

    
    #display the score matrix and alignment result
    show_score_matrix = pd.DataFrame(score_matrix)
    show_score_matrix.index    = np.append('',list(map(str, seq1)))
    show_score_matrix.columns  = np.append('',list(map(str, seq2)))
    show_score_matrix = show_score_matrix.applymap(lambda x: str(int(x)) if abs(x - int(x)) < 1e-6 else str(round(x,2)))
    show_score_matrix = show_score_matrix.T
    finalmax = np.max(score_matrix).astype("int64")
    print(show_score_matrix.to_csv(sep = '\t'),end='')
    print("----------------------\n|Best Local Alignment|\n----------------------")
    outputtemp1 = 'Alignment Score:' + str(finalmax)
    print(outputtemp1)
    print("Alignment Results:")

    #traceback process using a traceback function
    
    score_place = np.where(score_matrix==finalmax)
    score_place0 = score_place[0]
    score_place1 = score_place[1]
    for placei in range(score_place0.shape[0]):
        place0 = score_place0[placei]
        place1 = score_place1[placei]
        
        iniline1 = ')'
        iniline2 = ' '
        iniline3 = ')'
        for ci in range(np.max([len(seq1[place0:]), len(seq2[place1:])])):
            if ci+1 <= len(seq1[place0:]):
                iniline1 = iniline1 + seq1[place0+ci]
            else:
                iniline1 = iniline1 + ' '
            iniline2 = iniline2 + ' '
            if ci+1 <= len(seq2[place1:]):
                iniline3 = iniline3 + seq2[place1+ci]
            else:
                iniline3 = iniline3 + ' '

        tracemat(score_matrix, frommat, place0, place1, seq1, seq2, iniline1, iniline2, iniline3) #[::-1]

#traceback function
def tracemat(score_matrix, frommat, i, j, seq1, seq2, line1, line2, line3):
    if len(frommat.iloc[i,j]) == 0:

        tiniline1 = ''
        tiniline2 = ''
        tiniline3 = ''
        tempseq1 = seq1[0:i][::-1]
        tempseq2 = seq2[0:j][::-1]
        for ci in range(np.max([len(tempseq1), len(tempseq2)])):
            if ci+1 <= len(tempseq1):
                tiniline1 = tempseq1[ci] + tiniline1 
            else:
                tiniline1 = ' ' + tiniline1 
            tiniline2 = ' ' + tiniline2 
            if ci+1 <= len(tempseq2):
                tiniline3 = tempseq2[ci] + tiniline3
            else:
                tiniline3 = ' ' + tiniline3
        line1 = tiniline1+'('+line1
        line2 = tiniline2+' '+line2
        line3 = tiniline3+'('+line3
        print(line1+'\n'+line2+'\n'+line3)
        #print("\n-----------------------------------------------------")
    else:

        indexlist = frommat.iloc[i,j]

        positionlistnum = len(indexlist)

        #for placei in range(positionlistnum):
            #place = indexlist[placei]
        if 1==1:
            placei = 0
            place = indexlist[placei]
            if place[0] == i:
                bases = j-place[1]
                line1 = '-'*bases + line1
                line2 = ' '*bases + line2
                line3 = seq2[place[1]:j] + line3
            elif place[1] == j:
                bases = i-place[0]
                line1 = seq1[place[0]:i] + line1
                line2 = ' '*bases + line2
                line3 = '-'*bases + line3
            else:
                line1 = seq1[i-1] + line1
                if seq1[i-1] == seq2[j-1]:
                    line2 = '|' + line2
                else:
                    line2 = ' ' + line2
                line3 = seq2[j-1] + line3
            tracemat(score_matrix,frommat, place[0], place[1], seq1, seq2, line1, line2, line3)

 