from unittest import TestCase

from Assignment4 import Assignment4



class TestAssignment4(TestCase):
    """
    Test class for Assignment4 class
    """
    __author__ = "Rajat Kumar"

    def test_connect_table(self):
        """
        Test method for connect_teble() function in the Assignment4 class
        """
        test= Assignment4.connect_table(self)
        self.assertEqual(test, "Connected")

    def test_search_data(self):
        """
           Test method for search_data() function which takes a parameter for id to be searched in the database in the Assignment4 class
        """
        test = Assignment4.search_data(self, "1")
        self.assertEqual(test, "Row")