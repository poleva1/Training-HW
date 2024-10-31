import pytest

from string_utils import StringUtils


util = StringUtils()

   # def setup_method(self):
    #     self.utils = StringUtils()

    # def test_capitalize(self):
    #     assert self.utils.capitilize("hello") == "Hello"
    #     assert self.utils.capitilize("Hello") == "Hello"
    #     assert self.utils.capitilize("") == ""
    #     assert self.utils.capitilize("123") == "123"

@pytest.mark.parametrize('input_string, expected_result',
[("дом", "Дом"),
("Skypro", "Skypro"),
("hello, world", "Hello, world"),
("123", "123")
])
def test_capitilize(input_string, expected_result):
    res = util.capitilize(input_string)
    assert res == expected_result

@pytest.mark.parametrize('input_string, expected_result',
[(" дом", "дом"),
(" Skypro", "Skypro"),
(" hello, world", "hello, world"),
(" 123", "123")
])
def test_trim(input_string, expected_result):
    res = util.trim(input_string)
    assert res == expected_result

def test_to_list():
    res = util.to_list("a,b,c,d")
    assert res == ["a", "b", "c", "d"]



