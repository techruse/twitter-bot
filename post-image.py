import json
from requests_oauthlib import OAuth1Session


class Tweet(object):
    def __init__(self, user_status, user_media):
        credentials = open("creds.txt").readlines()
        self.session = OAuth1Session(credentials[0].strip(),
                                    client_secret=credentials[1].strip(),
                                    resource_owner_key=credentials[2].strip(),
                                    resource_owner_secret=credentials[3].strip()
                                    )
        self.media_id = None
        self.status = user_status
        self.user_media = user_media
        self.url = "https://api.twitter.com/1.1/statuses/update.json"
        self.url_media = "https://upload.twitter.com/1.1/media/upload.json"
        self.post_tweet()

    def post_tweet(self):
        if self.user_media is not None:
            self.media_id = self.get_media_id()
        else:
            print("user meida is not none")

        params = {'status': self.status, 'media_ids': [self.media_id]}
        print(params)
        post_object = self.session.post(self.url, params=params)

        if post_object.status_code in [200, 201]:
            print("Tweet was successfully posted")
        else:
            print("Something went wrong")

    def get_media_id(self):
        files = {"media" : open(self.user_media, 'rb')}
        req_media = self.session.post(self.url_media, files = files)

        if req_media.status_code in [200, 201]:
            media_id = json.loads(req_media.text)['media_id']
            return media_id
        else:
            return False


if __name__ == "__main__":
    status = input("Enter the status you want ")
    image = input("Enter the image path with the name, or leave it blank ")
    tweet_object = Tweet(status, image)
