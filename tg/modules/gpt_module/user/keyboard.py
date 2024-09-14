from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup


def start_kb():
    """This function creates a keyboard with one button that says "Give me the mouse".
    The button has a callback data of "hi_bot".

    Returns
    -------
        InlineKeyboardMarkup: The keyboard with the button.

    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Give me the mouse", callback_data="hi_bot")],
        ]
    )
    return keyboard
