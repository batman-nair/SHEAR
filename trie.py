''' A simple Trie structure with the following requirements:
    - Insert word list as a file
    - Manually traverse the trie
    - Check if trie is at a word end
    - Store the trie in a file
'''

from typing import Dict, Optional

class Trie:
    def __init__(self) -> None:
        self.data : Dict[str, Trie] = dict()
        self.end = False

    def read_file(self, file_path: str) -> None:
        ''' Read the file and insert the words into the trie '''
        with open(file_path, 'r') as file:
            for line in file.readlines():
                self.insert(line.strip())

    def insert(self, word: str) -> None:
        ''' Insert a word into the trie '''
        if len(word) == 0:
            self.end = True
            return
        if word[0] not in self.data:
            self.data[word[0]] = Trie()
        self.data[word[0]].insert(word[1:])

    def __getitem__(self, key: str) -> Optional['Trie']:
        assert len(key) == 1, 'Key must have exactly one character'
        if key not in self.data:
            self.data[key] = Trie()
        return self.data[key]