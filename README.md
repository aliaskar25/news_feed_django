1. Create an .env file inside news_feed folder. With this parameters: \
MAIL_USERNAME="your@gmail.com" \
MAIL_PASSWORD="gmail's password for app" #see here:# https://support.google.com/accounts/answer/185833?hl=en# \
SECRET_KEY="any word" \
**Like in .env.example file**

2. **in terminal run:** docker-compose up --build \
3. **in other terminal run:** docker-compose run web news_feed/manage.py createsuperuser \
4. **test it** \

