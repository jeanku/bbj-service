from Util.ChromeHeadless.pyppeteer.pyppeteer.launcher import launch
# from pyppeteer.launcher import launch
import asyncio
from Util.ChromeHeadless.exe_js import js1, js3, js4, js5
from Util.ChromeHeadless.Settings import launch_kwargs_settings


class ChromeHeadless():
    page = None
    browser = None
    cookies = None
    url = None

    async def driver(self):
        launch_kwargs = launch_kwargs_settings
        self.browser = await launch(launch_kwargs)
        page = await self.browser.newPage()
        # 浏览器默认开启大小为：800 * 600 一般是不够的
        # """使用tkinter获取屏幕大小，并设置为最大"""
        # tk = tkinter.Tk()
        # width = tk.winfo_screenwidth()
        # height = tk.winfo_screenheight()
        # tk.quit()
        # await page.setViewport({
        #     "width": width ,
        #     "height": height
        # })
        self.page = page

    def get_cookies(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.run())
        return self.cookies

    async def run(self):
        await self.driver()
        await self.page.goto(self.url)
        await self.page.evaluate(js1)
        await self.page.evaluate(js3)
        await self.page.evaluate(js4)
        await self.page.evaluate(js5)
        await self.handle()
        await self.browser.close()

    async def handle(self):
        pass

    async def handle_cookie(self, page):
        # res = await page.content() # 获取页面内容
        cookies_list = await page.cookies()
        cookies = ''
        for cookie in cookies_list:
            str_cookie = '{0}={1};'
            str_cookie = str_cookie.format(cookie.get('name'), cookie.get('value'))
            cookies += str_cookie
        self.cookies = cookies


if __name__ == '__main__':
    C = ChromeHeadless()
    print(C.get_cookies())
