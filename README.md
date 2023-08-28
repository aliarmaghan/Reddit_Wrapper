# Reddit_Wrapper

This is a basic web application that fetches articles from a subreddit using the Reddit API and displays them on a simple front end. The application uses Django for the backend and Bootstrap for basic styling.

## Features

- Fetches the last 10 threads from a specified subreddit using the Reddit API.
- Displays thread information including title, author, creation date, and link to the original thread.
- Provides a responsive and functional user interface.

## Getting Started

Follow these steps to set up and run the project locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/aliarmaghan/Reddit_Wrapper.git

2. Install dependencies:

     ```bash
     pip install -r requirements.txt

3. Configure Reddit API Access:
   
   - Sign up for Reddit API access and obtain the client ID and client secret using this link https://www.reddit.com/prefs/apps.
   - Update the RedditWrapper_App/reddit_client.py file with your credentials.

4. Configure Reddit API Access:

     ```bash
     python manage.py runserver

5. Access the web application:

    - Open your web browser and navigate to http://127.0.0.1:8000/

# Technologies Used

  - Django: Web framework for the backend.
  - Bootstrap: Front-end framework for basic styling.
  - PRAW: Python wrapper for the Reddit API.

# Directory Structure

  - `RedditWrapper_App`: Django app containing the Reddit API integration.
  - `static`: Static files including CSS and JavaScript.
  - `templates`: HTML templates for rendering the front end.
  - `manage.py`: Django management script.
  - `requirements.txt`: List of Python dependencies.

# Output

   ![output](https://github.com/aliarmaghan/Reddit_Wrapper/blob/main/Output/RedditWrapper_Output.jpeg)
