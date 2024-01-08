import reflex as rx
import web_reflex.constants as constants
import web_reflex.styles.styles as styles
from web_reflex.styles.styles import TextColor
from web_reflex.components.button import button


def instructions() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "¿Cómo funciona el evento?",
                class_name="title",
                color=TextColor.ACCENT.value
            ),
            rx.span(
                "• Del Enero a Diciembre descubriré cada mes, un nuevo proyecto en el calendario."),
            rx.span("• Podrás ver el código del proyecto en los repos de GitHub."),
            rx.span("• Sólo tendrás que hacer STAR al repo si te resulta interesante."),
            button(
                "Twitter",
                constants.TWITTER_URL
            ),
            rx.span(
                "• Se aceptan sugerencias para los proyectos..."
            ),
            rx.span(
                "• ¡Los llevaré a cabo en Python!"
            ),
            class_name="nes-container is-dark with-title",
            align_items="start",
            width="100%"
        ),
        style=styles.max_width_style
    )