import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import time
import constant


class Test_case:

        # 设置Appium的配置
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.platform_version = "15"  # 手机安卓版本
        options.device_name = "Pixel 8 Pro"  # 设备名称
        options.app_package = "com.xingmai.tech"  # APP包名
        options.app_activity = "com.xingmai.splash.SplashActivity"  # 默认启动Activity，可以根据需要调整
        options.no_reset = True  # 不重置应用数据
        options.automation_name = "UiAutomator2"  # 指定自动化框架
        options.full_context_list = True
        print('driver连接appium服务器,并打开app')
        # 连接appium服务器，打开beatbot
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)

        def test_signin_page(self):  # 进入注册页面
                print('点击注册按钮')
                self.driver.implicitly_wait(3)
                # 通过xpath获取注册按钮
                self.driver.find_element("xpath",
                                    "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]").click()
                time.sleep(3)  # 等待跳转到注册页面
                #获取注册页面标题
                title = self.driver.find_element("xpath",'//android.widget.TextView[@text="Sign Up"]').get_attribute('text')
                print(title+'@@@@@@@@@@@@@@@@')
                #判断是否进入注册页面
                assert title =="Sign Up"
                # self.driver.quit()

        def test_signin(self):  # 进入注册页面
                print('点击注册按钮')
                self.driver.implicitly_wait(3)
                #点击隐私政策和用户协议
                self.driver.find_element("xpath",'//android.widget.CheckBox').click()
                time.sleep(2)
                #输入邮箱名称
                self.driver.find_element("xpath", '//android.widget.EditText').send_keys(constant.ran + "@163.com")
                #点击Next按钮
                self.driver.find_element("xpath",'//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]').click()
                time.sleep(2)
                #输入密码
                self.driver.find_element('xpath','//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]').send_keys("Aa123456")
                time.sleep(2)
                #再次输入密码
                self.driver.find_element('xpath','//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]').send_keys("Aa123456")
                time.sleep(2)
                #点击Next
                self.driver.find_element('xpath','//android.widget.TextView[@text="Next"]').click()
                time.sleep(2)
                #点击Skip
                self.driver.find_element('xpath','//android.widget.TextView[@text="Skip"]').click()
                time.sleep(2)
                #获取用户名称
                username = self.driver.find_element('xpath','//android.widget.TextView[@text="Username"]').get_attribute('text')
                #的判断用户名
                assert username == 'Username'





if __name__=="__main__":
    pytest.main(['test_login.py','-v'])