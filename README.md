# SHEAR - SHorten sEntences to cAtchy woRds

Python script to shorten a phrase or a sentence to small word.

Run as `python short.py 'Sentence to shorten'`

Default run uses the whole word list but only 1 word guesses.
Another interesting use case is to look for 2 word combinations using only the common words list.

```bash
python short.py 'Sentence to shorten' --word_list common --n_word_combination 2
```

See all possible options with `python short.py -h`


# But why?

Saw a (paper)[https://openaccess.thecvf.com/content/CVPR2021/papers/Ahmed_Unsupervised_Multi-Source_Domain_Adaptation_Without_Access_to_Source_Data_CVPR_2021_paper.pdf] that shortened "Data frEe multi-sourCe unsupervISed domain adaptatiON" to DECISION.

Thought it would be cool to automate this and so the script was born.
One use-case is to come up with project names.


# Sources

Word list from https://github.com/dwyl/english-words
Common words from https://python.sdv.univ-paris-diderot.fr/data-files/english-common-words.txt
