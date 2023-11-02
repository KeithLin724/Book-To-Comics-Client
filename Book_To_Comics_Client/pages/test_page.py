"""The dashboard page."""
from Book_To_Comics_Client.templates import template

import reflex as rx
from ..state import State


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
        # rx.text("!" * 140),
        rx.text("Welcome to Reflex!"),
        rx.button(
            "test request",
            on_click=State.test_get_request,
        ),
        rx.text(f"get result {State.res} , {State.res}"),
    )
