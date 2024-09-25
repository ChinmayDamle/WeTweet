# WeTweet

WeTweet is a social media platform built using Django, allowing users to tweet and view others' tweets. This project features user authentication, responsive design, and a mobile-friendly interface.

## Features
- **User Authentication**: Users can register, log in, and log out.
- **Tweeting Functionality**: Authenticated users can create, edit, and delete tweets.
- **Responsive Design**: The application is optimized for both mobile and desktop views.
- **Search Functionality**: Users can search for tweets by name.
- **Hamburger Menu**: A mobile-friendly menu for navigation.

## Technologies Used
- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Tailwind CSS
- **Database**: SQLite (default), can be configured for others

## Installation
To run WeTweet locally, follow these steps: 
1. Clone the repository using `git clone https://github.com/ChinmayDamle/WeTweet.git` and navigate into the project directory. 
2. Set up a virtual environment (optional but recommended) by running `python -m venv .venv` and activating it. 
3. Install required packages by executing `pip install -r requirements.txt`. 
4. Run migrations with `python manage.py migrate`. 
5. Create a superuser (optional for admin access) using `python manage.py createsuperuser`. 
6. Start the development server by running `python manage.py runserver`. 
7. Access the application by opening your browser and navigating to `http://127.0.0.1:8000/`.

## Usage
- **Register**: Click on "Enter The Matrix" to create a new account. 
- **Login**: Use your credentials to log in. 
- **Tweet**: Post new tweets from your dashboard. 
- **Edit/Delete Tweets**: Manage your tweets easily from your profile. 
- **Search**: Use the search bar to find specific tweets.


## Contributing
If you want to contribute to WeTweet, please fork the repository and submit a pull request. Ensure your code follows the project's coding standards and includes relevant tests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
