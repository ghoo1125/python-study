import unittest
# pip intall mock
from mock import patch

from tests.my_module import SomeClass

class TestMock(unittest.TestCase):
    # pach.multiple to mock multiple calls
    @patch('tests.my_module.get_content')
    def test_some_func(self, mock_get_content):
        mock_get_content.return_value = "mock value"
        some_class = SomeClass()
        self.assertEqual(some_class.some_func(), "mock value")
        self.assertEqual(mock_get_content.call_count, 1)
        # mock_get_content.assert_called_once()
