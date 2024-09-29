from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Div(
        Div(
            H2("User Comment"),
            P("This is a user comment that might contain malicious HTMX attributes."),
            hx_disable=True
        )
    )

serve()