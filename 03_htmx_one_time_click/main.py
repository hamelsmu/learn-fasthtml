from fasthtml.common import *
app, rt = fast_app()

@rt("/")
def get():
    return Div(
        "Click me",
        hx_get="/data", # Make a GET request to "/data" when clicked
        hx_target="#target", # Specify where to insert the response
        hx_swap="beforeend", # Specify how to insert the response
        # hx_trigger="click once", # Trigger the request on click, but only once
    ), Div(id="target") # Empty div that will receive the response

@rt("/data")
def data(): return "Data from the server"

serve()