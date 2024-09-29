Given the following HTML, add the appropriate attribute to preserve the value of the input field during HTMX swaps:

```html
<form hx-post="/submit" hx-target="#result">
  <input type="text" name="important-data">
  <button type="submit">Submit</button>
</form>
<div id="result"></div>
```