import reflex as rx
import web_reflex.styles.styles as styles
import web_reflex.constants as constants
from web_reflex.styles.styles import Size, Color
from web_reflex.styles.styles import TextColor

def header() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Calendario de aDEViento 2023",
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
                    rx.text("24 días, 24 regalos."),
                    rx.text("Del 1 al 24 de diciembre."),
                    class_name="nes-balloon from-left is-dark"
                ),
                rx.span(
                    "Por tercer año, ¡aquí está el calendario de adviento sorpresa de nuestra ",
                    rx.span(
                        "comunidad de developers",
                        color=TextColor.ACCENT.value,
                        font_size=Size.DEFAULT.value
                    ),
                    "!",
                ),
                 rx.span(
                    "Una actividad en la que cada día sortearé un regalo relacionado con programación y desarrollo",
                ),               

                rx.span(
                    "Su finalidad es ayudar a compartir conociemiento y fomentar el aprendizaje de la comunidad",
                ),
                rx.link(
                    "aDEViento 2023",
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