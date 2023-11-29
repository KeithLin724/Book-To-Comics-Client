"""The dashboard page."""
from Book_To_Comics_Client.templates import template
from Book_To_Comics_Client.components import chat_ai_room as chat_ai
from Book_To_Comics_Client.components import functional as func
from Book_To_Comics_Client.styles import markdown_style

# from Book_To_Comics_Client.state import State


import reflex as rx

# from ..components import chat_ai_room as chat_com


@template(
    route="/chat",
    title="Chat with ai",
    image="/chat-with-ai.svg",
    on_load=func.check_server_state,
)
def chat_ai_room() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.fragment(
        func.error_board(),
        rx.heading(
            "Chat with AI",
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
