from django.test import TestCase
from models import *
from .model_factories import *
import logging
logger = logging.getLogger(__name__)

class ViewsTestClass(TestCase):
    user1 = None
    user2 = None
    user3 = None
    userProfile1 = None
    userProfile2 = None
    userProfile3 = None
    good_url = ''
    bad_url = ''

    def setUp(self):
        self.good_url = 'user/1'
        self.bad_url = '/user/H/'

        # create user profile 1
        self.user = User.objects.create_user(username="testuser", password="password2025")
        newUserID = self.user.id
        self.userProfile = UserProfileFactory.create(user_id = newUserID)
        self.userProfile.is_verified = True
        self.userProfile.save() # saves new user profile to DB

        # create user profile 2
        self.user = User.objects.create_user(username="testuser2", password="password2025")
        newUserID = self.user.id
        self.userProfile = UserProfileFactory.create(user_id = newUserID)
        self.userProfile.is_verified = True
        self.userProfile.save() # saves new user profile to DB

        # create user profile 3
        self.user = User.objects.create_user(username="testuser3", password="password2025")
        newUserID = self.user.id
        self.userProfile = UserProfileFactory.create(user_id = newUserID)
        self.userProfile.is_verified = True
        self.userProfile.save() # saves new user profile to DB

        # create some demos for each user
        self.demo1 = Demos.objects.create(userid_id=1, title='PacMan', hide_from_all=False, category='Desktop Games', description='Retro game')
        self.demo2 = Demos.objects.create(userid_id=1, title='Asteroids', hide_from_all=False, category='Mobile Games', description='Retro game')
        self.demo3 = Demos.objects.create(userid_id=2, title='Water', hide_from_all=False, category='Shaders', description='Water shader created in Unity')
        self.demo4 = Demos.objects.create(userid_id=3, title='Fire', hide_from_all=False, category='Shaders', description='Fire shader created in Unity')
        self.demo5 = Demos.objects.create(userid_id=1, title='Earth', hide_from_all=True, category='Shaders', description='Earth shader created in Unity')
        
        # create some favourites for each user
        self.fav1 = Favourites.objects.create(user_id_favs_id=1, demo_id_favs_id=1)
        self.fav2 = Favourites.objects.create(user_id_favs_id=3, demo_id_favs_id=3)

        # create a project
        self.event1 = Event.objects.create(user_id_leader=User(pk=1), event_title='Angry Birds', day='2022-10-22',
            start_time='08:00:15.0+00:00', end_time='09:00:15.0+00:00', event_description='test', meeting_details='test')

    def tearDown(self):
        Demos.objects.all().delete()
        UserProfile.objects.all().delete()
        User.objects.all().delete()


    '''
    ***********************************************************************************************
    ***************      ABOUT PAGE - Various tests associated with about page      ***************
    ***********************************************************************************************
    '''
    def test_about_page_user_access_if_no_login(self):
        logger.warning('\nTesting About page')
        # Check any user can access the about page
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)


    '''
    ***********************************************************************************************
    **********       REPORT PAGE - Various tests associated with report page       **********
    ***********************************************************************************************
    '''
    def test_report_page_no_access_if_no_login(self):
        logger.warning('\nTesting Report page')
        # Check if the user is not logged in there is no access to report page and is redirected
        response = self.client.get('/report/1') # report demo 1
        self.assertEqual(response.status_code, 302)

    def test_report_page_user_has_access_if_login(self):
        # Log in the user
        self.client.login(username="testuser", password="password2025")

        # Check the user can access report page
        response = self.client.get('/report/1') # report demo 1
        self.assertEqual(response.status_code, 200)

    def test_report_page_user_login_invalid_demo(self):
        # Log in the user
        self.client.login(username="testuser", password="password2025")
        
        # Check error if the user reports invalid demo
        response = self.client.get('/report/789') # report invalid demo
        self.assertEqual(response.status_code, 302) # error redirect

    def test_report_page_POST_form(self): 
        # Log in the user
        self.client.login(username="testuser", password="password2025")

        # post invalid test form (no text)
        response = self.client.post('/report/1', {'report_form':''})
        self.assertEqual(response.status_code, 200) # post not successful, no redirect keep existing fields

        # post invalid test form (no post name)
        response = self.client.post('/report/1', {'report':'test'})
        self.assertEqual(response.status_code, 200) # post not successful, no redirect keep existing fields

        # post valid test form
        response = self.client.post('/report/1', {'report':'test', 'report_form':''})
        self.assertEqual(response.status_code, 302) # success and redirect
        self.assertEqual(response.url, "/") # redirect to index page


