from __future__ import annotations

from typing import Union

from .base import TelegramMethod


class UnpinAllChatMessages(TelegramMethod[bool]):
    """
    Use this method to clear the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns :code:`True` on success.

    Source: https://core.telegram.org/bots/api#unpinallchatmessages
    """

    __returning__ = bool
    __api_method__ = "unpinAllChatMessages"

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target channel (in the format :code:`@channelusername`)"""
