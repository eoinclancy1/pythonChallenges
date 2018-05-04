# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 23:03:40 2018

@author: Eoin Clancy
"""

class Node(object):
    def __init__(self, letters=None):
        self.letters = letters
        self.children = {}
        self.num_occurences = 1

    def expand(self):
        print(self.letters)
        if not self.letters: #if it has no letters return
            return
        self.children[self.letters[0]] = Node(self.letters[1:])
        self.letters = None


class Trie(object):
    def __init__(self):
        self.root = Node()

    def add_contact(self, contact):
        node = self.root
        for i in range(len(contact)):
            letter = contact[i]
            if letter not in node.children:
                new_node = Node(letters=contact[i + 1:])
                node.children[letter] = new_node
                break
            else:
                node = node.children[letter]
                node.expand()
                node.num_occurences += 1

    def get_num_occurences(self, contact):
        node = self.root
        for letter in contact:
            if letter not in node.children:
                return 0
            node = node.children[letter]
            node.expand()
        return node.num_occurences
                
            
        
n = int(input().strip())
trie = Trie()
for i in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        trie.add_contact(contact)
    else:
        print(trie.get_num_occurences(contact))