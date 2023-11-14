import reflex as rx
from ..styles import (
    input_style,
    button_style,
    question_style,
    answer_style,
    markdown_style,
)
from ..state import State


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


def qa_markdown(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.markdown(
                    question,
                    component_map=markdown_style,
                ),
                style=question_style,
            ),
            text_align="right",
        ),
        rx.box(
            rx.box(
                rx.markdown(
                    answer,
                    component_map=markdown_style,
                ),
                style=answer_style,
            ),
            text_align="left",
        ),
        margin_y="1em",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa_markdown(messages[0], messages[1]),
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
            on_click=State.answer_ai,
            style=button_style,
        ),
    )
