Modify the `hx-trigger` attribute to only trigger the request when the input value is a valid email address:

```html
<input type="email" name="email" hx-get="/validate-email" hx-trigger="change">
```