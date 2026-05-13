from django.test import TestCase
from django.contrib.auth.models import User
from profile_app.models import UserProfile
from profile_app.api.serializers import UserProfileSerializer

class UserProfileSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123",
            first_name="Initial",
            last_name="Name",
            email="initial@example.com"
        )
        self.profile = UserProfile.objects.create(user=self.user, type="customer")

    def test_user_profile_update_data(self):
        data = {
            "first_name": "Updated",
            "last_name": "User",
            "email": "test@example.com"
        }
        serializer = UserProfileSerializer(instance=self.profile, data=data, partial=True)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        serializer.save()
        self.user.refresh_from_db()

        self.assertEqual(self.user.first_name,'Updated')
        self.assertEqual(self.user.last_name, 'User')

    def test_read_only_fields_not_updated(self):
        # Încercăm să schimbăm username-ul (care e read_only=True) și type
        data = {
            "username": "hacker_andy",
            "type": "admin",
            "first_name": "NewName"
        }
        serializer = UserProfileSerializer(instance=self.profile, data=data, partial=True)
        self.assertTrue(serializer.is_valid())
        serializer.save()

        self.user.refresh_from_db()
        self.profile.refresh_from_db()

        # Username-ul trebuie să rămână cel vechi
        self.assertEqual(self.user.username, "testuser")
        # Numele trebuie să se schimbe
        self.assertEqual(self.user.first_name, "NewName")