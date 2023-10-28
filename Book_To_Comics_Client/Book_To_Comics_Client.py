"""Welcome to Reflex!."""

from Book_To_Comics_Client import styles

# Import all the pages.
from Book_To_Comics_Client.pages import *

import reflex as rx

# Create the app and compile it.
app = rx.App(style=styles.base_style)
app.compile()
