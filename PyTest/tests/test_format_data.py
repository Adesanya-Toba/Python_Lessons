import pytest

from format_data import (
    format_data_for_display,
    format_data_for_excel,
)

"""In pytest, “fixtures” are functions we define
to prepare everything for our test.

"""


@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]


# Skip these two tests
@pytest.mark.skip(reason="Not yet implemented!")
def test_format_data_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]


@pytest.mark.skip(reason="Not yet implemented!")
def test_format_data_for_excel(example_people_data):
    assert (
        format_data_for_excel(example_people_data)
        == """given,family,title
    Alfonsa,Ruiz,Senior Software Engineer
    Sayid,Khan,Project Manager
    """
    )


CONTENT = "content"


def test_create_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(CONTENT)
    assert p.read_text() == CONTENT
    assert len(list(tmp_path.iterdir())) == 1
    # assert 0
