# -*- coding: utf-8 -
import os
from pathlib import Path
from simutil.App import app
import importlib

class TestIndex:
    # 当前脚本所在的文件绝对路径
    cur_path = Path(os.path.dirname(os.path.realpath(__file__)) + '/UnitTest/')

    def run(self):
        for item in self.cur_path.rglob('*.py'):
            self.handle('Scripts.UnitTest.{}' .format(item.stem), item.stem)

    def handle(self, path, name):
        try:
            Import = importlib.import_module(path)
            classname = getattr(Import, name)
            classname().run()
        except Exception as e:
            app('log').warning(e)


if __name__ == "__main__":
    app.register("BASE_PATH", os.path.dirname(os.path.dirname(__file__)))
    TestIndex().run()
