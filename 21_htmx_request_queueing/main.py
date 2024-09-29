from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Button(
        "Increment",
        hx_post="/increment",
        hx_trigger="click queue:3"
    )

@app.route("/increment", methods=["POST"])
def increment():
    # Increment some value and return the result
    return "Incremented"

serve()