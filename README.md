# py-logins
This project contains serveral python packages which could simulate a website login, but need input captcha manually.

Requirements:
-  requests
-  rsa
-  base64
-  json

Each package would contain below functions
```python

def testLogin(cookies=None, cookies_file=None):
    ''' Access a page that require a login status to validate if we login successfully.
    cookies: cookies dict
    cookies_file: a file that contains cookie dict, with JSON format.
    
    return: test result (true/false)
    '''

def login(username, password, captcha_file=None, cookies_file=None):
    ''' Perform login with given arguments
    username: Your username
    password: Your password
    captcha_file: Path to store captcha image
    cookies_file: Path to persist cookies dict. Optional.
    
    return: cookies dict or None.
    '''

```

# Available website (on progress)

-  bilibili
