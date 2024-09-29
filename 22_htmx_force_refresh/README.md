Write the server-side code (in Python using Flask) to force a refresh of the entire page after a successful form submission:

```python
@app.route('/submit-form', methods=['POST'])
def submit_form():
    # Form processing logic here
    response = make_response("Form submitted successfully")
    # Add your code here to force a page refresh
    return response
```