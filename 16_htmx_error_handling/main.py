from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Div(
        "Click me",
        hx_get="/non-existent-page",
        hx_target="#result",
        hx_swap="innerHTML"
    ), Div(id="result")

@app.route("/static/js/main.js")
def js():
    return """
        document.body.addEventListener('htmx:beforeSwap', (event) => {
            if (event.detail.xhr.status === 404) {
                event.detail.shouldSwap = false;
                document.getElementById('result').innerHTML = 'Custom 404 error message';
            }
        });
    """

serve()