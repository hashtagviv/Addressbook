import flask

app = flask.Flask(__name__)

app.config.from_object('addressbook.config')

app.config.from_envvar('ADDRESSBOOK_SETTINGS', silent=True)

import addressbook.api # noqa: E402  pylint: disable=wrong-import-position
import addressbook.views # noqa: E402  pylint: disable=wrong-import-position
import addressbook.model # noqa: E402  pylint: disable=wrong-import-position