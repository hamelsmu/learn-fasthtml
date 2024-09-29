from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Div(
        "Click me",
        hx_get="/data",
        hx_target="#result",
        hx_swap="innerHTML"
    ), Div(id="result")

@rt("/data")
def data():
    return "Data from the server"

@app.route("/static/js/main.js")
def js():
    return """
        htmx.logAll();
        htmx.logger = (eventName, event) => {
            if (eventName === 'htmx:afterRequest') {
                console.log('htmx:afterRequest event:', event);
            }
        };
    """

serve()