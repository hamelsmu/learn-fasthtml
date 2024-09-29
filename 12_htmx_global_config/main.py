from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Titled(
        "HTMX Configuration Example",
        Div(
            "Click me",
            hx_get="/data",
            hx_target="#result"
        ),
        Div(id="result")
    )

@rt("/data")
def data():
    return "Data from the server"

@app.route("/static/index.html")
def index():
    return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>HTMX Configuration Example</title>
            <meta name="htmx-config" content='{"defaultSwapStyle":"outerHTML","timeout":5000}'>
            <script src="https://unpkg.com/htmx.org@next/dist/htmx.min.js"></script>
        </head>
        <body>
            {{% include_template %}}
        </body>
        </html>
    """

serve()