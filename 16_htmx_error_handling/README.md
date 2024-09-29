Complete the JavaScript to show a custom error message when a 404 response is received:

```javascript
document.body.addEventListener('htmx:beforeSwap', (event) => {
  if (event.detail.xhr.status === 404) {
    // Add your code here
  }
});
```