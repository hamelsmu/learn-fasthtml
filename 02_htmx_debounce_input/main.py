from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Input(
        type="text",
        name="search",
        hx_get="/search",
        hx_trigger="keyup delay:500ms changed"
    )

@rt("/search")
def search(req):
    query = req.query_params.get("search", "")
    return f"Searching for: {query}"

serve()
```
</explain>

In this example, we:

1. Create a route at the root `/` that returns an `<input>` element with the `type="text"`, `name="search"`, `hx-get="/search"`, and `hx-trigger="keyup delay:500ms changed"` attributes.
2. Create a route at `/search` that retrieves the `search` query parameter from the request and returns a string with the search query.

When the user types in the input field, the `keyup` event is triggered, but the AJAX request to the `/search` endpoint is debounced by 500ms and only sent if the input value has changed.