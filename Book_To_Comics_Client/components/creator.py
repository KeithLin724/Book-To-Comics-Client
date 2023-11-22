import reflex as rx


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
        ),
    )
