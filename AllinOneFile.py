# coding: utf-8

import datetime
import json
import hashlib

#------------------------------------------------------------------------------------------

class Block:
    def __init__(self, index, timestamp, prev_hash, transaction):
        self.index = index
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.transaction = transaction
        self.seqHurdle = 3
        self.nonce = None
        self.current_hash = None


    def showBlock(self):
        outJSON = {
            'index'       : self.index,\
            'timestamp'   : self.timestamp,\
            'prev_hash'   : self.prev_hash,\
            'transaction' : self.transaction,\
            'nonce'       : self.nonce
        }
        print(outJSON)



    def mine(self, t_records):

        self.transaction.append(t_records)

        blockJSON = {
            'index'             : self.index,\
            'timestamp'         : self.timestamp,\
            'prev_hash'         : self.prev_hash,\
            'current_hash'      : self.current_hash,\
            'transaction'       : self.transaction
        } 

        N = 0
        for _ in range(50000):
            blockJSON['nonce'] = N
            blockText = json.dumps(blockJSON)
            test_hash = hashlib.sha256(blockText.encode('ascii')).hexdigest()
            if test_hash[0:self.seqHurdle].count('0') == self.seqHurdle:
                self.nonce = N        
                return True
            N += 1
        return False


    def storeHash(self):
        if self.nonce == None:
            return
        blockJSON = {
            'index'             : self.index,\
            'timestamp'         : self.timestamp,\
            'prev_hash'         : self.prev_hash,\
            'current_hash'      : self.current_hash,\
            'transaction'       : self.transaction,\
            'nonce'             : self.nonce
        }
        blockText = json.dumps(blockJSON)
        self.current_hash = hashlib.sha256(blockText.encode('ascii')).hexdigest()
        return

#------------------------------------------------------------------------------------------


block_chain = []

block = Block(0, str(datetime.datetime.now()), '-', [])

trade = {   'From_ID' : 'Amount', \
            'to_ID' : 'Amount'
        }

if block.mine(trade):
    block.storeHash()
    block_chain.append(block)
else:
    pass


for i in range(5):
    block = Block(i+1, str(datetime.datetime.now()), block_chain[i].current_hash, [])
    trade = {   'From_ID' : 'Amount', \
                'to_ID' : 'Amount'
            }
    if block.mine(trade):
        block.storeHash()
        block_chain.append(block)
    else:
        pass


    

for block in block_chain:
    block.showBlock()




