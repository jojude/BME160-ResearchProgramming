#!/usr/bin/env python3
# Name: Jude Allen Joseph (jajoseph)
# Group Members: None
import numpy as np

'''

    Provides functions to get certain attributes of an amino acid chain such as:
        Molecular weight
        Amino acid count 
        Amino acid composition
        Theoretical isoelectric point
        Molar and mass extinction 

    Inputs: Amino Acid chain
    Outputs: None
'''


class ProteinParam:
    # These tables are for calculating:
    #     molecular weight (aa2mw), along with the mol. weight of H2O (mwH2O)
    #     absorbance at 280 nm (aa2abs280)
    #     pKa of positively charged Amino Acids (aa2chargePos)
    #     pKa of negatively charged Amino acids (aa2chargeNeg)
    #     and the constants aaNterm and aaCterm for pKa of the respective termini
    #  Feel free to move these to appropriate methods as you like

    # As written, these are accessed as class attributes, for example:
    # ProteinParam.aa2mw['A'] or ProteinParam.mwH2O

    aa2mw = {
        'A': 89.093, 'G': 75.067, 'M': 149.211, 'S': 105.093, 'C': 121.158,
        'H': 155.155, 'N': 132.118, 'T': 119.119, 'D': 133.103, 'I': 131.173,
        'P': 115.131, 'V': 117.146, 'E': 147.129, 'K': 146.188, 'Q': 146.145,
        'W': 204.225, 'F': 165.189, 'L': 131.173, 'R': 174.201, 'Y': 181.189
    }
    mwH2O = 18.015
    aa2abs280 = {'Y': 1490, 'W': 5500, 'C': 125}

    aa2chargePos = {'K': 10.5, 'R': 12.4, 'H': 6}
    aa2chargeNeg = {'D': 3.86, 'E': 4.25, 'C': 8.33, 'Y': 10}
    aaNterm = 9.69
    aaCterm = 2.34

    # the __init__ method requires a protein string to be provided, either as a
    # string or list of strings that will be concatenated
    ''' added aaDict - amino acid count dictionary based on input sequence'''

    def __init__(self, protein):
        l = ''.join(protein).split()
        self.protString = ''.join(l).upper()
        self.aaDict = {key: self.protString.count(key)
                       for key in ProteinParam.aa2mw.keys()}

    # helper functions for _charge_(pH)
    """
        These functions are used for the netCharge equation.
        They are used respectively for pos and neg charged amino acids
        as well the start and end terminals.
    """

    def posChargeCalc(self, aa, pH):
        pKa = 10 ** ProteinParam.aa2chargePos[aa]
        divisor = pKa + 10 ** pH
        return self.aaDict[aa] * (pKa / divisor)

    def negChargeCalc(self, aa, pH):
        pKa = 10 ** ProteinParam.aa2chargeNeg[aa]
        divisor = pKa + 10 ** pH
        return self.aaDict[aa] * ((10 ** pH) / divisor)

    def aaNCalc(self, pH):
        return (10 ** ProteinParam.aaNterm) / ((10 ** ProteinParam.aaNterm) + (10 ** pH))

    def aaCCalc(self, pH):
        return (10 ** pH) / ((10 ** ProteinParam.aaCterm) + (10 ** pH))

        # main functions

    def aaCount(self):
        count = 0
        '''for each element in string find if it is an aa...'''
        for char in self.protString:
            if char in ProteinParam.aa2mw.keys():
                count += 1
        return count

    def pI(self):
        charges = []
        ''' use numpy function arange to iterate by 0.01'''
        for pH in np.arange(0.0, 14.01, 0.01):
            charges.append(self._charge_(pH))
        ''' find minimum value that is greater than 0 in list'''
        leastCharge = min(i for i in charges if i >= 0.0)
        '''mutiple index of min value by 0.01 to get the correct pH value'''
        return charges.index(leastCharge) * 0.01

    def aaComposition(self):
        ''' return already built dict from __init__'''
        return self.aaDict

    def _charge_(self, pH):
        posCharge = 0.0
        negCharge = 0.0
        nonDupString = "".join(set(self.protString))
        ''' find which char in string are pos or neg and calculate value'''
        for aa in nonDupString:
            if aa in self.aa2chargePos.keys():
                posCharge = posCharge + self.posChargeCalc(aa, pH)
            elif aa in self.aa2chargeNeg.keys():
                negCharge = negCharge + self.negChargeCalc(aa, pH)
        '''add start and end terminal values in aa chain'''
        posCharge += self.aaNCalc(pH)
        negCharge += self.aaCCalc(pH)
        return posCharge - negCharge

    def molarExtinction(self):
        y = self.aaDict['Y'] * ProteinParam.aa2abs280['Y']
        w = self.aaDict['W'] * ProteinParam.aa2abs280['W']
        c = self.aaDict['C'] * ProteinParam.aa2abs280['C']
        return y + w + c

    def massExtinction(self):
        myMW = self.molecularWeight()
        return self.molarExtinction() / myMW if myMW else 0.0

    def molecularWeight(self):
        '''get string without any duplicates for correct iteration'''
        nonDupString = "".join(set(self.protString))
        '''sum weights for each distinct aa in string mult by number of times it appears'''
        totalAAMW = sum(self.aaDict[aa] * ProteinParam.aa2mw[aa] for aa in nonDupString)
        totalH20W = ProteinParam.mwH2O * (sum(self.aaDict[aa] for aa in nonDupString) - 1)
        return totalAAMW - totalH20W

# Please do not modify any of the following.  This will produce a standard output that can be parsed

import sys

for inString in sys.stdin:
    myParamMaker = ProteinParam(inString)
    myAAnumber = myParamMaker.aaCount()
    print("Number of Amino Acids: {aaNum}".format(aaNum=myAAnumber))
    print("Molecular Weight: {:.1f}".format(myParamMaker.molecularWeight()))
    print("molar Extinction coefficient: {:.2f}".format(myParamMaker.molarExtinction()))
    print("mass Extinction coefficient: {:.2f}".format(myParamMaker.massExtinction()))
    print("Theoretical pI: {:.2f}".format(myParamMaker.pI()))
    print("Amino acid composition:")
    myAAcomposition = myParamMaker.aaComposition()
    keys = list(myAAcomposition.keys())
    keys.sort()
    if myAAnumber == 0: myAAnumber = 1  # handles the case where no AA are present
    for key in keys:
        print("\t{} = {:.2%}".format(key, myAAcomposition[key] / myAAnumber))

