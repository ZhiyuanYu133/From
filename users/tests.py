from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile



from django.test import TestCase
from django.contrib.auth.models import User
import json

test_users = [
    {"username": "testuser1", "password": "testpassword1"},
    {"username": "testuser2", "password": "testpassword2"},
]

class LoginTest(TestCase):
    def setUp(self):
        for user in test_users:
            new_user = User.objects.create(username=user["username"])
            new_user.set_password(user["password"])
            new_user.save()

    def test_login(self):
        USER1 = test_users[0]
        res = self.client.post('/api/token/',
                               data=json.dumps({
                                   'username': USER1["username"],
                                   'password': USER1["password"],
                               }),
                               content_type='application/json',
                               )
        result = json.loads(res.content)
        self.assertTrue("access" in result)


# Create your tests here.
class TestModels(TestCase):

    def setUp(self):
        # Main dummy user for testing 
        self.user = User.objects.create_user(username="test1",
                                    email="test1@domain.com",
                                    password="password1234567890")
        self.profile = Profile.objects.filter(user=self.user).first()
    
    # Test if the Profile is associated with the created user on creation
    def test_profile_associate_with_user_on_creation(self):
        self.assertEquals(self.profile.user, self.user)

    # Testing on linking from Profile to User model (is_active(), email)
    def test_profile_user_email_password(self):
        self.assertEquals(self.profile.user.is_active, True)   # user is not created using POST method, Django default is True
        self.assertEquals(self.profile.user.email, "test1@domain.com")

    # Test if profile_picture is default on creation
    def test_profile_picture_is_default_on_creation(self):
        self.assertEquals(self.profile.profileImage.name, "default.jpg")
        
    # Test if image is default and is resized to 300 * 300 on save
    def test_profile_picture_is_resized(self):
        self.assertEquals(self.profile.profileImage.height, 300)
        self.assertEquals(self.profile.profileImage.width, 300)

    # Test if number of follows is 0
    def test_profile_follow_num_on_creation(self):
        self.assertEquals(self.profile.follows.count(), 0)