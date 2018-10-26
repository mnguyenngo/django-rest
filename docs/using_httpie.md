# Quick Reference for HTTPie

## Making a POST request with authentication

```bash
http -a <username>:<password>  http://127.0.0.1:8000/tasks/ name="walk dog" created_by=1
```

Reference: https://httpie.org/doc#authentication
Â
