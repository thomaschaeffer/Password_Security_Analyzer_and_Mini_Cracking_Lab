from password_security_lab.analyzer.patterns import (
    detection_repetition,
    detection_sequence,
    detection_block_bis,
    filter_block,
    detection_date,
    replace_substitutions
)


def test_detection_repetition():

    # No repetition
    assert detection_repetition("abcdef") == {}

    # One repetition
    assert detection_repetition("abcdd") == {
        "dd": {"d": 2}
    }

    # Several different repetitions
    assert detection_repetition("aaabbbcccc") == {
        "aaa": {"a": 3},
        "bbb": {"b": 3},
        "cccc": {"c": 4}
    }

    # Same repeated sequence several times
    assert detection_repetition("aaabbbcccaaa") == {
        "aaa": {"a": 3},
        "bbb": {"b": 3},
        "ccc": {"c": 3},
        "aaa_": {"a": 3}
    }

    # Repetition at the beginning
    assert detection_repetition("aaaaabc") == {
        "aaaaa": {"a": 5}
    }

    # Repetition at the end
    assert detection_repetition("abcdddd") == {
        "dddd": {"d": 4}
    }


def test_detection_sequence():

    # No sequence
    assert detection_sequence("abcdef") == ["abcdef"]

    # Numeric sequence
    assert detection_sequence("123456") == ["123456"]

    # Alphabetic sequence
    assert detection_sequence("abcdefg") == ["abcdefg"]

    # Several sequences
    assert detection_sequence("123456abcdefg") == [
        "123456",
        "abcdefg"
    ]

    # Sequence inside a password
    assert detection_sequence("abc123456def") == [
        "abc",
        "123456",
        "def"
    ]

    # Sequence with no repetition
    assert detection_sequence("a1b2c3") == []

    # Difference of zero is not a sequence
    assert detection_sequence("4444") == []


def test_detection_block_bis():

    # No repeated block
    assert detection_block_bis("abcdef") == {}

    # Simple repeated block
    assert detection_block_bis("abab")["ab"] == [0, 2]

    # Repeated block separated by other characters
    assert detection_block_bis("abxxxxab")["ab"] == [0, 6]

    # Several occurrences
    assert detection_block_bis("abasdfgsfjabab")["ab"] == [0, 10, 12]

    # Different repeated blocks
    result = detection_block_bis("abcabc")
    assert result["abc"] == [0, 3]


def test_filter_block():

    # Nothing to filter
    blocks = {
        "ab": [0, 2]
    }

    assert filter_block(blocks) == {
        "ab": [0, 2]
    }

    # Smaller block completely covered by a larger block
    blocks = {
        "ab": [0, 4],
        "abab": [0, 4]
    }

    assert filter_block(blocks) == {
        "abab": [0, 4]
    }

    # Smaller block has an independent occurrence
    blocks = {
        "ab": [0, 4, 10],
        "abab": [0, 4]
    }

    assert filter_block(blocks) == {
        "ab": [0, 4, 10],
        "abab": [0, 4]
    }

    # Different motifs should not be confused
    blocks = {
        "ab": [0, 4],
        "ba": [1, 5]
    }

    assert filter_block(blocks) == blocks


def test_detection_date():

    # No date
    assert detection_date("abcdef") == []

    # Date without separator
    assert detection_date("191223") == [
        "191223"
    ]

    # Date with separators
    assert detection_date("19/12/23") == [
        "19/12/23"
    ]

    #Date with seperators and not at the beginning
    assert detection_date("abc19/12/2023def") == [
        "19/12/2023"
    ]

    # Date with different separators
    assert detection_date("19-12-23") == [
        "19-12-23"
    ]

    # Invalid day
    assert detection_date("321223") == []

    # Invalid month
    assert detection_date("191323") == []

    # Valid standalone year
    assert detection_date("2026") == [
        "2026"
    ]

    # Year outside the accepted range
    assert detection_date("1899") == []
    assert detection_date("2027") == []


def test_replace_substitutions():

    # No substitution
    assert replace_substitutions("password") == "password"

    # Single substitution
    assert replace_substitutions("p@ssword") == "password"

    # Several substitutions
    assert replace_substitutions("p@ssw0rd") == "password"

    # Numbers used as letters
    assert replace_substitutions("l3tme1n") == "letmein"

    # Uppercase should be converted to lowercase
    assert replace_substitutions("P@SSW0RD") == "password"

    # No modification for normal characters
    assert replace_substitutions("abcdef") == "abcdef"