import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize('input_str, expected', [
    ('привет', 'Привет'),
    ('hellow world!', 'Hellow world!'),
    ('день 1', 'День 1'),
    ('0ABC', '0abc'),
    ('  ', '  '),
    (' abc', ' abc'),
    ('False', 'False'),
    ('[1, 2]', '[1, 2]')
    ])
def test_positive_capitalize(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
def test_positive_capitalize_empty_string():
    string_utils = StringUtils()
    res = string_utils.capitalize('')
    assert res == ''
    assert len(res) == 0


@pytest.mark.negative
def test_negative_capitalize_type():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.capitalize(1)


@pytest.mark.negative
def test_negative_capitalize_list():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.capitalize([1, 2])


@pytest.mark.negative
def test_negative_capitalize_none():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)


@pytest.mark.positive
@pytest.mark.parametrize('string, expected', [
    (' Hellow', 'Hellow'),
    (' _hellow world!', '_hellow world!'),
    (' 1!@', '1!@'),
    (' False ', 'False '),
    ('    [1, 2]', '[1, 2]')
    ])
def test_positive_trim(string, expected):
    assert string_utils.trim(string) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_str, expected', [
    ('   ', ''),
    ('', '')
    ])
def test_negative_trim_empty(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
def test_negative_trim_none():
    with pytest.raises(AttributeError):
        string_utils.trim(None)


@pytest.mark.positive
@pytest.mark.parametrize('string, symbol, expected', [
    ('abc', 'a', True),
    ('123', '2', True),
    ('!@_', '_', True),
    ('test', 'test'[0], True),
    ('test', 'test'[-1], True),
    ('abc', 'd', False),
    ('  ', 't', False)
    ])
def test_positive_contains(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_str, input_symbol, expected', [
    ('test', 'testic', False), ('test', '', True)])
def test_negative_contains_specify(input_str, input_symbol, expected):
    assert string_utils.contains(input_str, input_symbol) == expected


@pytest.mark.negative
def test_negative_contains_none():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.contains(None, None)


@pytest.mark.negative
def test_negative_contains_none_string():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.contains(None, 'w')


@pytest.mark.negative
def test_negative_contains_none_simbol():
    string_utils = StringUtils()
    with pytest.raises(TypeError):
        string_utils.contains('hellow', None)


@pytest.mark.positive
@pytest.mark.parametrize('string, symbol, expected', [
    ('test', 't', 'es'),
    ('test', 'e', 'tst'),
    ('test', '', 'test'),
    ('test', '1', 'test'),
    ('test', 'test'[1], 'tst'),
    ('  ', 't', '  ')
    ])
def test_positive_delete_symbol(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
def test_delete_symbol_empty_string():
    string_utils = StringUtils()
    res = string_utils.delete_symbol('', 't')
    assert res == ''


@pytest.mark.negative
@pytest.mark.xfail(strict=False, reason="если вместо символа отправить пустоту?")
def test_negative_delete_symbol_none():
    string_utils = StringUtils()
    with pytest.raises(TypeError, match="index() argument 1 must be str, not None"):
        string_utils.delete_symbol('test', None)


@pytest.mark.negative
@pytest.mark.xfail(strict=False, reason="если вместо строки отправить пустоту?")
def test_negative_delete_str_none():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.delete_symbol('test', None)
