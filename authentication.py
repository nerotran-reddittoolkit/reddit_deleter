import praw

# Initialize a dictionary for hold the authentication info
authentication = {
    "client_id": "",
    "client_secret": "",
    "username": "",
    "password": "",
    "user_agent": ""
}

# Read authentication info for OAuth2 from a text file for security reason
with open("myauth.reddit", "r") as file_read:
        for field in authentication:
            authentication[field] = file_read.readline().strip("\n")

#initialize a reddit object
reddit = praw.Reddit(client_id=authentication["client_id"],
                     client_secret=authentication["client_secret"],
                     username=authentication["username"],
                     password=authentication["password"],
                     user_agent=authentication["user_agent"],)