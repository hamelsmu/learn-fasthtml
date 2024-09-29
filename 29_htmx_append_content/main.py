from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Ul(
        id="item-list",
        # Existing items here
    ), Button(
        "Load More",
        hx_get="/more-items",
        hx_target="closest ul",
        hx_swap="beforeend",
        hx_trigger="click",
        onclick="this.remove()"
    )

@rt("/more-items")
def more_items():
    return [Li(f"Item {i}") for i in range(1, 4)]

serve()