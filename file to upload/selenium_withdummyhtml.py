from selenium import webdriver
# sfrom selenium import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

browser.get()
browser.maximize_window()
browser.implicitly_wait(10)

# try:
element1 = browser.find_element(By.ID, "fileToUpload")
print('Found the choose file button')
element1.send_keys('https://www.google.com/search?q=johnny+bravo&rlz=1C5CHFA_enIN898IN898&sxsrf=AJOqlzWw_gpenLRo0w0rapPkjABptWMzzg:1675439807967&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjFrOLU2_n8AhUUtlYBHainBBUQ_AUoAXoECAQQAw#imgrc=e9DS120z-PI9xM')
submitbut= browser.find_element(By.NAME,"submit")
print("Found the upload button")

submitbut.click()
print("cLICKED on the searchbutton")
print("Mission accomplished")
# sendbutton.click()

# again =browser.find_element("class",'')
# print('Found <%s> element2 with that class name!' % (again.tag_name))
# again.send_keys('https://static.wikia.nocookie.net/gavin-and-stacey1031/images/3/36/Smithy.jpg/revision/latest?cb=20170108120754')
# print("Sent the link , pasted it to the textbox")
# sendbutton=browser.find_element_by_id("Search")
# sendbutton.click()
# print("Now it will search the web for matches ")
# print("Finally we get :Picture upload successful")




    #the image link ** 'https://static.wikia.nocookie.net/gavin-and-stacey1031/images/3/36/Smithy.jpg/revision/latest?cb=20170108120754'
# except:
# print('Was not able to find an element with that name.')




# from selenium import webdriver
  
# # create webdriver object
# driver = webdriver.Firefox()
  
# # get geeksforgeeks.org
# driver.get("https://www.geeksforgeeks.org/")
  
# # get element 
# element = driver.find_element("id","gcse-search-input")

  
# # send keys 
# element.send_keys("Arrays")
