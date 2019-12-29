# reddit_deleter
require: praw (reddit api wrapper)

A script I made that go through my reddit comments and posts, look for any that is older than a preset number of days (currently 100), copy the info of them down into .csv files before deleting the outdated posts and comments.

My authentication info is read from a text file and not uploaded to github for security reasons.

Personally, I run the script daily at 7am by using windows task scheduler to run a batch file.
