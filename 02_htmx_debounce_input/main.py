from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Div(
        Input(
            type="text",
            name="search",
            hx_get="/search",
            hx_trigger="keyup delay:1s changed",
            hx_target="#search-results",
        ),
        Div(id="search-results")
    )

@rt("/search")
def search(req):
    query = req.query_params.get("search", "")
    return P(f"Searching for: {query}")

serve()