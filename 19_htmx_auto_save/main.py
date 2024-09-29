from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Form(
        id="myForm",
        hx_post="/auto-save",
        hx_trigger="every 5s changed",
        children=[
            Input(type="text", name="data")
        ]
    )

@app.route("/auto-save", methods=["POST"])
def auto_save():
    data = request.form.get("data")
    # Save the data to the server
    return "Data saved"

serve()