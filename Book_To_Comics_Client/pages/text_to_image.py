"""The dashboard page."""
from Book_To_Comics_Client.templates import template

import reflex as rx
from Book_To_Comics_Client.components import text_to_image as tti


@template(route="/Text_to_Image", title="Text to image")
def text_to_image() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.fragment(
        rx.heading("Text to Image"),
        tti.input_box(),
        tti.zoom_message_board(),
    )
