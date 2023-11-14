from Book_To_Comics_Client.templates import template
from Book_To_Comics_Client.state import State


import reflex as rx


def textbox():
    return rx.vstack(
        rx.text_area(on_change=State.set_text, value=State.text, width="100%"),
        rx.button("Send", on_click=State.send),
    )


def single_img_button(index: int) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.image(src=State.img_src, width="100%", height="100%"),
            rx.text("Picture"),
            rx.button(
                rx.text("Change Image"),
            ),
            on_click=State.image_refresh,
        ),
        padding=20,
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
            rx.foreach(State.text_list, single_img_button),
            flex_wrap="wrap",
            width="100%",
        ),
        padding_top="20px",
        
    )