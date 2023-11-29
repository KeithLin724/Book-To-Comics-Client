import reflex as rx
from Book_To_Comics_Client.state import State
from Book_To_Comics_Client.styles import (
    input_style,
    button_style,
    question_style,
    answer_style,
    markdown_style,
    ai_is_thinking,
)


def qa_markdown(index: int, question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.markdown(
                    question,
                    component_map=markdown_style,
                ),
                style=question_style,
            ),
            text_align="right",
        ),
        rx.box(
            rx.cond(
                condition=State.chat_history[index][-1] == "",
                c1=rx.stack(
                    rx.skeleton_text(
                        no_of_lines=5,
                        start_color="pink.500",
                        end_color="orange.500",
                        speed=1.5,
                    ),
                    style=ai_is_thinking,
                    # style=answer_style,
                ),
                c2=rx.tooltip(
                    rx.box(
                        # add animation
                        rx.markdown(
                            answer,
                            component_map=markdown_style,
                        ),
                        style=answer_style,
                    ),
                    label="copy",
                    has_arrow=True,
                ),
            ),
            text_align="left",
            on_click=lambda: State.copy_show(answer),
        ),
        margin_y="1em",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa_markdown(messages[0], messages[1], messages[2]),
        )
    )


def action_bar() -> rx.Component:
    return rx.center(
        rx.hstack(
            rx.fragment(
                rx.input(
                    value=State.question,
                    placeholder="Ask a question",
                    on_change=State.set_question,
                    style=input_style,
                    on_key_up=State.answer_ai_enter,
                ),
            ),
            rx.button(
                "Ask",
                on_click=State.answer_ai,
                style=button_style,
                is_disabled=State.question == "",
                is_loading=State.ai_is_thinking,
                loading_text="thinking...",
                spinner_placement="start",
            ),
        ),
    )


# def copy_message_board() -> rx.Component:
#     # zoom image component

#     return rx.drawer(
#         rx.drawer_content(
#             # rx.text("Copied!"),
#             # rx.drawer_header("Copied!"),
#             rx.center(
#                 rx.drawer_header(
#                     "Copied!",
#                     color="white",
#                 ),
#             ),
#             bg="rgba(0, 0, 0, 0.3)",
#         ),
#         is_open=State.show_copy_in_top,
#         # placement prop to position drawer at top
#         placement="top",
#     )
