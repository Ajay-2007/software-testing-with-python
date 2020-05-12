from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual(b.title, 'Test')
        self.assertEqual(b.author, 'Test Author')
        self.assertListEqual(b.posts, [])
        # self.assertEqual(len(b.posts), 0)

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b2 = Blog('My Day', 'Rolf')

        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')
        self.assertEqual(b2.__repr__(), 'My Day by Rolf (0 posts)')

    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test Author')
        b2 = Blog('My Day', 'Rolf')
        b.posts = ['test']
        b2.posts = ['test', 'another']

        self.assertEqual(b.__repr__(), 'Test by Test Author (1 post)')
        self.assertEqual(b2.__repr__(), 'My Day by Rolf (2 posts)')

    # def test_create_post(self):
    #     b = Blog('Test', 'Test Author')
    #     p = b.create_post(b.title, 'Test Content')
    #     expected = [{'title': b.title, 'content': 'Test Content'}]
    #     self.assertListEqual(b.posts, expected)

    # def test_json(self):
    #     b = Blog('Test', 'Test Author')
    #     p = b.create_post(b.title, 'Test Content')
    #     json = [{'title': b.title, 'content': 'Test Content'}]
    #     expected = {
    #         'title': b.title,
    #         'author': b.author,
    #         'posts': json,
    #     }
    #
    #     self.assertDictEqual(b.json(), expected)
