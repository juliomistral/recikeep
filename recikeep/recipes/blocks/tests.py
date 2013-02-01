from . import TestCase
from .ingredients import ConcordanceIngredientBlock
from . import BlockEndNotFoundException, BlockStartNotFoundException, BlockIsEmptyException


class ConcordanceIngredientBlockTest(TestCase):
    """
    ConcordanceIngredientBlock: Scans text to extract the ingredients text demarcated
        by concordance markers
    """
    def setUp(self):
        self.block_start = "1234567890\nIngredients:\nconcordance-begin\n"
        self.ingredient_text = "ingredient 1\ningredient 2\n"
        self.block_end = "concordance-end"
        self.recipe_text = self.block_start + self.ingredient_text + self.block_end

    def test_should_find_the_beginning_of_block(self):
        """Should find the location where the concordance block begins"""
        block = ConcordanceIngredientBlock(self.recipe_text)
        self.assertEqual(block.start_of_block, len(self.block_start))

    def test_should_find_end_of_block(self):
        """Should find the location where the concordance block ends"""
        block = ConcordanceIngredientBlock(self.recipe_text)
        self.assertEqual(block.end_of_block, len(self.block_start + self.ingredient_text))

    def test_should_fail_when_no_block_start(self):
        """Should fail when the block start can't be found"""
        bad_recipe_text = "1234567890\nconcordance-begin"
        self.assertRaises(BlockStartNotFoundException, ConcordanceIngredientBlock, bad_recipe_text)

    def test_should_fail_when_no_block_end(self):
        """Should fail when the block end can't be found"""
        bad_recipe_text = "1234567890Ingredient\nIngredient\nconcordance-begin\n\n"
        self.assertRaises(BlockEndNotFoundException, ConcordanceIngredientBlock, bad_recipe_text)

    def test_should_fail_when_no_text_in_block(self):
        """Should fail when there's no non-whitespace text within the block"""
        bad_recipe_text = "1234567890\nIngredients:\nconcordance-begin\nconcordance-end\n"
        self.assertRaises(BlockIsEmptyException, ConcordanceIngredientBlock, bad_recipe_text)
