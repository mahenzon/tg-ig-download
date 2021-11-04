import re

from aiogram.dispatcher.filters import Regexp

instagram_post_link_shortcode_re = re.compile(
    r"instagram\.com/p/(?P<short_code>\w+)/?",
    flags=re.IGNORECASE | re.MULTILINE,
)
instagram_post_link_shortcode_filter = Regexp(instagram_post_link_shortcode_re)
