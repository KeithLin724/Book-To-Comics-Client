import reflex as rx
from ..styles import input_style, button_style
from ..state import State


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Ask a question",
            on_change=State.set_question,
            style=input_style,
        ),
        rx.button(
            "Ask",
            on_click=State.answer,
            style=button_style,
        ),
    )
