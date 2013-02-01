from pyparsing import *

from . import BlockEndNotFoundException, BlockStartNotFoundException, BlockIsEmptyException


class IngredientBlockFactory(object):
    @classmethod
    def get_block_for(cls, text):
        return ConcordanceIngredientBlock(text)

class ConcordanceIngredientBlock(object):
    _orginal_text = None
    _text = None
    start_of_block = None
    end_of_block = None

    def __init__(self, text):
        super(ConcordanceIngredientBlock, self).__init__()
        self.text = text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._orginal_text = value
        self.start_of_block = self._find_start_of_block_location()
        self.end_of_block = self._find_end_of_block()
        self._text = self._extract_text()

    def _find_start_of_block_location(self):
        ingredient_header = Combine(CaselessLiteral("ingredient") + Optional("s") + Optional(":"))
        concordance_begin = CaselessLiteral("concordance-begin")
        block_start = Combine(Group(ingredient_header + OneOrMore(White()) + concordance_begin))

        for toks, startLoc, endLoc in block_start.scanString(self._orginal_text):
            print toks
            return endLoc + 1

        raise BlockStartNotFoundException()

    def _find_end_of_block(self):
        end_index = self._orginal_text.find("concordance-end", self.start_of_block)
        if end_index == -1:
            raise BlockEndNotFoundException()
        return end_index

    def _extract_text(self):
        text = self._orginal_text[self.start_of_block:self.end_of_block]
        if len(text.rstrip().lstrip()) == 0:
            raise BlockIsEmptyException()
