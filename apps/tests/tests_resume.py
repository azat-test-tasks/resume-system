from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from apps.resume.models import Resume


class ResumeTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.token = Token.objects.create(user=self.user)
        self.resume = Resume.objects.create(
            owner=self.user,
            title="Test Resume",
            phone="+1234567890",
            email="test@test.com",
            specialty="Test Specialty",
            salary=50000,
            education="Test Education",
            status="Test Status",
            grade="Test Grade",
            experience="Test Experience",
            portfolio="https://test-portfolio.com",
        )

    def test_get_resume_list(self):
        """
        Ensure we can retrieve a list of resume
        """
        url = reverse("resume-list")
        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_resume_authenticated(self):
        url = reverse("resume-detail", kwargs={"pk": self.resume.id})
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        data = {
            "title": "Test Resume 1 Updated",
        }
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Resume.objects.get(id=self.resume.id).title, "Test Resume 1 Updated"
        )

    def test_patch_resume_wrong_user(self):
        """
        Ensure we cannot update a resume if the user is not the owner
        """
        url = reverse("resume-detail", args=[self.resume.id])
        self.client.force_authenticate(user=None)
        data = {
            "title": "Test Resume 1 Updated",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
