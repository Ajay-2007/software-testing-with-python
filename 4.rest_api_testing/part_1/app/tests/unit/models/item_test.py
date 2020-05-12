from unittest import TestCase

from models.item import ItemModel



class TestItem(TestCase):

    def test_create_item(self):
        item = ItemModel('test', 42)

        self.assertEqual(item.name, 'test',
                         'The name of the item after creation is not equal to the constructor argument')
        self.assertEqual(item.price, 42,
                         'The price of the item after creation is not equal to the constructor argument')


    def test_item_json(self):
        item = ItemModel('test', 42)
        expected = {
            'name' : item.name,
            'price' : item.price,
        }

        self.assertEqual(item.json(), expected,
                         f'The JSON export of the item is incorrect. Recieved {item.json()}, expected {expected}')