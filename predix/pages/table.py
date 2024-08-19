"""The table page."""

from ..templates import template
from ..backend.table_state import TableState
from ..views.table import main_table

import reflex as rx


@template(route="/table", title="Table", on_load=TableState.load_entries)
def table() -> rx.Component:
    """The table page.

    Returns:
        The UI for the table page.
    """
    return rx.vstack(
        rx.center(
            rx.heading("Classes Prompter", size="9"),
            width="100%"
        ),
        rx.center(
            rx.text("Prompt math classes from year 2018 to 2024.", size="3"),
            width="100%"
        ),
        main_table(),
        spacing="8",
        width="100%",
    )


