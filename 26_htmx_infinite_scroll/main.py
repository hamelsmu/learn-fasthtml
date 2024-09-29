from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Div(
        id="infinite-scroll",
        hx_get="/more-content",
        hx_trigger="revealed 100px",
        hx_target="this",
        hx_swap="beforeend"
    )

@rt("/more-content")
def more_content():
    return Div("More content loaded")

serve()