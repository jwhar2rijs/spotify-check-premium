# Spotify Premium Checker

This is a Python script that checks if a list of Spotify account credentials have a Premium subscription or not. The script uses Selenium WebDriver to automate the login process and check if the account is still Premium or not.

## Requirements

- Chrome 112 or higher must be installed.
- Python 3.x must be installed.
- Use pip to install the required packages with the following command:

```Markdown
pip install -r requirements.txt
```
## Usage

1. Edit the `config.json` file and fill in the following fields:
   - `discord_id`: The Discord user ID to tag when non-premium accounts are found (leave empty to disable).
   - `webhook_url`: The Discord webhook URL to use for sending messages.
   - `lang`: The language of the messages. Currently supports `en` (English) and `fr` (French).
2. Add your Spotify account credentials to the `logins.txt` file, with each line in the format `username:password`.
3. Run the script with the following command:
```Markdown
python main.py
```

The script will automatically launch Chrome and begin checking the accounts. Once completed, it will output a list of non-premium accounts to the console and send a message to Discord (if configured).

Note: The script will automatically detect if it is being run on Windows or Linux and select the appropriate `chromedriver`.

Important note: Before using this script, it is important to obtain authorization from the individuals whose Spotify accounts are being checked.

## Troubleshooting

- If you receive the error message "Chrome 112 or higher is required", please update your Chrome browser to the latest version.
- If you encounter any issues with the script, please make sure that the required packages are installed and that the `chromedriver` executable is in the PATH.zpdfz