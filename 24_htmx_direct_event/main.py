from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Button(
        Span("Perform Action"),
        hx_post="/action",
        hx_trigger="click target:self"
    )

@app.route("/action", methods=["POST"])
def action():
    # Perform the action
    return "Action performed"

serve()