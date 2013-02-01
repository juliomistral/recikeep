from bs4 import BeautifulSoup
from .blocks.ingredients import IngredientBlockFactory
from recikeep.lib.util import clean_split_lines

class RecipeScraper(object):
    raw_recipe_text = None
    raw_ingredient_list = None
    ingredient_block = None

    def scrape_recipe(self, loader):
        soup = BeautifulSoup(loader.load())
        self.raw_recipe_text = soup.text
        self._generate_raw_ingredients_list()

    def _generate_raw_ingredients_list(self):
        ingredient_block = IngredientBlockFactory.get_block_for(self.raw_recipe_text)
        ingredient_lines = ingredient_block.text.splitlines()
        self.raw_ingredient_list = clean_split_lines(ingredient_lines)
