from jprint import format


def test_dictionary():
    out = format({"a": 1, "b": 2, "c": 3})
    assert out == '{\n    "a": 1,\n    "b": 2,\n    "c": 3\n}'


def test_json_string():
    out = format('{"a": 1, "b": 2, "c": 3}')
    assert out == '''"{\\\"a\\\": 1, \\\"b\\\": 2, \\\"c\\\": 3}"'''


def test_list_of_dicts():
    out = format([{"a": 1, "b": 2, "c": 3}, {"d": 4, "e": 5, "f": 6}])
    assert (
        out
        == '[\n    {\n        "a": 1,\n        "b": 2,\n        "c": 3\n    },\n    {\n        "d": 4,\n        "e": 5,\n        "f": 6\n    }\n]'
    )


def test_non_json_string():
    out = format("This is not a valid JSON string")
    assert out == '"This is not a valid JSON string"'
