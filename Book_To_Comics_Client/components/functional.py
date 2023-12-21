import reflex as rx

from Book_To_Comics_Client.state import State


def check_server_state():
    return State.check_server_state


def get_server_service():
    return State.get_server_service


def error_board(service: str = "connect") -> rx.Component:
    return (
        rx.cond(
            condition=State.connect_server == False,
            c1=rx.alert(
                rx.alert_icon(),
                rx.alert_title("Connect Server error"),
                status="error",
            ),
        )
        if service == "connect"
        else rx.cond(
            condition=State.service_provide[service] == {},
            c1=rx.alert(
                rx.alert_icon(),
                rx.alert_title("Server is not provide this service"),
                status="error",
            ),
        )
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
