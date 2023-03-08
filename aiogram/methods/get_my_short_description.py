from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional

from ..types import BotShortDescription
from .base import Request, TelegramMethod

if TYPE_CHECKING:
    from ..client.bot import Bot


class GetMyShortDescription(TelegramMethod[BotShortDescription]):
    """
    Use this method to get the current bot short description for the given user language. Returns :class:`aiogram.types.bot_short_description.BotShortDescription` on success.

    Source: https://core.telegram.org/bots/api#getmyshortdescription
    """

    __returning__ = BotShortDescription

    language_code: Optional[str] = None
    """A two-letter ISO 639-1 language code or an empty string"""

    def build_request(self, bot: Bot) -> Request:
        data: Dict[str, Any] = self.dict()

        return Request(method="getMyShortDescription", data=data)
