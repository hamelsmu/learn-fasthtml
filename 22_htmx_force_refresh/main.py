from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Form(
        hx_post="/submit-form",
        hx_target="#result",
        hx_swap="innerHTML",
        children=[
            Input(type="text", name="data"),
            Button("Submit", type="submit")
        ]
    ), Div(id="result")

@app.route('/submit-form', methods=['POST'])
def submit_form():
    # Form processing logic here
    response = make_response("Form submitted successfully")
    response.headers['HX-Refresh'] = 'true'
    return response

serve()