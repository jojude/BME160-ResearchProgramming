#!/usr/bin/env python3
# Name: Jude Allen Joseph (jajoseph)
# Group Members: None

class NucParams:
    rnaCodonTable = {
    # RNA codon table
    # U
    'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C',  # UxU
    'UUC': 'F', 'UCC': 'S', 'UAC': 'Y', 'UGC': 'C',  # UxC
    'UUA': 'L', 'UCA': 'S', 'UAA': '-', 'UGA': '-',  # UxA
    'UUG': 'L', 'UCG': 'S', 'UAG': '-', 'UGG': 'W',  # UxG
    # C
    'CUU': 'L', 'CCU': 'P', 'CAU': 'H', 'CGU': 'R',  # CxU
    'CUC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',  # CxC
    'CUA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',  # CxA
    'CUG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',  # CxG
    # A
    'AUU': 'I', 'ACU': 'T', 'AAU': 'N', 'AGU': 'S',  # AxU
    'AUC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',  # AxC
    'AUA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',  # AxA
    'AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',  # AxG
    # G
    'GUU': 'V', 'GCU': 'A', 'GAU': 'D', 'GGU': 'G',  # GxU
    'GUC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',  # GxC
    'GUA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',  # GxA
    'GUG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'  # GxG
    }
    dnaCodonTable = {key.replace('U','T'):value for key, value in rnaCodonTable.items()}

    #ACGTUN
    accepted = ['A','C','G','T','U','N']    

    def __init__ (self, sequence):
    	''' clean up user input (remove spaces and capitalize)'''
    	l = ''.join(sequence).split()
        s = ''.join(l).upper()
        ''' get rid of any characters that are not accepted'''
        for a in s:
        	if a not in accepted:
        		s.rplace(a,"")
        ''' create array of codons in gene sequence '''
        self.geneSeq  = [s[i:i+n] for i in range(0, len(s),3)]

    def addSequence (self, thisSequence):
        self.geneSeq.append(thisSequence[i:i+n] for i in range(0, len(thisSequence),3))
        return self.geneSeq

    def aaComposition(self):
        aaDict = {key:self.geneSeq.count(key) for key in NucParams.dnaCodonTable.keys()}
        return aaDict

     def nucComposition(self):
        nucDict = {
        #nucleotide dictionary
        'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0,
        'U' : 0, 'N' : 0
       	}
       	return {key:nucDict[key]+1 for key in self.geneSeq}

     def codonComposition(self):
        rnaVersion = codon.replace('T','U') for codon in self.geneSeq
        cleanRna = rnaVersion.remove(codon) if 'N' in codon for codon in rnaVersion


     def nucCount(self):
        pass
 

import sys
class FastAreader :
    
    def __init__ (self, fname=''):
        '''contructor: saves attribute fname '''
        self.fname = fname
            
    def doOpen (self):
        if self.fname is '':
            return sys.stdin
        else:
            return open(self.fname)
 
    def readFasta (self):
        
        header = ''
        sequence = ''
        
        with self.doOpen() as fileH:
            
            header = ''
            sequence = ''
 
            # skip to first fasta header
            line = fileH.readline()
            while not line.startswith('>') :
                line = fileH.readline()
            header = line[1:].rstrip()
 
            for line in fileH:
                if line.startswith ('>'):
                    yield header,sequence
                    header = line[1:].rstrip()
                    sequence = ''
                else :
                    sequence += ''.join(line.rstrip().split()).upper()
 
                 
        yield header,sequence
 
 
# presumed object instantiation and example usage
# myReader = FastAreader ('testTiny.fa');
# for head, seq in myReader.readFasta() :
#     print (head,seq)