"""Welcome to Reflex!."""

from Book_To_Comics_Client import styles

# Import all the pages.
from Book_To_Comics_Client.pages import *
from Book_To_Comics_Client.backend import test_router, ai_router
import reflex as rx

# Create the app and compile it.
app = rx.App(style=styles.base_style)
app.api.include_router(router=test_router)
app.api.include_router(router=ai_router)
app.compile()
