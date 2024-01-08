import reflex as rx
import web_reflex.constants as constants
from web_reflex.styles.styles import Size, Color
from web_reflex.components.link_icon import link_icon


def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
                rx.image(
                    src="Foto_Cuentas.jpg",
                    alt="Avatar sasdev",
                    border="4px",
                    border_color=Color.SECONDARY.value,
                    class_name="nes-avatar is-large is-rounded",
                    width=Size.VERY_BIG.value,
                    height=Size.VERY_BIG.value
                ),
                rx.text("aDEViento 2023"),
                rx.spacer(),
                link_icon(
                    "linkedin",
                    constants.LINKEDIN_URL      
                ),
                link_icon(
                    "github",
                    constants.GITHUB_URL     
                ),
                link_icon(
                    "instagram",
                    constants.INSTAGRAM_URL      
                ),
                link_icon(
                    "twitter",
                    constants.TWITTER_URL
                ),
                width="100%"
            ),
            bg=Color.PRIMARY.value,
            position="sticky",
            border_bottom=f"0.25em solid {Color.SECONDARY.value}",
            padding_x=Size.BIG.value,
            padding_y=Size.BIG.value,
            z_index="999",
            top="0",
            width="100%"
    )

