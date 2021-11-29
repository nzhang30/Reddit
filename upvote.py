import praw
import time
from textblob import TextBlob

reddit = praw.Reddit('bot')

votes_for_submissions = 0
votes_for_comments = 0
for submission in list(reddit.subreddit('BotTown2').top(time_filter='all')):
    blob = TextBlob(str(submission.title))
    polarity = blob.sentiment.polarity
    submission.comments.replace_more(limit=None)

    if 'biden' in submission.title.lower():
        if polarity > 0:
            submission.upvote()
            votes_for_submissions += 1
            print ('votes_for_submissions=', votes_for_submissions)
            time.sleep(60)
    if 'trump' in submission.title.lower():
        if polarity < 0:
            submission.downvote()
            votes_for_submissions += 1
            print ('votes_for_submissions=', votes_for_submissions)
            time.sleep(60)
    all_comments = submission.comments.list()


    for comment in submission.comments.list():
        blob = TextBlob(str(comment.body))
        if 'biden' in comment.body.lower():
            if polarity > 0:
                comment.upvote()
                votes_for_comments += 1
                print ('votes_for_submissions=', votes_for_submissions)
                print ('votes_for_comments=', votes_for_comments)
                time.sleep(60)
        if 'trump' in comment.body.lower():
            if polarity < 0:
                comment.downvote()
                votes_for_comments += 1
                print ('votes_for_submissions=', votes_for_submissions)
                print ('votes_for_comments=', votes_for_comments)
                time.sleep(60)