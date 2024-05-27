# Weather Desktop Notifier
## Description: 
Weather Desktop Notifier is a desktop application built using Python and Tkinter. It allows users to enter the name of a city and receive a desktop notification with the current weather conditions of that city. The application fetches weather data from the OpenWeatherMap API and displays the temperature, atmospheric pressure, humidity, and a brief description of the weather.

## Features
- User-friendly graphical interface.

- Fetches and displays real-time weather data.

- Provides temperature, atmospheric pressure, humidity, and weather description.

- Desktop notifications with weather details.

- Technologies Used

- Python: The core programming language used to build the application.

- Tkinter: The standard GUI library for Python, used to create the application’s graphical interface.

- Requests: A simple HTTP library for Python, used to make API requests to OpenWeatherMap.

- Plyer: A library for accessing features commonly found on various platforms, used here to show desktop notifications.

## Prerequisites
Before running the application, ensure you have the following installed:

- Python 3.x
- The required Python libraries (Tkinter, Requests, Plyer)

You can install the required libraries using pip:
- pip install requests plyer

## How to Run,
Clone the repository:
- git clone https://github.com/Mustafaahmed00/weather-notification.git
Navigate to the project directory:
- cd weather-notification
Run the application:
- python weather.py

## Usage
Open the application.
Enter the name of the city you want to get the weather information for.
Click on the "Get Notification" button.
A desktop notification will appear with the current weather details of the specified city.

## Example
Here's an example of what the notification will look like:

YOUR WEATHER REPORT

Here is the weather description of London:

Temperature = 15.00°C

Atmospheric pressure = 1012 hPa

Humidity = 72%

Description of the weather = scattered clouds

## Acknowledgements
- OpenWeatherMap for providing the weather data API.
- Python for the programming language.
- Tkinter for the GUI toolkit.
- Plyer for the platform-independent API.
