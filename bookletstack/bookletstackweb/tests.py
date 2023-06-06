from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .user_models import UserDetails
from .product_models import Book, Comment

class UserDetailsModelTestCase(TestCase):
    def setUp(self):
        self.user = UserDetails.objects.create(
            username='Bablu Badmash',
            email='BabluBadmash@gmail.com',
            # Add other required fields here
        )

    def test_user_details_creation(self):
        self.assertEqual(self.user.username, 'Bablu Badmash')
        self.assertEqual(self.user.email, 'BabluBadmash@gmail.com')
        # Add additional assertions to test other fields and behaviors

class BookModelTestCase(TestCase):
    def test_book_creation(self):
        book = Book.objects.create(
            name='Rich Dad, poor dad',
            url='https://example.com/book',
            category='Money',
            rating=0
            # Add other required fields here
        )
        self.assertEqual(book.name, 'Rich Dad, poor dad')
        self.assertEqual(book.category, 'Money')
        self.assertEqual(book.rating, 0)
        # Add additional assertions to test other fields and behaviors

class CommentModelTestCase(TestCase):
    def setUp(self):
        self.user = UserDetails.objects.create(
            username='Bablu Badmash',
            email='BabluBadmash@gmail.com',
            # Add other required fields here
        )
        self.book = Book.objects.create(
            name='Rich Dad, poor dad',
            url='https://example.com/book',
            category='Money',
            rating = 0
            # Add other required fields here
        )

    def test_comment_creation(self):
        comment = Comment.objects.create(
            book=self.book,
            buyer=self.user,
            content='This book is great!',
            rated = 2
            # Add other required fields here
        )
        self.assertEqual(comment.book, self.book)
        self.assertEqual(comment.buyer, self.user)
        self.assertEqual(comment.content, 'This book is great!')
        self.assertEqual(comment.rated, 2)
        # Add additional assertions to test other fields and behaviors
