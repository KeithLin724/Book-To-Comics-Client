from Book_To_Comics_Client.templates import template
from Book_To_Comics_Client.state import State


import reflex as rx


def textbox():
    return rx.vstack(
        rx.text_area(
            on_change=State.set_text,
            value=State.text,
            width="100%",
        ),
        rx.button(
            "Send",
            on_click=State.get_test_image,
        ),
    )


def single_img_button(index: int) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.image(src=State.img_src, width="100%", height="100%"),
            rx.text(f"Picture {index+1}"),
            rx.text(f"Change Image times: {State.counter}"),
            rx.button("Change Image", on_click=State.image_refresh),
        ),
        padding="4em",
    )


def single_img_button_markdown(index: int, path) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.image(
                src=path,
                width="25%",
                height="25%",
            ),  # , width="100%", height="100%"
            # rx.markdown(path),
            rx.text(f"Picture {index+1}"),
            rx.text(f"Change Image times: {State.counter}"),
            rx.button("Change Image", on_click=State.image_refresh),
        ),
        padding="4em",
    )


@template(route="/book_to_comic", title="Book_to_Comic")
def book_to_comic() -> rx.Component:
    return rx.vstack(
        rx.heading("Book to Comic", font_size="3em"),
        rx.text("Welcome to Book to Comic!"),
        rx.text(
            'This is a Book to Comic tool. You can use it generate picture according stories. If you don\'t satisfy about the generated results, just press the " Change button " below to replace them.'
        ),
        textbox(),
        rx.flex(
            rx.foreach(
                State.img_src_arr,
                lambda item: single_img_button_markdown(item[0], item[1]),
            ),
            flex_wrap="wrap",
            width="100%",
        ),
        padding_top="20px",
    )
