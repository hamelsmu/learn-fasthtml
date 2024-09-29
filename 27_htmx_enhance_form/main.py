from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Form(
        hx_post="/submit",
        hx_target="#result",
        hx_swap="innerHTML",
        children=[
            Input(type="text", name="data"),
            Button("Submit", type="submit")
        ]
    ), Div(id="result")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.form.get("data")
    return f"Submitted data: {data}"

serve()