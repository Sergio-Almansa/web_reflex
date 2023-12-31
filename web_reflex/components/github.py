import reflex as rx
import web_reflex.constants as constants
from web_reflex.styles.styles import Size


def github() -> rx.Component:
    return rx.link(

        rx.vstack(
            rx.vstack(
                rx.span(
                    "Código Proyecto"
                ),
                rx.span(
                    "WEB en GitHub"
                ),
                align_items="start",
                class_name="nes-balloon from-right is-dark",
                margin_bottom=Size.BIG.value
            ),
            rx.box(
                rx.span(
                    constants.VERSION,
                    class_name="is-error"
                ),
                class_name="nes-badge"
            )
        ),
        rx.box(
            class_name="nes-octocat animate"
        ),
        href=constants.GITHUB_REPO_URL,
        is_external=True,
        align_items="end",
        display="flex",
        margin_top=Size.ZERO.value,
        padding_bottom=Size.BIG.value
    )