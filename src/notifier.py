import datetime as dt
import time
import config
from mailer import Mailer
from solr import Solr
from database import Database

class Notifier():
    def __init__(self, interval):
        self.last_send_time = dt.datetime.now()
        self.interval = dt.timedelta(minutes=config.INTERVAL)
        self.mailer = Mailer(config.SMTP_HOST, config.SMTP_PORT, config.SMTP_USERNAME, config.SMTP_PASSWORD)
        self.solr = Solr(config.SOLR_HOST, config.SOLR_PORT, config.SOLR_CORE)
        self.db = Database(config.MYSQL_HOST, config.MYSQL_PORT, config.MYSQL_USERNAME, config.MYSQL_PASSWORD)
        self.loop()
    
    def get_solr_docs(self):
        num_found = 100
        offset = 0
        rows = 100
        solr_docs = []
        while offset < num_found:
            try:
                res = self.solr.select({
                    "q": "*:*",
                    "fl": "id,deleted,document,title_txt_*,scanDate", 
                    "fq": f"scanDate:[{self.last_send_time} TO NOW]",
                    "rows": rows, 
                    "start": offset
                })
                solr_docs += res["response"]["docs"]
                num_found = res["response"]["numFound"]
            except: pass
            finally:
                offset += rows
        return solr_docs

    def get_users(self):
        return self.db.fetch("SELECT id, email, username FROM login")

    def get_user_favs(self, user_id):
        return self.db.fetch(f"SELECT DocId from Favorites HWERE UserId={user_id}")

    def loop(self):
        while True:
            time.sleep(self.last_send_time.timestamp() + self.interval - time.time())
            solr_docs = self.get_solr_docs()
            users = self.get_users()
            for user in users:
                user_favs = self.get_user_favs(user)
                user_favs_solr_docs = []
                for doc in solr_docs:
                    if doc.id in user_favs:
                        user_favs_solr_docs.append(doc)
                
                print()
                print(f"Hallo {user.username}")
                print(user_favs_solr_docs)

            self.last_send_time = self.last_send_time + self.interval

def main():
    Notifier()

if __name__ == "__main__":
    main()