
class BasePage:
    """基础page层,封装元素定位常用方法。"""

    def __init__(self, driver):
        self.driver = driver

    # 打开页面
    def open(self, url=None):
        if url is None:
            self.driver.get(self.url)
            # 进入登陆表单
            el_frame = self.driver.find_element_by_xpath("//*[starts-with(@id, 'x-URS-iframe')]")
            self.driver.switch_to.frame(el_frame)
        else:
            self.driver.get(url)

    # id 定位
    def by_id(self, id_):
        return self.driver.find_element_by_id(id_)

    # name 定位
    def by_name(self, name):
        return self.driver.find_element_by_name(name)

    # class 定位
    def by_class(self, class_name):
        return self.driver.find_element_by_class_name(class_name)

    # xpath 定位
    def by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    # css 定位
    def by_css(self, css):
        return self.driver.find_element_by_css_selector(css)

    # 获取title
    def get_title(self):
        return self.driver.title

    # 获取页面text，仅使用xpath定位
    def get_text(self, xpath):
        return self.by_xpath(xpath).text

    # 执行JavaScript脚本
    def js(self, script):
        self.driver.execute_script(script)

