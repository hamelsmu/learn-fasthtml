from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Div(
        "Click me",
        id="click-me",
        hx_get="/data",
        hx_target="#target",
        hx_swap="innerHTML",
        hx_trigger="click once"
    ), Div(id="target")

@rt("/data")
def data():
    return "Data from the server"

serve()