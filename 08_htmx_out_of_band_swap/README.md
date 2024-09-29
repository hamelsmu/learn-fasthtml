Given the following HTML, add an out-of-band swap to update an element with id "notification" when the form is submitted:

```html
<form hx-post="/submit">
  <input type="text" name="data">
  <button type="submit">Submit</button>
</form>
```