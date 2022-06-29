from main import YaUploader
import pytest


class TestSomething:
    ya_disk = ''

    def setup(self):
        self.ya_disk = YaUploader('..\\token_yad.txt')
        self.ya_disk.delete_catalog('4567')

    def test_create_catalog_201(self):
        assert self.ya_disk.create_catalog('4567') == 201

    def test_create_catalog_409(self):
        self.ya_disk.create_catalog('4567')
        assert self.ya_disk.create_catalog('4567') == 409

    def test_create_catalog_404(self):
        assert self.ya_disk.create_catalog('////') == 404

    def test_create_catalog_401(self):
        # В файле находятся не корректные авторизационные данные
        ya_disk_123 = YaUploader('..\\token_yad_false.txt')
        assert ya_disk_123.create_catalog('4567') == 401
