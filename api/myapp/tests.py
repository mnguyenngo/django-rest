# from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Task
from .serializers import TaskSerializer

# Create your tests here.


# tests for views
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_task(title="", assignee=""):
        if title != "" and assignee != "":
            Task.objects.create(title=title, assignee=assignee)

    def setUp(self):
        # add test data
        self.create_task("walk dog", "Nguyen")
        self.create_task("buy milk", "Nguyen")
        self.create_task("call Mom", "Tobey")
        self.create_task("submit homework", "Nguyen")


class GetAllTasksTest(BaseViewTest):

    def test_get_all_tasks(self):
        """
        This test ensures that all tasks added in the setUp method
        exist when we make a GET request to the tasks/ endpoint
        """
        # hit the API endpoint
        response = self.client.get("/tasks/?format=json")

        # fetch the data from db
        expected = Task.objects.all()
        serialized = TaskSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
