import os

SMTP_HOST = os.getenv("SMTP_HOST", "localhost")
SMTP_PORT = os.getenv("SMTP_PORT", 587)
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_FROM = os.getenv("SMTP_FROM", "noreply@example.com")
SOLR_HOST = os.getenv("MOPSY_SOLR_HOST", "localhost")
SOLR_PORT = os.getenv("MOPSY_SOLR_PORT", 8983)
SOLR_CORE = os.getenv("MOPSY_SOLR_CORE", "mopsy")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = os.getenv("MYSQL_PORT", 3306)
MYSQL_USERNAME = os.getenv("MYSQL_USERNAME", "mopsy")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "mopsy")
INTERVAL = os.getenv("INTERVAL", 1440)                   # Mail Send Interval in Minutes