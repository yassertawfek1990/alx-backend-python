#!/usr/bin/env python3
"""jkbskd vkjn lkjasnv knlkndafkvnl klkjnlkdfvn kjnjnlnfdavln lkv"""
import unittest
import requests
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """knks dvkjn klnldkfnv lkjnkln dslknv kjjnldfv klxzk m;ldffv dfv"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        """kbl dfv kjlnkldfnv lkkjn ldskfnv n; ijadv ih erv knl;m ldsvoii"""
        response = access_nested_map(nested_map, path)
        self.assertEqual(response, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """bklsldv kjnkjsdvn kljjnkjlsdvn k nlkv;fdv pok ervk o;o;kov olkl"""
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """hjblkjas kjnskjdnvlkjnkjasvn nkjljnlkdafvjn lkdfvnlkjn lkadfnv ldf"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        """sdbkj sdkjnkj lsdnlkj jkljsdnckjn kjknkjsdckjkjnsd"""
        mock_requests_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_requests_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """jbk ksdjknkj lkjdsn cjnlkjdsc kjnkjdsc jnlksddnkjlndslkdc sdsds"""
    def test_memoize(self):
        """sdnjklk sdjkn kjsdn klnlkn kjnsdc kjds kn"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_object:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock_object.assert_called_once()
