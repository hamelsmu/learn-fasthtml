from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Button(
        "Perform Action",
        hx_post="/perform-action",
        hx_target="#result"
    ), Div(id="result"), Div(id="notification")

@app.route('/perform-action', methods=['POST'])
def perform_action():
    # Action logic here
    response = make_response("Action completed")
    response.headers['HX-Retarget'] = '#notification'
    return response

serve()