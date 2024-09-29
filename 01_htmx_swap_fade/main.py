from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Div(
        "Load Data",
        hx_get="/data",
        hx_swap="outerHTML swap:300ms",
        cls="fade-out"
    )

@rt("/data")
def data():
    return "New Data"

@app.route("/static/css/main.css")
def css():
    return """
        .fade-out {
            opacity: 1;
            transition: opacity 300ms ease-out;
        }
        .fade-out.htmx-swapping {
            opacity: 0;
        }
    """

serve()