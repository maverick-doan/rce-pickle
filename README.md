# rce-pickle - Insecure Python Pickle Deserialisation Testing

**For authorised security testing only**

This repository contains Proof-of-Concept pickle payloads for testing insecure deserialisation vulnerabilities in glorious Python applications that use `pickle.load()` without proper validation.

I created this to assist in RCE validation during a security assessment at work. While there are many ways to verify RCE, this is built mainly for having a consistent and purpose-built pickle bomb that allows for simplicity, easy retrieval (via GitHub) and standardisation.

## Payloads

The generated pickles use the `__reduce__` method to execute system commands upon deserialisation.

- **linux-pickle.pkl**: Writes to `/tmp/evil.txt`.
- **windows-pickle.pkl**: Writes to `C:\Users\Public\evil.txt`.

## How to Use

### Local Generation
You can generate the payloads manually using the provided script:
```bash
python evil-pickle.py linux pkl/linux-pickle.pkl
python evil-pickle.py windows pkl/windows-pickle.pkl
```

### Automated Builds
This repo uses GitHub Actions to automate the generation of these pickles. The workflow runs on every push to `main` and stores the resulting files in the `pkl/` directory. Fetch these via `raw.githubusercontent.com` if needed.

### Vulnerability Verification
To test if an application is vulnerable, attempt to load the generated `.pkl` file:
```python
import pickle

with open('pkl/linux-pickle.pkl', 'rb') as f:
    # ...snip... -> No validation, deserilisation isolation, etc.
    pickle.load(f) # If vulnerable, this executes the payload
```