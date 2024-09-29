from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Div(
        "Long Running Request",
        id="long-running-request",
        hx_get="/long-running",
        hx_target="#result",
        hx_swap="innerHTML"
    ), Div(id="result"), Button(
        "Abort Request",
        onclick="document.getElementById('long-running-request')\
            .dispatchEvent(new Event('htmx:abort'))"
    )

@rt("/long-running")
async def long_running():
    import time
    await asyncio.sleep(5)  # Simulating a long-running request
    return "Result from long-running request"

serve()