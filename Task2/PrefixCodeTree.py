import binascii
from bitstring import BitArray
# must install bitstring and binascii module
# "pip3 install module's name'" to install module

class PrefixCodeTree:
    def __init__(self):
        '''
            Contructor of PrefixCodeTree class
            self.right : the right leaf of the root leaf
            self.left : the left leaf of the root leaf
            self.symbol: the data that this leaf contains
        '''
        self.right = None
        self.left = None
        self.symbol = ""
    def insert(self, codeword, symbol):
        '''insert codeword to a tree'''
        for bit in codeword:
            if bit==1:
                if self.right is None: self.right = PrefixCodeTree()
                self = self.right
            elif bit==0:
                if self.left is None: self.left = PrefixCodeTree()
                self = self.left
        self.symbol = symbol
    def decode(self, encodedData, datalen):
        # convert Binascii string to a list of '0' and '1' characters
        encodedDataBinList = list(BitArray(encodedData).bin)
        # node is an iterator leaf to traverse the tree
        node = self 
        # first : the decodeData <- root leaf's data
        decodeData = node.symbol
        # Traversing tree to decode the string
        for bit in range(datalen):
            if encodedDataBinList[bit] == '1': 
                node = node.right
            elif encodedDataBinList[bit] == '0': 
                node = node.left
            if node == None : return "Undecoded Data!!"
            elif node.symbol != "": 
                decodeData += node.symbol
                node = self
        return decodeData