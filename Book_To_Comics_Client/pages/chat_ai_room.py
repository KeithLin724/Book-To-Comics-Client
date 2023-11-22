"""The dashboard page."""
from Book_To_Comics_Client.templates import template
from Book_To_Comics_Client.components import chat_ai_room as chat_ai
from Book_To_Comics_Client.styles import markdown_style

import reflex as rx

# from ..components import chat_ai_room as chat_com


@template(route="/chat", title="Chat")
def chat_ai_room() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.heading(
            "Chat to AI",
            font_size="3em",
        ),
        rx.markdown(
            "---\nhere you can talk with our ai and generate image use `generate image` to generate image, also here can write some code for you",
            component_map=markdown_style,
        ),
        chat_ai.chat(),
        chat_ai.action_bar(),
        chat_ai.copy_message_board(),
    )
