#!/usr/bin/env python3
# Name: Jude Allen Joseph (jajoseph)
# Group Members: None

import sequenceAnalysis

"""
    Takes in file name and builds :
        nucleotide dict
        codon dict
        amino acid dict
        rna codon dict
    from sequenceAnalysis.py
"""
def analyze(file):
    fastaReader = sequenceAnalysis.FastAreader(file)
    analyzer = sequenceAnalysis.NucParams()

    for header, sequence in fastaReader.readFasta():
        analyzer.addSequence(sequence)

    '''get all the dictionaries we need for analysis'''
    nucComp = analyzer.nucComposition()
    codonComp = analyzer.codonComposition()
    aaComp = analyzer.aaComposition()
    rnaCodonDict = sorted(analyzer.rnaCodonTable.items())

    return nucComp, codonComp, aaComp, rnaCodonDict

"""
    Use the data we gathered from analyze(file_name) to
    compare:
        gcContent
        amino acid counts
        codon frequency
    between two fasta files
"""
def compare(file1, file2):
    nucComp, codonComp, aaComp, rnaCodonDict = analyze(file1)
    nucComp_2, codonComp_2, aaComp_2, rnaCodonDict_2 = analyze(file2)

    '''extract data from dictionaries'''
    gcContent = ((nucComp['G'] + nucComp['C'])/sum(nucComp.values()))*100
    gcContent_2 = ((nucComp_2['G'] + nucComp_2['C'])/sum(nucComp_2.values()))*100

    '''compare gcContent between two files'''
    print("comparing | {0} | {1} \n".format(file1, file2))
    print("gcContent | %0.1f %% | %0.1f %% \n" % (gcContent, gcContent_2))

    '''compare numbers of aa's found in two files'''
    print("aa | {0} | {1}".format(file1, file2))
    for aa in sorted(aaComp.keys()):
        if aaComp[aa] > aaComp_2[aa]:
            print("%s | %d > %d" % (aa, aaComp[aa], aaComp_2[aa]))
        elif aaComp[aa] == aaComp_2[aa]:
            print("%s | %d == %d" % (aa, aaComp[aa], aaComp_2[aa]))
        else:
            print("%s | %d < %d" % (aa, aaComp[aa], aaComp_2[aa]))
    print("\n")

    '''compare codon frequency between files'''
    print("codon | {0} | {1}".format(file1, file2))
    for codon, aa in rnaCodonDict:
        codonFreq = (codonComp[codon] / aaComp[aa]) * 100
        codonFreq2 = (codonComp_2[codon] / aaComp_2[aa]) * 100
        if codonFreq > codonFreq2:
            print("%s | %5.1f > %5.1f" % (codon, codonFreq, codonFreq2))
        elif codonFreq == codonFreq2:
            print("%s | %5.1f = %5.1f" % (codon, codonFreq, codonFreq2))
        else:
            print("%s | %5.1f < %5.1f" % (codon, codonFreq, codonFreq2))

def main():
    '''compare the two files for similarities and differences'''
    compare("testGenome.fa", "haloVolc1_1-genes.fa")

main()