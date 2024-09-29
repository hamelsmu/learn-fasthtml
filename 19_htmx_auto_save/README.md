Complete the HTML to submit a form with id "myForm" every 5 seconds, but only if the form's data has changed:

```html
<form id="myForm" hx-post="/auto-save" [...]>
  <input type="text" name="data">
</form>
```