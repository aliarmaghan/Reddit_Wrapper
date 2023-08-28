import praw

def get_reddit_data(subreddit_name):
    reddit = praw.Reddit(
        client_id='your_client_id',
        client_secret='your_client_secret',
        user_agent='your_user_agent',
    )


    subreddit = reddit.subreddit(subreddit_name)
    threads = subreddit.new(limit=10)

    data = []
    for thread in threads:
        data.append({
            'title': thread.title,
            'author': thread.author.name,
            'creation_date': thread.created_utc,
            'link': thread.url,
        })

    return data