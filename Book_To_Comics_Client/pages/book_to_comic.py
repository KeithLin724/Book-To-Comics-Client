from Book_To_Comics_Client.templates import template
from Book_To_Comics_Client.components import book_to_comic as btc


import reflex as rx


@template(route="/book_to_comic", title="Book to Comic", image="/book-to-comics.svg")
def book_to_comic() -> rx.Component:
    return rx.fragment(
        rx.heading("Book to Comic", font_size="3em"),
        rx.text("Welcome to Book to Comic!"),
        rx.text(
            'This is a Book to Comic tool. You can use it generate picture according stories. If you don\'t satisfy about the generated results, just press the " Change button " below to replace them.'
        ),
        btc.textbox(),
        btc.display_image_board(),
        btc.zoom_message_board(),
        btc.copy_message_board(),
        padding_top="20px",
    )
