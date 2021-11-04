import logging
import tempfile
from pathlib import Path
from typing import Awaitable, Coroutine

import instaloader
from aiogram import types
from instaloader import LoginRequiredException

from utils import wrap_sync

log = logging.getLogger(__name__)

loader = instaloader.Instaloader()


def save_pictures(shortcode: str, save_path=None) -> Path:
    """
    :param shortcode:
    :param save_path:
    :return: directory where data is saved
    :rtype: str
    """
    if not save_path:
        save_path = tempfile.mkdtemp(suffix=shortcode)
        log.info("created temporary directory %r", save_path)

    dirname = Path(save_path)

    log.info("start downloading post %s to directory %r", shortcode, dirname)
    post = instaloader.Post.from_shortcode(loader.context, shortcode)
    loader.download_post(post=post, target=dirname)
    log.info("downloaded post to directory %r", dirname)

    return dirname


@wrap_sync
def save_pics_async(shortcode: str) -> Awaitable[Path]:
    # noinspection PyTypeChecker
    return save_pictures(shortcode)


@wrap_sync
def create_media_group(post_data_path: Path) -> tuple[types.MediaGroup, str]:
    caption_text = None
    input_medias = []
    for path in post_data_path.iterdir():
        if path.suffix == ".jpg":
            media = types.InputFile(path)
            media_photo = types.InputMediaPhoto(media)
            input_medias.append(media_photo)
        elif path.suffix == ".mp4":
            media = types.InputFile(path)
            media_video = types.InputMediaVideo(media)
            input_medias.append(media_video)
        elif path.suffix == ".txt":
            caption_text = path.read_text()

    extra_text = None
    if len(caption_text) > 1000:
        extra_text = caption_text
    else:
        input_medias[0].caption = caption_text

    media = types.MediaGroup(input_medias)
    return media, extra_text


async def load_and_send_post(message: types.Message, shortcode: str):
    post_data_path: Path = await save_pics_async(shortcode)

    # noinspection PyTypeChecker
    create_media_coro: Coroutine = create_media_group(post_data_path)
    media, extra_text = await create_media_coro
    messages = await message.reply_media_group(
        media=media,
        allow_sending_without_reply=True,
    )
    if extra_text:
        first_message_in_group = messages[0]
        res = await first_message_in_group.reply(extra_text)
        messages.append(res)

    return messages


async def load_and_send_post_safe(message: types.Message, shortcode: str):
    log.info("start loading posts for shortcode %s", shortcode)
    try:
        return await load_and_send_post(message, shortcode)
    except LoginRequiredException:
        await message.reply("can't help, IG requires login :(")
    except Exception:
        log.exception("Error loading post! %s", shortcode)
