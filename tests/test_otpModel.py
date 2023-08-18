from django.test import TestCase
from django.contrib.auth.models import User
from mobile_otp.models import PhoneNumber

class PhoneNumberModelTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a phone number instance
        self.phone_number = PhoneNumber.objects.create(
            user=self.user,
            phone_number='1234567890',
            is_primary=True
        )

    def test_phone_number_str(self):
        self.assertEqual(str(self.phone_number), '1234567890')

    def test_phone_number_user(self):
        self.assertEqual(self.phone_number.user, self.user)

    def test_phone_number_is_primary(self):
        self.assertTrue(self.phone_number.is_primary)

    def test_phone_number_default_is_primary(self):
        phone_number = PhoneNumber.objects.create(
            user=self.user,
            phone_number='9876543210'
        )
        self.assertFalse(phone_number.is_primary)

    # Add more test cases as needed

    def tearDown(self):
        self.user.delete()
        self.phone_number.delete()

# Add more test classes for other models or functionalities if needed

