import reflex as rx
from Book_To_Comics_Client.state import State


def textbox() -> rx.Component:
    return rx.vstack(
        rx.text_area(
            on_change=State.set_text,
            value=State.text,
            width="100%",
        ),
        rx.button(
            "Send",
            on_click=State.get_test,
            border_radius="1em",
            box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
            background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
            box_sizing="border-box",
            color="white",
            opacity="0.6",
            _hover={
                "opacity": 1,
            },
            is_disabled=State.text == "",
            is_loading=State.is_cutting_prompt,
            loading_text="thinking...",
            spinner_placement="start",
        ),
    )


def single_img_frame(index: int, image, image_url, image_prompt: str) -> rx.Component:
    """
    single image frame

    The `single_img_button` function returns a component that displays an image, along with buttons to
    change the image and copy the image URL.

    :param index: An integer representing the index of the image
    :type index: int
    :param image: The `image` parameter is a string that represents the image source or URL. It is used
    to display the image in the component
    :param image_url: The `image_url` parameter is the URL of the image that will be displayed in the
    component
    :return: The function `single_img_button` returns a `rx.Component` object.
    """
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
                        # zoom image
                        on_click=lambda: State.toggle_zoom(image),
                    ),
                    label=f"{image_prompt}",
                    has_arrow=True,
                ),
            ),
            rx.text(f"Picture {index+1}"),
            rx.text(f"Prompt : {image_prompt}"),
            rx.text(f"Change Image times: {State.counter}"),
            rx.button(
                "Change Image",
                on_click=State.image_refresh,
                is_disabled=image == "",
            ),
            rx.button(
                "Copy Image",
                on_click=lambda: State.copy_show(image_url),
                is_disabled=image == "",
            ),
        ),
        padding="4em",
    )


def display_image_board() -> rx.Component:
    """
    display image boarder


    The function `display_image_board` returns a component that displays a board of images using the
    `rx` library.
    :return: a reactive component that displays an image board.
    """
    return rx.flex(
        rx.foreach(
            State.img_src_arr,
            lambda item: single_img_frame(
                item[0],
                item[1],
                item[2],
                item[3],
            ),
        ),
        flex_wrap="wrap",
        width="100%",
    )


def zoom_message_board() -> rx.Component:
    # drawer component : display a message in the top , "Copied!"
    return rx.alert_dialog(
        rx.alert_dialog_overlay(
            rx.alert_dialog_content(
                rx.image(
                    src=State.zoom_image,
                    on_click=lambda: State.toggle_zoom(""),
                ),
            ),
        ),
        is_open=State.is_zoomed,
        on_overlay_click=lambda: State.toggle_zoom(""),
    )


def copy_message_board() -> rx.Component:
    # zoom image component

    return rx.drawer(
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
    )
