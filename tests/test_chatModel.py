from django.test import TestCase
from django.contrib.auth.models import User
from chat.models import Message, Chat

class ChatAppModelTestCase(TestCase):
    def setUp(self):
        # Create users for testing
        self.user1 = User.objects.create_user(username='user1', password='testpassword1')
        self.user2 = User.objects.create_user(username='user2', password='testpassword2')

    def test_message_creation(self):
        message = Message.objects.create(
            sender=self.user1,
            receiver=self.user2,
            content='Hello, user2!'
        )
        self.assertEqual(message.sender, self.user1)
        self.assertEqual(message.receiver, self.user2)
        self.assertEqual(message.content, 'Hello, user2!')
        self.assertFalse(message.is_read)
        self.assertIsNotNone(message.timestamp)

    def test_chat_creation(self):
        chat = Chat.objects.create()
        chat.participants.add(self.user1, self.user2)

        message1 = Message.objects.create(
            sender=self.user1,
            receiver=self.user2,
            content='Message from user1'
        )
        message2 = Message.objects.create(
            sender=self.user2,
            receiver=self.user1,
            content='Message from user2'
        )

        chat.messages.add(message1, message2)
        self.assertEqual(chat.participants.count(), 2)
        self.assertEqual(chat.messages.count(), 2)

    def test_model_str_methods(self):
        message = Message.objects.create(
            sender=self.user1,
            receiver=self.user2,
            content='Hello, user2!'
        )
        chat = Chat.objects.create()
        chat.participants.add(self.user1, self.user2)

        self.assertEqual(str(message), 'user1 -> user2')
        self.assertEqual(str(chat), 'user1, user2')

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()

# Add more test classes for other models or functionalities if needed
