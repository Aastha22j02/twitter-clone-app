# from django.test import TestCase
# from django.contrib.auth.models import User
# from tweets.models import Tweet, Mention, Retweet

# class TweetAppModelTestCase(TestCase):
#     def setUp(self):
#         self.user1 = User.objects.create_user(username='user1', password='testpassword1')
#         self.user2 = User.objects.create_user(username='user2', password='testpassword2')

#     def test_tweet_creation(self):
#         tweet = Tweet.objects.create(author=self.user1, body='Test tweet content')
#         self.assertEqual(tweet.author, self.user1)
#         self.assertEqual(tweet.body, 'Test tweet content')

#     def test_mention_creation(self):
#         tweet = Tweet.objects.create(author=self.user1, body='Test tweet content')
#         mention = Mention.objects.create(author=self.user2, tweet=tweet, mention='Mention text')
#         self.assertEqual(mention.author, self.user2)
#         self.assertEqual(mention.tweet, tweet)
#         self.assertEqual(mention.mention, 'Mention text')

#     def test_retweet_creation(self):
#         tweet = Tweet.objects.create(author=self.user1, body='Test tweet content')
#         retweet = Retweet.objects.create(author=self.user2, tweet=tweet, retweet='Retweet text')
#         self.assertEqual(retweet.author, self.user2)
#         self.assertEqual(retweet.tweet, tweet)
#         self.assertEqual(retweet.retweet, 'Retweet text')

#     def test_model_str_methods(self):
#         tweet = Tweet.objects.create(author=self.user1, body='Test tweet content')
#         mention = Mention.objects.create(author=self.user2, tweet=tweet, mention='Mention text')
#         retweet = Retweet.objects.create(author=self.user1, tweet=tweet, retweet='Retweet text')

#         self.assertEqual(str(tweet), 'user1 writes Test tweet content...')
#         self.assertEqual(str(mention), 'user2 mention to Test tweet content with Mention text')
#         self.assertEqual(str(retweet), 'user1 retweet to Test tweet content with Retweet text')

#     def test_like_count_property(self):
#         tweet = Tweet.objects.create(author=self.user1, body='Test tweet content')
#         tweet.users_like.add(self.user2)
#         tweet.users_like.add(self.user1)
#         self.assertEqual(tweet.like_count, 2)

#     # Add more test cases for edge cases and other functionalities

#     def tearDown(self):
#         self.user1.delete()
#         self.user2.delete()

# # Add more test classes for other models or functionalities if needed
