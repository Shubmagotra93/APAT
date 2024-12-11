import allure
import pytest
from pageObjects.landing_page import LandingPage
from tests.base import Base


class Test_Amazon_Site(Base):
    config = Base.config_data()

    @allure.feature("Amazon Product Search")
    @pytest.mark.admin
    def test_amazon_workflow(self):
        lp = LandingPage(self.driver)
        # lp.login_feature(self.config.get("username"))
        lp.search_feature(self.config.get("search_value"))
        lp.adding_cart_feature(self.config.get("card_number"))

