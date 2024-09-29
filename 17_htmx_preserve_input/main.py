from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Form(
        hx_post="/submit",
        hx_target="#result",
        children=[
            Input(type="text", name="important-data", hx_preserve=True),
            Button("Submit", type="submit")
        ]
    ), Div(id="result")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.form.get("important-data")
    return Div(f"Submitted data: {data}")

serve()