# WeTweet

WeTweet is a social media platform built with **Django** and **TailwindCSS** that allows users to post tweets, view other users' tweets, and manage their own posts. This project showcases my **front-end development** and **Django back-end** skills. The project emphasizes user authentication, and CRUD functionality for posts.

## Features

- **User Authentication**: Secure login, registration, and logout functionalities using Django's built-in authentication.
- **Tweet Management**: Users can create, edit, and delete their tweets.
- **Image Support**: Users can attach an image to their tweets.
- **Dynamic Content**: The layout adjusts dynamically to handle tweets with and without images.

## Technologies Used

- **Backend**: Django Framework
- **Frontend**: TailwindCSS for styling
- **Database**: SQLite (can be replaced with PostgreSQL or MySQL for production)
- **HTML**: Used Django templating engine to render dynamic content
- **Python**: Server-side scripting
- **JavaScript**: Used to add interactivity

## How to Run the Project

1. Clone the repository:

    ```bash
    git clone https://github.com/ChinmayDamle/WeTweet.git
    ```

2. Navigate to the project directory:

    ```bash
    cd WeTweet
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Django development server:

    ```bash
    python manage.py runserver
    ```



## Skills Demonstrated

- **Django Expertise**: Built robust models and views to handle user authentication, form handling, and dynamic content rendering.
- **TailwindCSS**: Used utility-first CSS to ensure responsiveness and a clean UI.
- **HTML & Templating**: Mastered Django's templating system to dynamically inject content into HTML.
- **Python & Django ORM**: Developed efficient server-side logic and database queries.
- **Version Control**: Managed the project using Git and GitHub for collaboration and versioning.


## Future Enhancements

- Add real-time tweet updates using Django Channels or WebSockets.
- Implement user mentions and hashtags.
- Add unit and integration tests for better test coverage.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
