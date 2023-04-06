"""(this is the module docstring)"""

import time # TODO remove this after testing
from selenium import webdriver
from selenium.webdriver.common.by import By
from hd_rebates.xpaths import buttons, inputs

def handle_submission
rebate_website = 'https://www.homedepotrebates11percent.com/'

driver = webdriver.Chrome()
driver.get(rebate_website)
driver.implicitly_wait(5)

# Home page
driver.find_element(By.XPATH, inputs['purchase_date']).send_keys(dummy_date)
driver.find_element(By.XPATH, buttons['home_page_continue']).click()

# Terms page
driver.find_element(By.XPATH, buttons['terms_page_continue']).click()

# Receipt details page
driver.find_element(By.XPATH, inputs['receipt_number']).send_keys(dummy_receipt_number)
driver.find_element(By.XPATH, inputs['receipt_total']).send_keys(dummy_total)
driver.find_element(By.XPATH, buttons['receipt_page_continue']).click()

# Personal details page
driver.find_element(By.XPATH, inputs['zip_code']).send_keys(dummy_zip) # Set zip code first because that populates state and country when you set it
driver.find_element(By.XPATH, inputs['first_name']).send_keys(dummy_first_name)
driver.find_element(By.XPATH, inputs['last_name']).send_keys(dummy_last_name)
driver.find_element(By.XPATH, inputs['phone_number']).send_keys(1234567890)
driver.find_element(By.XPATH, inputs['email']).send_keys(dummy_email)
driver.find_element(By.XPATH, inputs['email_confirmation']).send_keys(dummy_email)
driver.find_element(By.XPATH, inputs['street']).send_keys(dummy_address)
driver.find_element(By.XPATH, inputs['apartment']).send_keys("Apt 1")
driver.find_element(By.XPATH, buttons['personal_page_continue']).click()

# TODO this could be improved for sure
if driver.find_element(By.XPATH, buttons['use_entered_address']).is_displayed():
    driver.find_element(By.XPATH, buttons['use_entered_address']).click()


# Submit the form
#driver.find_element(By.XPATH, buttons['final_submit']).click()

time.sleep(100000)
