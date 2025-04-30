from googletrans import Translator


#
async def translate_from_language(input_text: str, input_dest: str):
    """
        Определить язык пользователя по координатам по вводу.

        :param input_dest:'ru'
        :return:
    """

    translator = Translator()

    result = await translator.translate(text=input_text, dest=input_dest)

    return result.text
