from . import TestCase
from flexmock import flexmock

from recikeep.recipes.scraper import RecipeScraper
from .blocks.ingredients import IngredientBlockFactory


class RecipeScraperTest(TestCase):
    """
    RecipeScraper:  Scrapes text input to construct recipes
    """

    def test_should_strip_out_html_tags(self):
        """Should strip out any HTML tags from the loaded text to create the ingredient block"""
        mocked_loader = flexmock().should_receive('load').and_return("<html>recipe text</html>").mock()
        mocked_block = flexmock(text='recipe text')
        flexmock(IngredientBlockFactory).should_receive("get_block_for").with_args('recipe text').once().and_return(mocked_block)

        scrapper = RecipeScraper()
        scrapper.scrape_recipe(mocked_loader)

    def test_should_generate_ingredient_string_list_from_concordance_block(self):
        """Should generate a list of ingredient strings from the ingredients concordance block"""
        ingredient_block = """
            ingredient 1
            ingredient 2
            ingredient 3

            """
        ingredient_list = ["ingredient 1", "ingredient 2", "ingredient 3"]

        mocked_loader = flexmock().should_receive('load').and_return("<html>recipe text</html>").mock()
        mocked_block = flexmock(text=ingredient_block)
        flexmock(IngredientBlockFactory).should_receive("get_block_for").with_args('recipe text').once().and_return(mocked_block)

        scrapper = RecipeScraper()
        scrapper.scrape_recipe(mocked_loader)
        self.assertEqual(scrapper.raw_ingredient_list, ingredient_list)
