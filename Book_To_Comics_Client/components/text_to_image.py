import reflex as rx
from Book_To_Comics_Client.state import State


def input_box() -> rx.Component:
    return rx.vstack(
        rx.input(
            placeholder="Enter a prompt",
            on_change=State.set_text_to_image_prompt,
        ),
        rx.button(
            "Generate Image",
            on_click=State.get_text_to_image,
            is_loading=State.text_to_image_processing,
            width="100%",
            is_disabled=State.text_to_image_prompt == "",
        ),
        rx.cond(
            State.text_to_image_complete,
            rx.tooltip(
                rx.image(
                    src=State.text_to_image_result,
                    height="25em",
                    width="25em",
                    on_click=lambda: State.toggle_zoom(State.text_to_image_result),
                ),
                label="zoom",
            ),
        ),
        padding="2em",
        shadow="lg",
        border_radius="lg",
    )
