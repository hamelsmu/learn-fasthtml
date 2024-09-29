Complete the server-side code (in Python using Flask) to respond with a 204 No Content status when a delete operation is successful:

```python
@app.route('/delete-item/<int:id>', methods=['DELETE'])
def delete_item(id):
    # Delete item logic here
    # Add your code here to return a 204 No Content response
```