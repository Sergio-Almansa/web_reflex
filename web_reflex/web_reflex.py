import reflex as rx
import web_reflex.styles.styles as styles
from web_reflex.views.navbar import navbar

def index() -> rx.Component:
    return rx.box(
        navbar()
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