#!/usr/bin/env python3
# Name: Jude Allen Joseph (jajoseph)
# Group Members: None

import sequenceAnalysis

"""
    genome analyzer class
    initializes object with fastaReader and NucParams

    analyze - reads fasta file and uses NucParams to build:
                nucloetide comp dictioanry
                codon comp dictionary
                aa comp dictionary
              and print out analysis
"""

class geneomeAnalzer:
    def __init__(self):
        self.fastaReader = sequenceAnalysis.FastAreader()
        self.analyzer = sequenceAnalysis.NucParams()

    def analyze(self):
        for header, sequence in self.fastaReader.readFasta():
            self.analyzer.addSequence(sequence)

        '''get all the dictionaries we need for analysis'''
        nucComp = self.analyzer.nucComposition()
        codonComp = self.analyzer.codonComposition()
        aaComp = self.analyzer.aaComposition()

        '''extract data from dictionaries'''
        sequenceLength = self.analyzer.nucCount() / 1000000
        gcContent = 0
        if sequenceLength > 0:
            gcContent = ((nucComp['G'] + nucComp['C']) / sum(nucComp.values())) * 100

        '''output data'''
        print("sequence length = %0.2f Mb\n" % sequenceLength)
        print("GC content = %0.1f %% \n" % gcContent)

        for codon, aa in sorted(self.analyzer.rnaCodonTable.items()):
            codonFrequency = 0
            '''check if file has any aa in it'''
            if sequenceLength > 0:
                codonFrequency = (codonComp[codon] / aaComp[aa]) * 100
            '''print out information on codon bias'''
            print("%s : %s %5.1f (%6d)" % (codon, aa, codonFrequency, codonComp[codon]))

def main():
    analyzer = geneomeAnalzer()
    analyzer.analyze()

main()