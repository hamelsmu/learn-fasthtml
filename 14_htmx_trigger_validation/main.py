from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Input(
        type="email",
        name="email",
        hx_get="/validate-email",
        hx_trigger="change[this.value.includes('@')]"
    )

@rt("/validate-email")
def validate_email(req):
    email = req.query_params.get("email")
    if "@" in email:
        return "Valid email"
    else:
        return "Invalid email", 400

serve()