from django.test import TestCase
from django.contrib.auth.models import User
import json, uuid

test_user = {"username": "testuser", "password": "testpassword"}

class PostsTest(TestCase):
    def setUp(self):
        new_user = User.objects.create(
            username=test_user["username"])
        new_user.set_password(test_user["password"])
        new_user.save()

    def get_token(self):
        res = self.client.post('/api/token/',
           data=json.dumps({
               'username': test_user["username"],
               'password': test_user["password"],
           }),
           content_type='application/json',
           )
        result = json.loads(res.content)
        self.assertTrue("access" in result)
        return result["access"]


def test_get_posts(self):
    token = self.get_token()
    post_id_1 = uuid.uuid4
    post_id_2 = uuid.uuid4
    res = self.client.post('/api/posts/',
                           data=json.dumps({
                               'type': "post",
                               'title': "Post Title",
                               'id': post_id_1,
                               'content': "Here are some post content",
                           }),
                           content_type='application/json',
                           HTTP_AUTHORIZATION=f'Bearer {token}'
                           )
    self.assertEquals(res.status_code, 201)
    id1 = json.loads(res.content)["data"]["id"]

    res = self.client.post('/api/orders/',
                           data=json.dumps({
                               'type': "post",
                               'title': "Post 2 Title",
                               'id': post_id_2,
                               'content': "Here are some post content for post 2",
                           }),
                           content_type='application/json',
                           HTTP_AUTHORIZATION=f'Bearer {token}'
                           )
    self.assertEquals(res.status_code, 201)
    id2 = json.loads(res.content)["data"]["id"]

    res = self.client.get('/api/orders/',
                          content_type='application/json',
                          HTTP_AUTHORIZATION=f'Bearer {token}'
                          )

    self.assertEquals(res.status_code, 200)
    result = json.loads(res.content)["data"]
    self.assertEquals(len(result), 2)
    self.assertTrue(result[0]["id"] == id1 or result[1]["id"] == id1)
    self.assertTrue(result[0]["id"] == id2 or result[1]["id"] == id2)

    res = self.client.get(f'/api/orders/{id1}/',
                          content_type='application/json',
                          HTTP_AUTHORIZATION=f'Bearer {token}'
                          )
    self.assertEquals(res.status_code, 200)
    result = json.loads(res.content)["data"]
    self.assertEquals(result["type"], 'post')
    self.assertEquals(result["title"], 'Post Title')
    self.assertEquals(result["id"], post_id_1)
    self.assertEquals(result["content"], "Here are some post content")