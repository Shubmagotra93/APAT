import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from caseStudy.tests.base import Base


class LandingPage(Base):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)


    sign_in_button = (By.XPATH, "(//a[@data-nav-role='signin'])[1]")
    email = (By.ID, "ap_email")
    continue_btn = (By.CSS_SELECTOR, "#continue")
    after_otp = (By.XPATH, "//input[@aria-label='Verify OTP Button']")
    search_bar = (By.ID, "twotabsearchtextbox")
    search_items = (By.XPATH, "//div[@class='s-suggestion-container']")
    iphone_15_click = (By.XPATH, "//span[text()='Apple iPhone 15 (128 GB) - Blue']")
    add_to_cart = (By.XPATH, "(//input[@id='add-to-cart-button'])[2]")
    go_to_cart = (By.XPATH, "//a[contains(text(),'Go to Cart')]")
    checkout = (By.NAME, "proceedToRetailCheckout")
    use_address = (By.XPATH, "(//input[@class='a-button-input'])[6]")
    payment_radio = (By.XPATH, "(//div[@class='a-radio'])[1]")
    enter_card_details_link = (By.XPATH, "(//a[text()='Enter card details'])[1]")
    frame = (By.NAME, "//iframe[@name='ApxSecureIframe']")
    card_no = (By.NAME, "addCreditCardNumber")
    click_enter = (By.XPATH, "//span[text()='Enter card details']")
    card_alert_error = (By.CSS_SELECTOR, ".a-box-inner a-alert-container")



    def login_feature(self, email):
        self.wait.until(EC.element_to_be_clickable(LandingPage.sign_in_button)).click()
        self.wait.until(EC.presence_of_element_located(LandingPage.email)).send_keys(email)
        self.wait.until(EC.element_to_be_clickable(LandingPage.continue_btn)).click()
        self.wait.until(EC.element_to_be_clickable(LandingPage.continue_btn)).click()
        # wait for OTP to enter
        time.sleep(20)  # Replace with actual OTP handling logic
        self.wait.until(EC.element_to_be_clickable(LandingPage.after_otp)).click()
        return

    def search_feature(self,value):
        search = self.wait.until(EC.element_to_be_clickable(LandingPage.search_bar))
        search.clear()
        search.send_keys(value)
        lst = self.driver.find_elements(*LandingPage.search_items)
        for i in lst:
            print("Auto Suggestion: ", i.text)
        search.send_keys(Keys.ENTER)
        ele = self.driver.find_element(*LandingPage.iphone_15_click)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        original_window = self.driver.current_window_handle
        ele.click()
        for child_window in self.driver.window_handles:
            print(child_window)
            if child_window != original_window:
                self.driver.switch_to.window(child_window)
                break
        return

    def adding_cart_feature(self, card_no):
        cart = self.driver.find_element(*LandingPage.add_to_cart)
        self.driver.execute_script("arguments[0].scrollIntoView();", cart)
        time.sleep(2)
        cart.click()
        self.wait.until(EC.element_to_be_clickable(LandingPage.go_to_cart)).click()
        self.wait.until(EC.element_to_be_clickable(LandingPage.checkout)).click()
        self.wait.until(EC.element_to_be_clickable(LandingPage.use_address)).click()
        self.wait.until(EC.element_to_be_clickable(LandingPage.payment_radio)).click()
        self.wait.until(EC.element_to_be_clickable(LandingPage.enter_card_details_link)).click()
        frame = self.driver.find_element(*LandingPage.frame)
        self.driver.switch_to.frame(frame)
        self.wait.until(EC.element_to_be_clickable(LandingPage.card_no)).send_keys(card_no)
        self.wait.until(EC.element_to_be_clickable(LandingPage.click_enter)).click()
        error = self.wait.until(EC.element_to_be_clickable(LandingPage.card_alert_error))
        print(error.text)
        return






















