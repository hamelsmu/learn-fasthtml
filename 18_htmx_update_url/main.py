from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Button(
        "Go to New Page",
        hx_get="/new-page-content",
        hx_target="body",
        hx_push_url="/new-page"
    )

@rt("/new-page-content")
def new_page_content():
    return Div("New Page Content")

serve()