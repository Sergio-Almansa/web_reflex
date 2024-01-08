import reflex as rx
import web_reflex.styles.styles as styles
from web_reflex.styles.styles import Size
from web_reflex.views.navbar import navbar
from web_reflex.views.header import header
from web_reflex.views.footer import footer
from web_reflex.components.github import github
from web_reflex.views.calendar import calendar
from web_reflex.views.instructions import instructions
from web_reflex.views.author import author

def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        rx.script(src="/js/snow.js"),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                instructions(),
                author(),
                calendar(),
                footer(),
                github(),
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
    title="@sasdev 2024",
    description="Página WEB de Sergio Almansa"

)

app.compile()