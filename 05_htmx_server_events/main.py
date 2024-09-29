from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Div(
        "Update User",
        hx_post="/update-user",
        hx_target="#user-info",
        hx_swap="innerHTML",
        hx_trigger="click"
    ), Div(id="user-info")

@app.route('/update-user', methods=['POST'])
def update_user():
    # Update user logic here
    response = make_response("User updated")
    response.headers['HX-Trigger'] = 'userUpdated'
    return response

serve()