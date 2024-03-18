from django.test import TestCase
from rest_framework.test import APIClient
from .models import Task

# TaskAPITest inherits from TestCase, providing a framework for writing test cases for the Task API.
class TaskAPITest(TestCase):
    # This setUp method is run before every test method to set up any objects or state that the test needs
    def setUp(self):
        self.client = APIClient()                   # APIClient is a DRF class that acts as a client for making requests to the api for testing purpose
        self.task = Task.objects.create(title="Test Task", description="This is a test task description...", status="To Do")    # Here we are creating a task instance to use in our tests

    # To test API's ability to retrieve a list of tasks
    def test_get_tasks(self):
        response = self.client.get('/api/tasks/')   # we make a get request to the API endpoint that lists tasks
        self.assertEqual(response.status_code, 200) # Asserts the response that status code is 200 (OK), indicating the request was successful
        self.assertEqual(len(response.data), 1)     # Asserts that response contains only one task, which we setup in setUp

    # To test the API ability to create new task
    def test_create_task(self):
        data = {'title': 'New Task', 'description': 'This is a new task description....', 'status': 'TO_DO'}   # Dictionary that represents a new task that we want to create
        response = self.client.post('/api/tasks/', data) # creates a net task
        self.assertEqual(response.status_code, 201)      # Assert that the response status code is 201 (CREATED), indicating the task was successfully created
        tasks = Task.objects.filter(title="New Task")
        self.assertEqual(tasks.count(), 1)               # Assert that there are now two objects in the database- The one we setup in the setUp method and the one we just createed

    # To test the API ability to create new task without title
    def test_create_task_without_title(self):
        data = {'Description': 'This is a new task without title...', 'status': 'TO_DO'}
        response = self.client.post("/api/tasks/", data)
        self.assertEqual(response.status_code, 400)

    def test_create_task_title_length(self):
        data1 = {'title': 'A', 'description': 'description....', 'status': 'TO_DO'}
        response1 = self.client.post('/api/tasks/', data1, format='json')
        self.assertEqual(response1.status_code,400)
        self.assertEqual(response1.data['title'][0],'Title must be at least 3 characters long.')

        data2 = {'title': 'Abcdef', 'description': 'description....', 'status': 'TO_DO'}
        response2 = self.client.post('/api/tasks/', data2, format='json')
        self.assertEqual(response2.status_code,201)

    # To test the API ability to create new task without description
    def test_create_task_without_description(self):
        data = {'title': 'New Task Without Description', 'status': 'TO_DO'}
        response = self.client.post('/api/tasks/',  data, format='json')
        self.assertEqual(response.status_code, 201)
        task = Task.objects.filter(title='New Task Without Description')
        self.assertEqual(task.count(), 1)
        self.assertEqual(task.first().description, '')

    # To test the API ability to create new task without status
    def test_create_task_without_status(self):
        data = {'title': 'Task without status', 'description': 'This is a new task without status desc...'}
        response = self.client.post('/api/tasks/', data, format='json')
        self.assertEqual(response.status_code, 201)
        tasks = Task.objects.filter(title="Task without status")
        self.assertEqual(tasks.count(), 1)
        task = tasks.first()
        self.assertEqual(task.status, 'TO_DO')


