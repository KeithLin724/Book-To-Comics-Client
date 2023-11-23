import reflex as rx
from Book_To_Comics_Client.func.creator_item import User
from Book_To_Comics_Client.state import State


def creator() -> rx.Component:
    return rx.avatar_group(
        rx.link(
            rx.tooltip(
                rx.avatar(
                    src="https://avatars.githubusercontent.com/u/38067890?v=4",
                    name="Keith Lin",
                ),
                label="Keith Lin",
            ),
            href="https://github.com/KeithLin724",
            is_external=True,
        ),
        rx.link(
            rx.tooltip(
                rx.avatar(
                    src="https://avatars.githubusercontent.com/u/148564112?v=4",
                    name="Vincent Lien",
                ),
                label="Vincent Lien",
            ),
            href="https://github.com/Vincent-Lien",
            is_external=True,
        ),
    )


def make_detail_card(creator_data: dict[str, str]) -> rx.Component:
    return rx.card(
        rx.text(creator_data["bio"]),
        header=rx.hstack(
            rx.heading(creator_data["login"], size="lg"),
            rx.link(
                rx.tooltip(
                    rx.avatar(
                        src=creator_data["avatar_url"],
                        name=creator_data["name"],
                    ),
                    label=creator_data["login"],
                ),
                href=creator_data["html_url"],
                is_external=True,
            ),
        ),
        footer=rx.heading("public repos", size="sm"),
    )


def creator_cards() -> rx.Component:
    return rx.fragment(
        rx.heading("About us"),
        rx.flex(
            rx.foreach(
                State.creator_info,
                make_detail_card,
            ),
            flex_wrap="wrap",
            width="100%",
        ),
    )
