from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from chat.models import Message, Chat

class ChatAppViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='user1', password='testpassword1')
        self.user2 = User.objects.create_user(username='user2', password='testpassword2')

    def test_send_message(self):
        self.client.login(username='user1', password='testpassword1')
        response = self.client.get(reverse('send_message', args=[self.user2.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/send_message.html')

        # Simulate sending a message
        message_content = "Hello, user2!"
        response = self.client.post(reverse('send_message', args=[self.user2.id]), {'content': message_content})
        self.assertEqual(response.status_code, 302)  # Should redirect after sending

        # Retrieve the created message and verify its content
        chat = Chat.objects.filter(participants=self.user1).filter(participants=self.user2).first()
        self.assertIsNotNone(chat)
        messages = chat.messages.all()
        self.assertEqual(len(messages), 1)
        sent_message = messages[0]
        self.assertEqual(sent_message.sender, self.user1)
        self.assertEqual(sent_message.receiver, self.user2)
        self.assertEqual(sent_message.content, message_content)

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()

# Add more test classes for other views or functionalities if needed
