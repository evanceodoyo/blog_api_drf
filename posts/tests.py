from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username="testuser", email="testuser@mail.com", password="secret",)


        cls.post = Post.objects.create(author=cls.user, title="A blog title", body="The content of the blog.")
    
    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, 'A blog title')
        self.assertEqual(self.post.body, "The content of the blog.")
        self.assertEqual(str(self.post), "A blog title")
