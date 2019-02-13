#!/usr/bin/env python
#=========================================================================
# This is OPEN SOURCE SOFTWARE governed by the Gnu General Public
# License (GPL) version 3, as described at www.opensource.org.
# Author: William H. Majoros (bmajoros@alumni.duke.edu)
#=========================================================================
from __future__ import (absolute_import, division, print_function, 
   unicode_literals, generators, nested_scopes, with_statement)
from builtins import (bytes, dict, int, list, object, range, str, ascii,
   chr, hex, input, next, oct, open, pow, round, super, filter, map, zip)
# The above imports should allow this program to run in both Python 2 and
# Python 3.  You might need to update your version of module "future".
import sys
import ProgramName
from Rex import Rex
rex=Rex()
from DataFrame import DataFrame

def getNonzeros(header,fields):
    n=len(fields)
    if(n!=len(header)): 
        raise Exception("length mismatch: "+str(n)+" vs "+str(len(header)))
    gene=fields[0]
    print(gene,"\t",sep="",end="")
    for i in range(1,n):
        x=fields[i]
        if(x=="0"): continue
        cell=header[i]
        print("\t",i,"=",x,sep="",end="")
    print()

def findGuides(df):
    for i in range(df.nrow()):
        row=df[i]
        if(rex.find("^chr",row.label)): return i

def sumColumn(df,col):
    nrow=df.nrow()
    s=0
    for i in range(nrow):
        s+=df[i][col]
    return s

#=========================================================================
# main()
#=========================================================================
if(len(sys.argv)!=2):
    exit(ProgramName.get()+" <infile.tx>\n")
(infile,)=sys.argv[1:]

df=DataFrame.readTable(infile)
df.toInt()
firstGuideIndex=findGuides(df)
#print(firstGuideIndex,df.nrow(),df.ncol())

#for i in range(df.nrow()):
#    print(df[i].length())
#exit()

ncol=df.ncol()
for i in range(ncol):
    colSum=sumColumn(df,i)
    print(colSum)

#with open(infile,"rt") as IN:
#    header=IN.readline()
#    header=header.rstrip().split()
#    for line in IN:
#        fields=line.rstrip().split()
#        getNonzeros(header,fields)


