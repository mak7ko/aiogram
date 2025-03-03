from aiogram.methods import Request, SetPassportDataErrors
from aiogram.types import PassportElementError
from tests.mocked_bot import MockedBot


class TestSetPassportDataErrors:
    async def test_bot_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(SetPassportDataErrors, ok=True, result=True)

        response: bool = await bot.set_passport_data_errors(
            user_id=42, errors=[PassportElementError()]
        )
        request = bot.get_request()
        assert response == prepare_result.result
