import reflex as rx
import web_reflex.constants as constants
import web_reflex.styles.styles as styles
from web_reflex.styles.styles import Size, TextColor

def footer() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text(
                "Calendario de Proyectos/Desafíos 2024",
                font_size=Size.MEDIUM.value,
                margin_bottom=Size.ZERO.value        
            ),
            rx.link(
                "Creado con amor ",
                rx.box(class_name="nes-icon is-small heart"),
                " (y gracias a ti) por @sasdev by Sergio Almansa",
                href=constants.SASDEV_URL,
                is_external=True,
                margin_top=Size.SMALL.value,
                font_size=Size.MEDIUM.value,
                color=TextColor.TERCIARY.value
            ),
            align_items="start",
            spacing=Size.MEDIUM.value
        ),
        rx.spacer(),
        rx.image(
            src="Foto_Cuentas.jpg",
            alt="Avatar SASDev",
            class_name="nes-avatar is-large is-rounded",
            
        ),
        padding_bottom=Size.BIG.value,
        style=styles.max_width_style,
        align_items="center"

    )