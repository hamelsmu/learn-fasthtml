from fasthtml.common import *
import time

app, rt = fast_app()

@rt("/")
def get():
    return Div(
        "Initial content",
        hx_get="/live-data",
        hx_trigger="every 30s queue:5 once"
    )

@rt("/live-data")
def live_data():
    return Div(f"New content at {time.time()}")

serve()