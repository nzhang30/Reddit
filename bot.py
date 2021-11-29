import praw
import random
import datetime
import time

# FIXME:
# copy your generate_comment function from the madlibs assignment here

madlibs = [
    "[BIDEN] is a [MEDIOCRE] [PRESIDENT].  He [CAN_DO] [MANY] of [THINGS]. [EVERYONE] [MUST] [LEARN] [POLITICS] and [BECOME] a [POLITICIAN].",
    "I [DISLIKE] [BIDEN].",
    "[BIDEN] and his administration [DISLIKE] [EVERYONE]. [BIDEN] is a [POLITICIAN] who [MUST] [LEARN [POLITICS]. I [DISLIKE] anyone who is a [POLITICIAN].",
    "The [PRESIDENT] is a [POLITICIAN]. During his 4 years as a leader, he [MUST] [LEARN] [MANY] [THINGS]. [EVERYONE] I know has a sense of [DISLIKE] for [BIDEN].",
    "I like the learn about [POLITICS], but my [PRESIDENT], doesn't seem to have much of a [POLITICIAN] mindset. The [PRESIDENT] mmust serve [EVERYONE]. The US people must [LEARN] more [THINGS].",
    "I like [MANY] [THINGS]. But [PRESIDENT] [BIDEN] is not one of them. As a [POLITICIAN], he is [MEDIOCRE] and must learn what his constituents (US People), really want. As [PRESIDENT] he [CAN_DO] a lot of good or harm.",
    "In school, I [LEARN] about [POLITICS] because I want to become a better [PRESIDENT]. I aspire to be a [POLITICIAN] unlike the ones we have today. I [DISLIKE] bipartisanship, and think that [EVERYONE] should be well informed.",
    ]

replacements = {
    'BIDEN' : ['Joe', 'Sleepy Joe', 'Old Man'],
    'MEDIOCRE' : ['Average', 'Tolerable', 'OK', 'Decent'],
    'PRESIDENT' : ['leader', 'commander'],
    'CAN_DO' : ['can do', 'is able to do', 'accomplishes', 'enables me to do', 'helps me do'],
    'MANY'  : ['a bunch', 'a plethora', 'a lot'],
    'THINGS' : ['stuff', 'actions', 'fun things'],
    'POLITICS' : ['Government', 'diplomacy', 'party politics'],
    'EVERYONE' : ['All People', 'Everyone (even young people)', 'Everyone, including you,', 'All adults', 'We'],
    'MUST' : ['should', 'has to', 'need to'],
    'BECOME' : ['become', 'turn into', 'try to be'],
    'POLITICIAN' : ['legislator', 'lawmaker', 'statesmen', 'politico'],
    'LEARN' : ['learn', 'master', 'study', 'comprehend','be taught'],
    'DISLIKE' : ['detest', 'loathe', 'despise', 'oppose'],
    }

def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.
    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.
    For example, if we randomly seleected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    '''
    comment = random.choice(madlibs)
    for key in replacements:
        w = random.choice(replacements[key])
        comment = comment.replace('[' + key + ']',w)
    return comment

# Get raw text as string.
with open("trump_corpus.txt", encoding="utf8") as f:
    text = f.read()

# Seed Random with date
random.seed(datetime.datetime.now())

# Build the model
text_model = markovify.Text(text, state_size=2)

# find random thing to tweet
def generate_comment():
    list_poss_tweets = []
    for i in range(0, 100):
        new_sentence = text_model.make_short_sentence(140)
        list_poss_tweets.append(new_sentence)
        comment = random.choice(list_poss_tweets)
    return comment


# FIXME:
# connect to reddit 
reddit = praw.Reddit('bot')

# FIXME:
# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below
submission_url = 'https://old.reddit.com/r/BotTownHW4/comments/r1hrzx/sandbox/?'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    
    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()
    
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        if str(comment.author) != 'NZ-bot':
            not_my_comments.append(comment)


    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        text = generate_comment()
        submission.reply(text)

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []
        for comment in not_my_comments:
            did_reply = False
            for replies in comment.replies:
                if str(replies.author) == 'NZ-bot':
                    did_reply = True
            if did_reply == False:
                comments_without_replies.append(comment)

        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message

        try:
            comment = random.choice(comments_without_replies)
            try:    
                comment.reply(generate_comment())
            except praw.exceptions.RedditAPIException:
                print('not replying to a comment that has been deleted')
        except IndexError:
            pass


    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    
    try:
        hot_subs = []
        for submission in reddit.subreddit('thoughts').hot(limit=5):
            hot_sub = hot_subs.append(submission.url)
        submission_url = str(random.choice(hot_subs))
        submission = reddit.submission(url=submission_url)
        print(submission_url)
    except praw.exceptions.InvalidURL:
        pass

    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(20)
