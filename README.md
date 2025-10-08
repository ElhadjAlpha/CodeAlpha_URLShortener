# URL Shortener - CodeAlpha

## Description
This is a Django-based URL Shortener project. It allows users to shorten long URLs and manage them through a simple web interface or API. Features include:

- Bootstrap form for URL input
- Copyable short link
- List of shortened links for each user
- Redirection with click counter
- URL validation (http/https) and blocking of internal domains (localhost, 127.0.0.1)
- REST API endpoints for programmatic access

## Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:ElhadjAlpha/CodeAlpha_URLShortener.git
   cd CodeAlpha_URLShortener
## Create a virtual environment
- python -m venv venv
- venv\Scripts\activate     # Windows
- source venv/bin/activate  # macOS/Linux
# Install dependencies
- pip install -r requirements.txt
# Copy the example settings file and add your secret key
- copy codealpha_shortener\settings_example.py codealpha_shortener\settings.py   # Windows
- cp codealpha_shortener/settings_example.py codealpha_shortener/settings.py      # macOS/Linux
# Apply migrations and run the server
- python manage.py migrate
- python manage.py runserver
