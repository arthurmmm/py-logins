# py-logins
This project contains serveral python packages which could simulate a website login, but need input captcha manually.

Requirements:
-  requests==2.13.0
-  rsa==3.4.2

Each package would contain below functions

```python

def prepare(captcha_file=None):
    ''' Get captcha and store in captcha_file
    captcha_file: path to store captcha image
    
    return: session with cookies
    '''

def login(username, password, captcha, session=None):
    ''' Perform login with given arguments
    username: Your username
    password: Your password
    captcha: Your captcha code. Should run prepare first to get captcha
    session: session with cookies
    
    return: cookies dict or None.
    '''

```

# Available website (on progress)

## bilibili

Test Case:

```bash
python -m unittest bilibili_login.TestCases.getlogin
# Get a login cookie json file on /var/tmp/bilibili.login

python -m unittest bilibili_login.TestCases.uselogin
# Use login cookie json file to verify
```
