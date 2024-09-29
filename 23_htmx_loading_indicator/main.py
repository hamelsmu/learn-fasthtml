from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Button(
        "Load Slow Data",
        hx_get="/slow-data",
        hx_indicator=".spinner"
    ), Div("Loading...", cls="spinner", style="display:none;")

@rt("/slow-data")
def slow_data():
    import time
    time.sleep(2)  # Simulating a slow request
    return "Slow data loaded"

serve()