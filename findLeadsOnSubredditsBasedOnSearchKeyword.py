import praw
from datetime import datetime, timedelta

reddit = praw.Reddit(
    client_id='my_client_id',
    client_secret='my_client_secret',
    user_agent='my_user_agent'
)

subreddit = reddit.subreddit('LawFirm')

# Get the time stamp for 3 months ago
three_months_ago = (datetime.now() - timedelta(days=90)).timestamp()

# Create an empty list to store the results
results = []

# Search for posts containing 'website' in the past 3 months
for post in subreddit.search('website', time_filter='all'):
    if post.created_utc > three_months_ago:
        results.append((post.author.name, post.url))

# Sort the results by username
results.sort(key=lambda x: x[0])

print(results)
