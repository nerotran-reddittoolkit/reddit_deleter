from datetime import date
import time
import authentication

# Initialize the reddit object using the authentication script
reddit = authentication.reddit

# Initialize the user's profile as a redditor object
user = reddit.user.me()

# Get the current time from utc
current_time = time.time()
days = 0
seconds = days * 3600 * 24

# Run a loop through the user's comments and delete any whose posted date exceeds the days provided
for id in user.comments.new(limit=None):
    comment = reddit.comment(id=id) # initalize the comment object using the id retrieved from the user
    time = current_time - comment.created # Check if the datetime exceeds the limit
    if time > seconds:
        print("deleting comment: " + comment.id)
        with open("comments.csv", "a") as fa:
            fa.writelines("reddit.com" + comment.submission.permalink + "\t"
                         + comment.body.replace("\n", " ").encode("ascii", "replace").decode()
                          + "\t" + str(date.fromtimestamp(comment.created)) + "\n")
        #comment.delete() # delete the comment

print()

# Run a loop through the user's posts and delete any whose posted date exceeds the days provided
for id in user.submissions.new(limit=None):
    post = reddit.submission(id=id) # initalize the post object using the id retrieved from the user
    time = current_time - post.created # Check if the datetime exceeds the limit
    if time > seconds:
        print("deleting post: " + post.id)
        with open("posts.csv", "a") as fa:
            fa.writelines("reddit.com/r/" + post.subreddit.display_name + "\t" + post.title
                         + "\t" + str(date.fromtimestamp(post.created)) +
                          "\t" + post.selftext.replace("\n", " ").encode("ascii", "replace").decode()
                          + "\n")
        #post.delete() # delete the post

