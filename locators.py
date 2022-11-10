from selenium.webdriver.common.by import By

CONTACT_US = (By.ID, 'contact-link')
SING_IN = '/html/body/div[1]/div[1]/header/div[2]/div/div/nav/div[1]/a'
WOMEN_MENU = (By.XPATH, "(//a[@class='sf-with-ul'][normalize-space()='Women'])[1]")
DRESSES_MENU = (By.XPATH, "(//a[@title='Dresses'][normalize-space()='Dresses'])[2]")
SHIRTS_MENU = (By.XPATH, "(//a[@title='T-shirts'][normalize-space()='T-shirts'])[2]")
T_SHIRTS = (By.XPATH, "(//a[@title='T-shirts'][normalize-space()='T-shirts'])[1]")
CASUAL_DRESSES = (By.XPATH, "(//a[@title='Casual Dresses'][normalize-space()='Casual Dresses'])[1]")
EVENING_DRESSES = (By.XPATH, "(//a[@title='Evening Dresses'][normalize-space()='Evening Dresses'])[1]")
SUMMER_DRESSES = (By.XPATH, "(//a[@title='Summer Dresses'][normalize-space()='Summer Dresses'])[1]")
BLOUSES = (By.XPATH, "(//a[@title='Blouses'][normalize-space()='Blouses'])[1]")

CASUAL_DRESSES_FROM_DRESS_MENU = (By.CSS_SELECTOR, "class='sfHover'] a[title='Casual Dresses']")
EVENING_DRESSES_FROM_DRESS_MENU = (By.CSS_SELECTOR, "class='sfHover'] a[title='Evening Dresses']")
SUMMER_DRESSES_FROM_DRESS_MENU = (By.CSS_SELECTOR, "class='sfHover'] a[title='Summer Dresses']")
