from typing import List, Tuple, Union
from trie import Trie
from typing import NamedTuple
import argparse


def setup_trie(words_file: str) -> Trie:
    t = Trie()
    t.read_file(words_file)
    return t

def get_words(
        sentence: str,
        min_word_coverage: Union[int, float]=1.0,
        only_first_n_char: int=0,
        n_word_combinations: int=1
) -> List[str]:
    ''' Method 2: Split the sentence into words and find all possible words'''

    class State(NamedTuple):
        string: str
        touched_words: Tuple[int]
    min_words = min_word_coverage*len(sentence.split())
    only_first_n_char = only_first_n_char or len(sentence)

    trie_pointers = {State('', ()): root_trie}
    for word_index, word in enumerate(sentence.split()):
        for char in word[:only_first_n_char]:
            new_pointers = dict()
            for state, current_trie in trie_pointers.items():
                if char in current_trie:
                    next_trie = current_trie[char]
                    new_touched_words = state.touched_words
                    if not new_touched_words or new_touched_words[-1] != word_index:
                        new_touched_words = new_touched_words + (word_index,)
                    new_state = State(state.string+char, new_touched_words)
                    new_pointers[new_state] = next_trie
                    # If the word is a valid word, try to add more words
                    if next_trie.end and len(new_state.string.split('-')) < n_word_combinations:
                        new_pointers[State(new_state.string + '-', new_touched_words)] = root_trie
                new_pointers[state] = current_trie
            trie_pointers = new_pointers

    words = {state.string for state, trie in trie_pointers.items()
             if trie.end and len(state.touched_words) >= min_words}
    return words


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find a short word from a phrase or a sentence')
    parser.add_argument('sentence', type=str, help='The sentence to find words in')
    parser.add_argument('--min_word_coverage', type=float, default=0.7, help='Percentage of words in the sentence that must be touched by a word.')
    parser.add_argument('--only_first_n_char', type=int, default=3, help='Only consider the first n characters of each word')
    parser.add_argument('--n_word_combinations', type=int, default=2, help='Maximum number of words that can be combined for a word')
    parser.add_argument('--word_list', default='common', choices=['common', 'all'], help='The word list to use')
    args = parser.parse_args()


    method_args = [args.sentence.lower(), args.min_word_coverage, args.only_first_n_char, args.n_word_combinations]

    words_file = 'english-common-words.txt'
    if args.word_list == 'all':
        words_file = 'words_alpha.txt'
    print(f'Using {args.word_list} words list...')
    root_trie = setup_trie(words_file)
    words = get_words(*method_args)
    words = sorted(words, key=lambda x: (len(x.split('-')), x))

    print(f'Got {len(words)} words. Writing to output.txt...')
    print(words)
    with open('output.txt', 'w') as file:
        for word in words:
            file.write(word + '\n')
