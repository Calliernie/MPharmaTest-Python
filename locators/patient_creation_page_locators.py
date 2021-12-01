class PatientCreationPageLocators:
    first_name_xpath = "//input[@data-test-id='first-name']"
    middle_name_xpath = "//input[@data-test-id='middle-name']"
    last_name_xpath = "//input[@data-test-id='last-name']"
    phone_number_xpath = "//input[@data-test-id='phone-number']"
    date_of_birth_xpath = "//input[@data-test-id='dob']"
    address_xpath = "//textarea[@data-test-id='address']"
    add_new_user_button_xpath = "//a[@data-test-id='submit-btn']"

    # locators for checking the newly added patient
    created_user_full_name_xpath = "//*[@id=\"root\"]/div/div[2]/main/div[1]/div[2]/h4"
    created_user_address = "//*[@id=\"root\"]/div/div[2]/main/div[1]/div[2]/p[1]"
    created_user_date_of_birth = "//*[@id=\"root\"]/div/div[2]/main/div[1]/div[2]/p[2]"
