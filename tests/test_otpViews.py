# from django.test import TestCase, Client
# from django.urls import reverse
# from django.contrib.auth.models import User
# from mobile_otp.models  import PhoneNumber

# class LoginWithOTPViewTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user(username='testuser', password='testpassword')
#         self.phone_number = PhoneNumber.objects.create(
#             user=self.user,
#             phone_number='+911234567890',
#             is_primary=True
#         )

#     def test_login_with_otp_successful(self):
#         response = self.client.post(reverse('login_with_otp'), {'phone_number': '+911234567890'})
#         self.assertEqual(response.status_code, 302)  # Should redirect to verify_otp
#         self.assertEqual(response.url, reverse('verify_otp'))

#     def test_login_with_otp_invalid_phone_number(self):
#         response = self.client.post(reverse('login_with_otp'), {'phone_number': '+918982132095'})
#         self.assertEqual(response.status_code, 302)  # Should redirect back to login_with_otp
#         self.assertEqual(response.url, reverse('login_with_otp'))

#     # Add more test cases as needed

#     def tearDown(self):
#         self.user.delete()
#         self.phone_number.delete()

# # Add more test classes for other views or functionalities if needed
