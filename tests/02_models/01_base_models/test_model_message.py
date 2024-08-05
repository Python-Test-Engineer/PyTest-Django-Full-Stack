"""Unit tests for Topic model"""

from django.test import TestCase
from base.models import Message, Room, Topic, User


class TestTopicModel(TestCase):
    """Message model test"""

    def test_message_model_exists(self):
        """test Posts model exists"""
        messages = Message.objects.count()
        self.assertEqual(messages, 0)

    def test_str_rep_of_message(self):
        """The Message obkect has an __str__ that returns the first 50 characters of the message body.

        We will test this is the case. We need a User FK and Room FK.
        """
        user = User.objects.create(name="admin")
        room = Room.objects.create(name="Python")
        message = Message.objects.create(
            body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum pulvinar, elit sit amet scelerisque vestibulum, nisi velit semper leo, non imperdiet arcu dui ut dui.",
            user=user,
            room=room,
        )
        len_body = len(message.__str__())
        print(
            f"\nLength of __str__ vs actual lenght : {len_body} v {len(message.body)}"
        )
        self.assertEqual(len_body, 50)
