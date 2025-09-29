# 使用Selenium自动化工具实现网页操作

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# 启动Chrome浏览器服务
chrome_service = Service(r'C:\Users\CGH\Desktop\pyth\slz\chromedriver.exe')
chrome_service.start()
# 创建Chrome浏览器对象
driver = webdriver.Chrome(service=chrome_service)

# 打开指定网页
driver.get("https://slz02.scholasticlearningzone.com/resources/dp-int/dist/#/login3/PHLxpdd")
time.sleep(1)

# 定位并填写用户名输入框
username_input = driver.find_element(By.XPATH, '//*[@id="main-container"]/app-login3/div[1]/div[1]/div/form/div[2]/input')
username_input.send_keys("Alex Cai")

# 定位并填写密码输入框
password_input = driver.find_element(By.XPATH, '//*[@id="main-container"]/app-login3/div[1]/div[1]/div/form/div[3]/input')
password_input.send_keys("123456")

# 点击登录按钮
login_button = driver.find_element(By.XPATH, '//*[@id="main-container"]/app-login3/div[1]/div[1]/div/form/div[4]/button')
login_button.click()
time.sleep(2)

# 点击学生仪表板图标
student_dashboard = driver.find_element(By.XPATH, '//*[@id="main-container"]/app-student-dashboard/div/div[2]/div[1]/div[1]/img')
student_dashboard.click()

print('done')
