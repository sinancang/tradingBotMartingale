------------------WORK-IN-PROGRESS------------------

This is my attempt at an automated trader. The program flow, as seen in the main function, is as follows:
- Connect to API
- Authenticate
    - both connect and authenticate require a file Alpaca_credentials.py to be populated with
        the public/secret key and endpoint. They are .gitignored as I wouldn't want my
        account getting stolen ;)
- Subscribe to instruments (not implemented yet)
- Listen for quotes (not implemented yet)