import pytest

from string_utils import StringUtils

string_utils = StringUtils()
util = StringUtils()

@pytest.mark.parametrize('input_string, expected_result',
[("дом", "Дом"),
("skypro", "Skypro"),
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

def test_contains():
    # positive tests
    assert string_utils.contains('SkyPro', 'S') is True # символ найден
    assert string_utils.contains('skypro', 'skypro') is True # полное совпадение

    # negative tests
    assert string_utils.contains('SkyPro', 'U') is False # символ не найден
    assert string_utils.contains('', 's') is False # пустая строка
    assert string_utils.contains('sky', '') is True # пустая подстрока

def test_delete_symbol():
    # positive tests
    assert string_utils.delete_symbol('SkyPro', 'k') == 'SyPro' # удаление символа
    assert string_utils.delete_symbol('SkyPro123', '123') == 'SkyPro' # удаление символов

    # negative tests
    assert string_utils.delete_symbol('', 's') == '' # пустая строка
    assert string_utils.delete_symbol('SkyPro', 'a') == 'SkyPro' # символ не найден

def test_starts_with():
    # positive tests
    assert string_utils.starts_with('SkyPro', 'S') is True  # символ в начале
    assert string_utils.starts_with('abc', 'a') is True  # символ в начале

    # negative tests
    assert string_utils.starts_with('SkyPro', 'U') is False # символ не найден
    assert string_utils.starts_with('', 's') is False # пустая строка
    assert string_utils.starts_with('SkyPro', 'a') is False  # символ не найден

def test_end_with():
    # positive tests
    assert string_utils.end_with('SkyPro', 'o') is True # окончание совпадает
    assert string_utils.end_with('Sky', 'y') is True  # окончание совпадает

    # negative tests
    assert string_utils.end_with('SkyPro', 'u') is False  # окончание не совпадает
    assert string_utils.end_with('', 'x') is False  # пустая строка
    assert string_utils.end_with('Sky', '_') is False  # окончание не совпадает

def tests_list_to_string():
    # positive tests
    assert string_utils.list_to_string(['a', 'b', 'c'], ',') == 'a,b,c' # разделитель запятая
    assert string_utils.list_to_string(['a', 'b', 'c'], ':') == 'a:b:c'  # разделитель двоеточие

    # negative tests
    assert string_utils.list_to_string(['a', '', 'b', 'c'], ',') == 'a,,b,c'  # отсутствие символа
    assert string_utils.list_to_string([]) == ''  # пустой список
    assert string_utils.list_to_string(['a', '', 'b', 'c'], '') == 'abc'  # список без разделителя