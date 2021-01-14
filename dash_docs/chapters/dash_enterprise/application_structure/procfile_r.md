## Procfile

Declares what commands are run by app's container(s). This is commonly:

```
web: R -f /app/app.R
```

which launches the Dash app from the /app subdirectory (where it was be copied during deployment).

---
