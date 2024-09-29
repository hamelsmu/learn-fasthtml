from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Div(
        "Lazy Loading Example",
        Div(
            hx_get="/lazy-content",
            hx_trigger="intersect 200px",
            hx_target="this"
        )
    )

@rt("/lazy-content")
def lazy_content():
    return "Lazy loaded content"

serve()