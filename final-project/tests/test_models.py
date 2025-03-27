from django.test import TestCase
from models import *


class ReportsTestClass(TestCase):
    @classmethod

    # Called once at the beginning of the test run for class-level setup.
    def setUpTestData(cls):
        User.objects.create(first_name='Bob', last_name='Job', username='Bobajob', password='pw', email='cjb@gmail.com', 
            is_superuser=False, is_staff=False, is_active=True, date_joined='2022-10-22 08:00:15.0+00:00', 
            last_login=None)
        Demos.objects.create(userid=User(pk=1), title='Angry Birds')
        Reports.objects.create(demo_id_report=Demos(pk=1), user_id_report=User(pk=1), report='test')

    # Test for correct object name ()
    def test_object_name_is_correct(self):
        reports = Reports.objects.get(id=1)
        expected_object_name = f"{reports.demo_id_report} {reports.timedate}"
        self.assertEqual(str(reports), expected_object_name)

    # Test fields which have defaults are set correctly with no input
    def test_correct_defaults_are_set(self):
        reports = Reports.objects.get(id=1)
        self.assertFalse(reports.read)

    # Test the maximum field lengths are correct (where applicable).
    def test_for_correct_max_lengths(self):
        reports = Reports.objects.get(id=1)
        max_length = reports._meta.get_field('report').max_length
        self.assertEqual(max_length, 512)
        max_length = reports._meta.get_field('action').max_length
        self.assertEqual(max_length, 512)

    # Test for correct null, blank and unique fields
    def test_for_correct_null_and_blank_fields(self):
        reports = Reports.objects.get(id=1)
        isNullBlankUnique = reports._meta.get_field('user_id_report')
        self.assertTrue(isNullBlankUnique.null)
        self.assertFalse(isNullBlankUnique.blank and isNullBlankUnique.unique)
        isNullBlankUnique = reports._meta.get_field('demo_id_report')
        self.assertTrue(isNullBlankUnique.null)
        self.assertFalse(isNullBlankUnique.blank and isNullBlankUnique.unique)
        isNullBlankUnique = reports._meta.get_field('report')
        self.assertFalse(isNullBlankUnique.null and isNullBlankUnique.blank and isNullBlankUnique.unique)
        isNullBlankUnique = reports._meta.get_field('read')
        self.assertFalse(isNullBlankUnique.null and isNullBlankUnique.blank and isNullBlankUnique.unique)
        isNullBlankUnique = reports._meta.get_field('action')
        self.assertTrue(isNullBlankUnique.null and isNullBlankUnique.blank)
        self.assertFalse(isNullBlankUnique.unique)
        isNullBlankUnique = reports._meta.get_field('timedate')
        self.assertFalse(isNullBlankUnique.null and isNullBlankUnique.blank and isNullBlankUnique.unique)
        isNullBlankUnique = reports._meta.get_field('user_pk')
        self.assertTrue(isNullBlankUnique.null and isNullBlankUnique.blank)
        self.assertFalse(isNullBlankUnique.unique)
        isNullBlankUnique = reports._meta.get_field('demo_pk')
        self.assertTrue(isNullBlankUnique.null and isNullBlankUnique.blank)
        self.assertFalse(isNullBlankUnique.unique)


