Modify the following HTML to swap in new content every 30 seconds, but stop after 5 swaps:

```html
<div hx-get="/live-data" hx-trigger="every 30s">
  <!-- Initial content here -->
</div>
```