from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Form(
        hx_post="/submit",
        children=[
            Input(type="text", name="data"),
            Button("Submit", type="submit")
        ]
    ), Div(id="notification")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.form.get("data")
    return Div(f"Notification: {data}"), Div(id="notification", hx_swap_oob="true")

serve()