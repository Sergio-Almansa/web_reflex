import reflex as rx
import web_reflex.styles.styles as styles
from web_reflex.styles.styles import Size
from web_reflex.views.navbar import navbar
from web_reflex.views.header import header
from web_reflex.views.footer import footer
from web_reflex.views.instructions import instructions
from web_reflex.views.author import author

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                instructions(),
                author(),
                footer(),
                width="100%",
                spacing=Size.VERY_BIG.value
            )
        )
        
  
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)

app.add_page(
    index,
    title="Calendario de aDEViento 2023",
    description="Página WEB del calendario de aDEViento 2023"

)

app.compile()