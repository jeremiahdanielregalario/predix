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
        rx.heading("Classes Prompter", size="5"),
        rx.text("Prompt math classes from year 2018 to 2023.", size="3"),
        main_table(),
        spacing="8",
        width="100%",
    )

