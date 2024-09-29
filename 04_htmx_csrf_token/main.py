from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Div(
        "Click me",
        hx_get="/data",
        hx_target="#target",
        hx_swap="innerHTML"
    ), Div(id="target")

@rt("/data")
def data():
    return "Data from the server"

@app.route("/static/js/main.js")
def js():
    return """
        document.body.addEventListener('htmx:configRequest', (event) => {
            event.detail.headers['X-CSRF-Token'] = 'your_csrf_token_value';
        });
    """

serve()