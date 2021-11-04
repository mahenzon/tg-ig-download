import pytest

from filtering import instagram_post_link_shortcode_re


@pytest.mark.parametrize(
    "text, codes",
    [
        pytest.param(
            """https://www.instagram.com/p/CNZ8GngF3M0/?utm_medium=copy_link
ну например что-то такое
https://www.instagram.com/p/CVyI_lyMYhK/?utm_medium=copy_link
в принципе ок
ну например что-то такое
https://www.instagram.com/p/CQOJnCzHr24/?utm_medium=copy_link
https://www.instagram.com/p/CVyI_lyMYhK/
в принципе ок
https://www.instagram.com/p/CVc6G4DMt6X/
https://www.instagram.com/p/CVyI_lyMabc
https://www.instagram.com/p/CVyIalylalz/""",
            [
                "CNZ8GngF3M0",
                "CVyI_lyMYhK",
                "CQOJnCzHr24",
                "CVyI_lyMYhK",
                "CVc6G4DMt6X",
                "CVyI_lyMabc",
                "CVyIalylalz",
            ],
            id="regex-matches-shortcode",
        ),
    ],
)
def test_matches_shortcodes(text, codes):
    regexp = instagram_post_link_shortcode_re
    matches = regexp.findall(text)
    assert matches == codes
