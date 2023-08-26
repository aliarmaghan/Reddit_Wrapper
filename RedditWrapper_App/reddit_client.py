import praw

def get_reddit_data(subreddit_name):
    reddit = praw.Reddit(
        client_id='wPkY7dggIHCHp9rcINdTCA',
        client_secret='LlzCdZPh2hO_J2A57Sg_pfHv4evP7w',
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