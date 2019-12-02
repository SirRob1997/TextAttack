import spacy

from textattack.tokenizers import Tokenizer

class SpacyTokenizer(Tokenizer):
    """ A basic implementation of the spaCy English tokenizer. 
    
        Params:
            word2id (dict<string, int>): A dictionary that matches words to IDs
            oovid (int): An out-of-variable ID
    """
    def __init__(self, word2id, oovid, padid, max_seq_length=128):
        self.tokenizer = spacy.load('en').tokenizer
        self.word2id = word2id
        self.oovid = oovid
        self.padid = padid
        self.max_seq_length = max_seq_length
    
    def convert_text_to_tokens(self, text):
        spacy_tokens = [t.text for t in self.tokenizer(text)]
        spacy_tokens = spacy_tokens[:self.max_seq_length]
        pad_tokens_to_add = [self.padid] * (self.max_seq_length - len(spacy_tokens))
        spacy_tokens += pad_tokens_to_add
        return spacy_tokens
        
    def convert_tokens_to_ids(self, tokens):
        ids = []
        for token in tokens:
            if token in self.word2id:
                ids.append(self.word2id[token])
            else:
                ids.append(self.oovid)
        return ids