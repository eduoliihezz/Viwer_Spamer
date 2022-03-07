# GitHub Profile Views Stats Spamer

This is a small python code that will spam your GitHub Views Stats link. This will make that your profile views increase as all as you want !!

**ADVISE:** This is not a DoS Attack Script, any bad/illegal use of this script, I'm not responsible.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install requests
```
```bash
pip install time
```

## Usage
In line 9 and 10 add your discord webhook link, and the one that you want to spam.
```python
# The URL you want to spam
url = ""
# The URL of Discord Webhook
webhook_url = ""
```
Also in line 15 change the numbers (Times you want to spam)
```python
def spam():
    for i in range(4000): # Change 4000 to the time you want to spam
```
And if you want (I don't recommend) you can change the time between link request
```python
time.sleep(2) # Change 2 to time bettween request (In seconds)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[APACHE 2.0](https://choosealicense.com/licenses/apache-2.0/)