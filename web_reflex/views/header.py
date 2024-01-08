import reflex as rx
import web_reflex.styles.styles as styles
import web_reflex.constants as constants
from web_reflex.styles.styles import Size, Color
from web_reflex.styles.styles import TextColor

def header() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Página de Sergio Almansa",
            size="lg",
            padding_bottom= Size.BIG.value
        ),
        rx.flex(
            rx.avatar(
                src="Foto_Cuentas.jpg",
                alt="Avatar sasdev",
                border="4px",
                border_color=Color.SECONDARY.value,
                class_name="nes-avatar is-large is-rounded",
                width=Size.VERY_BIG.value,
                height=Size.VERY_BIG.value,
                margin_right= Size.BIG.value

            ),
            rx.vstack(
                rx.box(
                    rx.text("12 meses, 12 proyectos."),
                    rx.text("Del 01/01 al 31/12 de 2024."),
                    class_name="nes-balloon from-left is-dark"
                ),
                rx.span(
                    "Por primera vez, ¡aquí está el calendario de proyectos de ",
                    rx.span(
                        "@sasdev",
                        color=TextColor.ACCENT.value,
                        font_size=Size.DEFAULT.value
                    ),
                    "!",
                ),
                 rx.span(
                    "Una actividad en la que cada mes realizaré un proyecto de Software hasta completar el año.",
                ),

                rx.span(
                    "Esta WEB está desarrollada completamente en Python.",
                ),

                rx.span(
                    "He usado para ello el nuevo FRAMEWORK web (REFLEX) y la libreria NES.css.",
                ),            

                rx.span(
                    "Su finalidad es poder llevar a cabo esos proyectos que hasta ahora habían quedado aparcados.",
                ),
                rx.link(
                    "@sasdev 2024",
                    href=constants.ADEVIENTO_HASHTAG_URL,
                    is_external=True,
                    #color=TextColor.TERCIARY.value,
                    padding_top=Size.BIG.value,
                    font_size=Size.MEDIUM.value
                ),
                align_items="start",
                   
            ),
            flex_direction=["column","column","column","row","row"]

        ),
        padding=Size.VERY_BIG.value,
        style=styles.max_width_style
        
    )