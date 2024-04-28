import unittest
from trie import Trie

class TestTrie(unittest.TestCase):

    def test_multiple_words(self):
        t = Trie()
        t.insert('apple')
        t.insert('banana')
        t.insert('orange')
        t.insert('app')
        self.assertTrue(t['a']['p']['p']['l']['e'].end)
        self.assertTrue(t['b']['a']['n']['a']['n']['a'].end)
        self.assertTrue(t['o']['r']['a']['n']['g']['e'].end)
        self.assertTrue(t['a']['p']['p'].end)
        self.assertFalse(t['a']['p']['p']['l'].end)
        self.assertFalse(t['z'].end)

    def test_read_file(self):
        t = Trie()
        t.read_file('test/test_words.txt')
        self.assertTrue(t['a']['p']['p']['l']['e'].end)
        self.assertTrue(t['b']['a']['n']['a']['n']['a'].end)
        self.assertTrue(t['o']['r']['a']['n']['g']['e'].end)
        self.assertTrue(t['a']['p']['p'].end)
        self.assertFalse(t['a']['p']['p']['l'].end)
        self.assertFalse(t['z'].end)

if __name__ == '__main__':
    unittest.main()