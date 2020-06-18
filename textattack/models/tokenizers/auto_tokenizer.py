import transformers

<<<<<<< HEAD:textattack/tokenizers/auto_tokenizer.py
=======
from textattack.models.tokenizers import Tokenizer
>>>>>>> 6953f0ee7d024957774d19d101175f0fa0176ccc:textattack/models/tokenizers/auto_tokenizer.py
from textattack.shared import TokenizedText
from textattack.tokenizers import Tokenizer



class AutoTokenizer(Tokenizer):
    """ 
    A generic class that convert text to tokens and tokens to IDs. Supports
    any type of tokenization, be it word, wordpiece, or character-based.
    Based on the ``AutoTokenizer`` from the ``transformers`` library.
    
    Args: 
        name: the identifying name of the tokenizer (see AutoTokenizer,
            https://github.com/huggingface/transformers/blob/master/src/transformers/tokenization_auto.py)
        max_length: if set, will truncate & pad tokens to fit this length
    """

    def __init__(
        self,
        name="bert-base-uncased",
        max_length=256,
        pad_to_length=False,
        use_fast=True,
    ):
        self.tokenizer = transformers.AutoTokenizer.from_pretrained(
            name, use_fast=use_fast
        )
        self.max_length = max_length

    def encode(self, input_text):
        if TokenizedText.SPLIT_TOKEN in input_text:
            input_text = input_text.split(TokenizedText.SPLIT_TOKEN)
        encoded_text = self.tokenizer.encode_plus(
            input_text,
            max_length=self.max_length,
            add_special_tokens=True,
            pad_to_max_length=True,
        )
        return dict(encoded_text)