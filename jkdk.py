#!/usr/bin/env python
# coding: utf-8

# In[70]:


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from send_email import sm

def checkin(username, password, email_address, email_lisence):
    try:
        #登录
        daka = "http://my.lzu.edu.cn:8080/login?service=http://my.lzu.edu.cn"
        driver = webdriver.Chrome()
        driver.get(daka)
        driver.find_element_by_id("username").send_keys("{}").format(username)
        driver.find_element_by_id("password").send_keys("{}").format(password)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/form/div[4]/button").click()

        sleep(3)

        #悬停
        move = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/ul/li[1]/a/div[2]/p[1]")
        ActionChains(driver).move_to_element(move).perform()
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/ul/li[1]/a/div[2]/p[2]/span[1]").click()

        #切换到子页面
        sleep(3)
        driver.switch_to.frame('iframe')


        #填报
        try:
            element=driver.find_element_by_xpath("/html/body/uni-app/uni-modal/div[2]/div[3]/div")
            element.click()
        except Exception as e:
            pass

        driver.find_element_by_xpath("/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view/uni-form/span/uni-view[12]/uni-button").click()
        driver.switch_to.default_content()
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/img").click()
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/a[2]/span").click()
        #关闭浏览器
        sleep(3)
        driver.quit()
        #发送成功邮件
        sm("{}", "{}", "1846128548@qq.com", "打卡成功！", "打卡成功！not bad!" ).format(email_address, email_lisence)
    except Exception as e:
        #发送成功邮件
        sm("{}", "{}", "1846128548@qq.com", "打卡失败！", "打卡失败！not well!建议手动打卡" ).format(email_address, email_lisence)


# In[ ]:




