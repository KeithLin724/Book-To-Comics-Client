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
            not State.check_service(service),
            rx.alert(
                rx.alert_icon(),
                rx.alert_title("Server is not provide this service"),
                status="error",
            ),
        )
    )
