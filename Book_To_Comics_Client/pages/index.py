"""The home page of the app."""

from Book_To_Comics_Client import styles
from Book_To_Comics_Client.templates import template

import reflex as rx


@template(route="/", title="Home", image="/github.svg")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    with open("README.md", encoding="utf-8") as readme:
        content = readme.read()
    return rx.fragment(
        rx.avatar_group(
            rx.avatar(
                src="https://avatars.githubusercontent.com/u/38067890?v=4",
                name="Keith Lin",
            ),  # src="https://example.com/avatar1.jpg"
            rx.avatar(
                src="https://avatars.githubusercontent.com/u/148564112?v=4",
                name="Vincent Lien",
            ),  # src="https://example.com/avatar2.jpg"
        ),
        rx.markdown(content, component_map=styles.markdown_style),
    )
