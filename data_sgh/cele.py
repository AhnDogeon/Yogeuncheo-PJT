from selenium import webdriver

## Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome('/Users/multicampus/Desktop/chromedriver')
driver.implicitly_wait(3)
driver.get('https://google.com')

