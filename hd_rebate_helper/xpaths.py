"""(This is the module docstring)"""

buttons = {
    'home_page_continue': '//*[@id="home-offer-purchasedate-continue2"]',
    'terms_page_continue': '//*[@id="continueOrSubmitBtn"]',
    'receipt_page_continue': '//*[@id="continueOrSubmitBtn"]',
    'personal_page_continue': '//*[@id="continueBtn"]/button',
    'use_entered_address': '//*[@id="enteredAddressBtn"]',
    'final_submit': '//*[@id="continueOrSubmitBtnBottom"]',
}

inputs = {
    'receipt_number': '//*[@id="Receipt Number"]',
    'receipt_total': '//*[@id="Gross Sales"]',
    'first_name': '//*[@id="pdfGenerate1"]/div[3]/div/div[1]/form/div/div[1]/div[1]/input',
    'last_name': '//*[@id="pdfGenerate1"]/div[3]/div/div[1]/form/div/div[1]/div[2]/input',
    'phone_number': '//*[@id="pdfGenerate1"]/div[3]/div/div[1]/form/div/div[1]/div[4]/input',
    'purchase_date': '//*[@id="purchaseDateOnlyText"]',
    'email': '//*[@id="pdfGenerate1"]/div[3]/div/div[1]/form/div/div[1]/div[5]/input',
    'email_confirmation': '//*[@id="pdfGenerate1"]/div[3]/div/div[1]/form/div/div[1]/div[6]/input',
    'street': '//*[@id="pdfGenerate1"]/div[3]/div/div[1]/form/div/div[2]/div[1]/input',
    'apartment': '//*[@id="pdfGenerate1"]/div[3]/div/div[1]/form/div/div[2]/div[2]/input',
    'zip_code': '//*[@id="pdfGenerate1"]/div[3]/div/div[1]/form/div/div[2]/div[3]/input',
}
