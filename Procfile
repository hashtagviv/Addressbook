release: pip install -e .
app: npx webpack
web: gunicorn -w 2 addressbook:app