'''
注意：此文件是针对以下类的测试文件。
你可以在此文件同一文件夹下新建shopping_list.py，并复制以下内容到该文件：

class ShoppingList:
    """初始化购物清单，shopping_list是字典类型，包含商品名和对应价格
    例子：{"牙刷": 5, "沐浴露": 15, "电池": 7}"""
    def __init__(self, shopping_list):
        self.shopping_list = shopping_list

    """返回购物清单上有多少项商品"""
    def get_item_count(self):
        return len(self.shopping_list)

    """返回购物清单商品价格总额数字"""
    def get_total_price(self):
        total_price = 0
        for price in self.shopping_list.values():
            total_price += price
        return total_price
'''

import unittest
from shopping_list import ShoppingList

class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.shopping_list = ShoppingList({"纸巾": 8, "帽子": 30, "拖鞋": 15})

    def test_get_item_count(self):
        self.assertEqual(self.shopping_list.get_item_count(), 3)

    def test_get_total_price(self):
        self.assertEqual(self.shopping_list.get_total_price(), 55)