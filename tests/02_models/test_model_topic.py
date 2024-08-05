"""Unit tests for Topic model"""

from django.test import TestCase
from base.models import Topic


class TestTopicModel(TestCase):
    """Topic model test"""

    def test_topic_model_exists(self):
        """test Posts model exists"""
        topics = Topic.objects.count()

        self.assertEqual(topics, 0)

    def test_str_rep_of_objects(self):
        """test __str__"""
        topic = Topic.objects.create(name="First Topic")
        self.assertEqual(topic.name, "First Topic")
