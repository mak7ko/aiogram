from __future__ import annotations

from typing import Union

from .base import TelegramMethod


class DeleteChatPhoto(TelegramMethod[bool]):
    """
    Use this method to delete a chat photo. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns :code:`True` on success.

    Source: https://core.telegram.org/bots/api#deletechatphoto
    """

    __returning__ = bool
    __api_method__ = "deleteChatPhoto"

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target channel (in the format :code:`@channelusername`)"""
