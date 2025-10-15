# Simple Weather App

A simple Django-based web application that fetches and displays current weather information for a given city using the wttr.in API.

## Features

- 🌤️ Real-time weather data retrieval
- 📍 City-based weather lookup
- 🌡️ Temperature, humidity, wind speed, and "feels like" temperature
- 💧 User-friendly interface with error handling
- 🚀 No API key required (uses wttr.in free service)

## Requirements

- Python 3.8 or higher
- Django 5.2.2
- requests library

## Installation

1. Clone or download the project to your local machine.

2. Navigate to the project directory:

   ```bash
   cd simple-weather-app
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the required packages:

   ```bash
   pip install django requests
   ```

5. Run database migrations (though the database is already set up):
   ```bash
   python manage.py migrate
   ```

## Usage

1. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

2. Open your web browser and go to `http://127.0.0.1:8000/`.

3. Enter a city name (e.g., "Cebu") in the input field and click "Get Weather" to view the current weather conditions.

## API Information

This app uses the [wttr.in](https://wttr.in/) service, which provides weather data in JSON format without requiring an API key. The endpoint used is `http://wttr.in/{city}?format=j1`.

## Project Structure

- [`weatherapp`](weatherapp): Main Django project directory
  - [`weatherapp/settings.py`](weatherapp/settings.py): Project settings
  - [`weather/urls.py`](weather/urls.py): URL routing
  - [`weatherapp/wsgi.py`](weatherapp/wsgi.py): WSGI configuration
- [`weather`](weather): Django app for weather functionality
  - [`weather/views.py`](weather/views.py): Handles requests and API calls
  - [`weather/urls.py`](weather/urls.py): App-specific URL routing
  - [`weather/templates/weather/index.html`](weather/templates/weather/index.html): HTML template for the weather page
- [`db.sqlite3`](db.sqlite3): SQLite database file
- [`manage.py`](manage.py): Django management script

## Contributing

Feel free to fork the repository and submit pull requests for improvements or bug fixes.

## License

This project is open-source and available under the MIT License.
