Write the server-side code (in Python using Flask) to retarget the swap to an element with id "notification" instead of the requesting element:

```python
@app.route('/perform-action', methods=['POST'])
def perform_action():
    # Action logic here
    response = make_response("Action completed")
    # Add your code here to retarget the swap
    return response
```