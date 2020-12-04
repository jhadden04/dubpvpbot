import praw
import time
reddit = praw.Reddit(client_id='*',
                     client_secret='*',
                     user_agent='a reddit instance',
                     username='*',
                     password='*')

def imageposter():
    n = 0
    while True:

        subreddits = ["Johntesting","AmongUs", "gaming", "MobileGaming", "Shopping"] # you can add to this

        titles = ["change this"]  # you must change this to your desired title
        reddit.validate_on_submit = True
        text = ["change this"]  # you must change this
        subreddit = reddit.subreddit(subreddits[n])
        try:
            subreddit.submit(titles[0], text[0])

        except:
            continue
        print(f'posted on r/{subreddit}')
        n += 1
        if n >= len(subreddits):
            n = 0
        time.sleep(900)
imageposter()
