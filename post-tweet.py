from requests_oauthlib import OAuth1Session


class Tweet(object):
    def __init__(self, user_status):
        credentials = open("creds.txt").readlines()
        self.session = OAuth1Session(credentials[0].strip(),
                                    client_secret=credentials[1].strip(),
                                    resource_owner_key=credentials[2].strip(),
                                    resource_owner_secret=credentials[3].strip()
                                    )
        self.status = user_status
        self.url = "https://api.twitter.com/1.1/statuses/update.json"
        self.post_tweet()

    def post_tweet(self):
        params = {'status': self.status}
        post_object = self.session.post(self.url, params=params)

        if post_object.status_code in [200, 201]:
            print("Tweet was successfully posted")
        else:
            print("Something went wrong")


if __name__ == "__main__":
    status = input("Enter the status you want ")
    tweet_object = Tweet(status)
