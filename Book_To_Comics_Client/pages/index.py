"""The home page of the app."""

from Book_To_Comics_Client import styles
from Book_To_Comics_Client.templates import template
from Book_To_Comics_Client.components import creator as c
from Book_To_Comics_Client.state import State

import reflex as rx


@template(
    route="/", title="Home", image="/github.svg"
)  # , on_load=State.load_creator_info
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    with open("docs/README.md", encoding="utf-8") as readme:
        content = readme.read()

    return rx.fragment(
        rx.markdown(content, component_map=styles.markdown_style),
        rx.divider(),
        # c.creator_cards(),
        # rx.hstack(
        #     # rx.heading("Team"),
        #     # c.creator(),
        #     c.creator_card(),
        #     c.creator_card(),
        # ),
    )
