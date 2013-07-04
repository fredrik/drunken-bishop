from drunken_bishop import drunken_bishop


def test_drunken_bishop():
    fingerprint = "37:e4:6a:2d:48:38:1a:0a:f3:72:6d:d9:17:6b:bd:5e"
    expected_art = """
+-----------------+
|                 |
|                 |
|          .      |
|     .   o       |
|o . o . S +      |
|.+ + = . B .     |
|o + + o B o E    |
| o .   + . o     |
|         .o      |
+-----------------+
    """.strip()
    assert drunken_bishop(fingerprint) == expected_art
