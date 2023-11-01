"""The dashboard page."""
from Book_To_Comics_Client.templates import template

import reflex as rx
from ..state import State
from functools import partial


@template(route="/test_page", title="Test_page")
def test_page() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.heading(
            "Test",
            font_size="3em",
        ),
        rx.text("Welcome to Reflex!"),
        rx.button(
            "test request",
            on_click=State.get_posts_host,
        ),
        rx.text(f"get result {State.posts} , {State.res}"),
    )
