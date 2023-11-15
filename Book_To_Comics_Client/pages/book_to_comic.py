from Book_To_Comics_Client.templates import template
from Book_To_Comics_Client.state import State


import reflex as rx

from functools import partial


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
            border_radius="1em",
            box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
            background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
            box_sizing="border-box",
            color="white",
            opacity="0.6",
            _hover={
                "opacity": 1,
            },
        ),
    )


def single_img_button(index: int, image, image_url) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.cond(
                condition=(image == ""),
                # CircularProgress when the image is loading
                c1=rx.circular_progress(is_indeterminate=True),
                # Display image when loading is complete
                c2=rx.tooltip(
                    rx.image(
                        src=image,
                        width="200px",
                        html_height="auto",
                        # Keep aspect ratio
                        fit="scale-down",
                        on_click=State.toggle_zoom,
                    ),
                    label="cat is running",
                    has_arrow=True,
                ),
            ),
            rx.text(f"Picture {index+1}"),
            rx.text(f"Change Image times: {State.counter}"),
            rx.button("Change Image", on_click=State.image_refresh),
            rx.button(
                "Copy Image",
                on_click=partial(State.copy_show, image_url),
            ),
            # drawer component
            rx.drawer(
                rx.drawer_content(
                    # rx.text("Copied!"),
                    # rx.drawer_header("Copied!"),
                    rx.center(
                        rx.drawer_header(
                            "Copied!",
                            color="white",
                        ),
                    ),
                    bg="rgba(0, 0, 0, 0.3)",
                ),
                is_open=State.show_copy_in_top,
                # placement prop to position drawer at top
                placement="top",
            ),
            rx.alert_dialog(
                rx.alert_dialog_overlay(
                    rx.alert_dialog_content(
                        rx.image(
                            src=image,
                            on_click=State.toggle_zoom,
                        ),
                    ),
                ),
                is_open=State.is_zoomed,
                on_overlay_click=State.toggle_zoom,
            ),
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
                lambda item: single_img_button(
                    item[0],
                    item[1],
                    item[2],
                ),
            ),
            flex_wrap="wrap",
            width="100%",
        ),
        padding_top="20px",
    )
