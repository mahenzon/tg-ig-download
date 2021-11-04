import pathlib

import instaloader


def main():
    # Get instance
    loader = instaloader.Instaloader()

    # URL = "https://www.instagram.com/p/CVw7-n6MV5A/?utm_medium=copy_link"
    post_shortcode = "CVw7-n6MV5A"

    post = instaloader.Post.from_shortcode(loader.context, post_shortcode)
    target = pathlib.Path("./pic").resolve()
    loader.download_post(post=post, target=target)


if __name__ == "__main__":
    main()
