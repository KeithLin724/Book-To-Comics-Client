"""The dashboard page."""
from Book_To_Comics_Client.templates import template

import reflex as rx
from ..state import State

# from ..components import chat_ai_room as chat_com
from ..styles import answer_style, question_style, input_style, button_style


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=answer_style),
            text_align="left",
        ),
        margin_y="1em",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.question,
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


@template(route="/chat", title="Chat")
def chat_ai_room() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.container(
        rx.heading(
            "Chat to AI",
            font_size="3em",
        ),
        chat(),
        action_bar(),
    )
