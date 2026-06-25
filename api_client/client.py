import requests


class NewsAPIClient:
    def __init__(self, base_url, token=None):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        if token:
            self.session.headers.update({'Authorization': f'Token {token}'})

    def register(self, username, email, password):
        
        resp = self.session.post(f"{self.base_url}/api/users/", json={
            'username': username,
            'email': email,
            'password': password
        })
        return resp.json() if resp.status_code == 201 else resp.json()

    def login(self, username, password):

        resp = self.session.post(f"{self.base_url}/api/token/", json={
            'username': username,
            'password': password
        })
        if resp.status_code == 200:
            data = resp.json()
            self.session.headers.update({'Authorization': f"Token {data['token']}"})
            return data
        return resp.json()

    def get_users(self):

        return self.session.get(f"{self.base_url}/api/users/").json()

    def get_user(self, user_id):

        return self.session.get(f"{self.base_url}/api/users/{user_id}/").json()

    def create_news(self, title, content, summary=""):

        resp = self.session.post(f"{self.base_url}/api/news/", json={
            'title': title,
            'content': content,
            'summary': summary
        })
        return resp.json() if resp.status_code == 201 else resp.json()

    def get_news(self, news_id=None):

        if news_id:
            return self.session.get(f"{self.base_url}/api/news/{news_id}/").json()
        return self.session.get(f"{self.base_url}/api/news/").json()

    def update_news(self, news_id, **kwargs):

        resp = self.session.patch(f"{self.base_url}/api/news/{news_id}/", json=kwargs)
        return resp.json() if resp.status_code == 200 else resp.json()

    def delete_news(self, news_id):

        return self.session.delete(f"{self.base_url}/api/news/{news_id}/").status_code