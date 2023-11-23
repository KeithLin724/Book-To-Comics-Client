import reflex as rx
from Book_To_Comics_Client.templates import template
from Book_To_Comics_Client import styles


@template(route="/reference", title="Reference", image="/logo.svg")
def reference() -> rx.Component:
    """
    The `reference` function reads the content of a README.md file and returns it as a markdown
    component with a specified style.
    :return: a markdown component with the content of the README.md file. The component is styled using
    the `markdown_style` component map from the `styles` module.
    """
    with open("README.md", encoding="utf-8") as readme:
        content = readme.read()
    return rx.markdown(content, component_map=styles.markdown_style)
