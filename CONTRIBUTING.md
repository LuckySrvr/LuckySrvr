# Contributing to Lucky

Thank you for linking your infrastructure to our network! To keep the cluster safe and organized, please follow these file registration rules:

## PR Requirements
- File name must match the target domain case exactly (e.g., `nodes/example.com.json`).
- Do not modify files in the root folder (`lucky_core.py`, `.gitignore`, etc.).
- Ensure your JSON values contain valid formatting and protocol declarations.

## Validation Checklist
Before submitting your Pull Request, double-check that your JSON configuration parses correctly:
```bash
python3 -m json.tool nodes/yourdomain.json
```
