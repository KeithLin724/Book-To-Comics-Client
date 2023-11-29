"""The dashboard page."""
import reflex as rx

from Book_To_Comics_Client.templates import template
from Book_To_Comics_Client.components import text_to_image as tti
from Book_To_Comics_Client.components import functional as func


@template(
    route="/Text_to_Image",
    title="Text to image",
    on_load=func.get_server_service,
)
def text_to_image() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.fragment(
        func.error_board("text_to_image"),
        rx.heading("Text to Image"),
        tti.input_box(),
        func.zoom_message_board(),
    )
