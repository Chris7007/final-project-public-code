from django.test import TestCase


# class YourTestClass(TestCase):
#     @classmethod

#     # Called once at the beginning of the test run for class-level setup.
#     # Use to create objects that aren't going to be modified or changed in any of the test methods.
#     def setUpTestData(cls):
#         print("setUpTestData: Run once to set up non-modified data for all class methods.")
#         pass

#     # Called before every test function to set up any objects that may be modified by the test.
#     # (Every test function will get a "fresh" version of these objects).
#     def setUp(self):
#         print("setUp: Run once for every test method to set up clean data.")
#         pass
    
#     # Test if condition is true.
#     def test_false_is_false(self):
#         print("Method: test_false_is_false.")
#         self.assertFalse(False)

#     # Test if condition is false.
#     def test_false_is_true(self):
#         print("Method: test_false_is_true.")
#         self.assertTrue(False)

#     # Test if condition is equal.
#     def test_one_plus_one_equals_two(self):
#         print("Method: test_one_plus_one_equals_two.")
#         self.assertEqual(1 + 1, 2)# Create your tests here.
