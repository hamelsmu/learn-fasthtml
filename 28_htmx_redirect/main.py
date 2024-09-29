from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Div(
        "Login",
        Form(
            hx_post="/login",
            hx_target="#result",
            hx_swap="innerHTML",
            children=[
                Input(type="text", name="username"),
                Input(type="password", name="password"),
                Button("Login", type="submit")
            ]
        )
    ), Div(id="result")

@app.route('/login', methods=['POST'])
def login():
    # Login logic here
    username = request.form.get("username")
    password = request.form.get("password")
    if username == "admin" and password == "password":
        response = make_response("Login successful")
        response.headers['HX-Redirect'] = '/dashboard'
        return response
    else:
        return "Login failed", 401

@rt("/dashboard")
def dashboard():
    return Titled("Dashboard", P("Welcome to the dashboard!"))

serve()