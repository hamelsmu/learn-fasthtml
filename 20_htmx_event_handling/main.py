from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Div(
        id="user-info",
        hx_get="/user-info",
        hx_trigger="userUpdated from:body"
    )

@rt("/user-info")
def user_info():
    return Div(
        H2("User Information"),
        P("Name: John Doe"),
        P("Email: john@example.com")
    )

@app.route("/update-user", methods=["POST"])
def update_user():
    # Update user logic here
    response = make_response("User updated")
    response.headers['HX-Trigger'] = 'userUpdated'
    return response

serve()