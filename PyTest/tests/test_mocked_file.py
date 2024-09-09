import mocked_file


# tests/test_my_module.py
# from unittest.mock import mock_open, patch


# @patch("mocked_file.open", new_callable=mock_open, read_data="mocked file content")
# def test_file_read(mock_file):
#     # Importing the module after mocking the open function
#     import mocked_file

#     # Check if the data read from the file is as expected
#     assert mocked_file.get_data() == "mocked file content"


def test_file_creation(tmp_path):
    d = tmp_path / "junit"
    d.mkdir()
    p = d / "mocked-file.txt"
    p.write_text("content", encoding="utf-8")
    assert p.read_text() == "content"


def test_mocked_file(tmp_path):
    assert mocked_file.get_data() == "content"
