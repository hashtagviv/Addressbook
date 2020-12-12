import addressbook
from addressbook.model import get_db
import flask

@addressbook.app.route('/api/v1/add/', methods=["GET", "POST"])
def get_addresses():
    """get {size} addressses address id"""
    connection = get_db()
    size = flask.request.args.get("size", default=50000, type=int)
    page = flask.request.args.get("page", default=0, type=int)
    cur = connection.execute("Select addressid, firstname,lastname,Category, Company,Email from Addresses limit ? offset ?",(size, page*size))
    results = cur.fetchall()
    context = {}
    # for address in results:
    #     address["url"] = "/api/v1/add/" + str(address["addressid"])
    context["data"] = results
    # context["url"] = flask.request.path
    next_page = page + 1
    cur = connection.execute("Select Count(*) from Addresses")
    results = cur.fetchone()["Count(*)"]
    # if size * page + size < results:
    #     context["next"] = "/api/v1/add/?size={}&page={}".format(size, next_page)
    # else:
    #     context["next"] = ""
    
    # context["size"] = size
    # context["results"] = results
    return flask.jsonify(**context)

@addressbook.app.route('/api/v1/add/<int:address_id>/', methods=["GET"])
def get_address(address_id):
    """Get individual address"""
    connection = get_db()
    query = "select lastname,firstname,company,email,category from Addresses where addressid = " + str(address_id)
    address = connection.execute(query).fetchone()
    context = address
    return flask.jsonify(**context)

@addressbook.app.route('/api/v1/ci/<int:address_id>/', methods=["GET"])
def get_contactinfo(address_id):
    """Get contact info for individual"""
    connection = get_db()
    query = "select workphone,homephone,mobile,urllink from contactinfo where addressid = " + str(address_id)
    contactinfo = connection.execute(query).fetchone()
    context = {}
    context = contactinfo
    return flask.jsonify(**context)

@addressbook.app.route('/api/v1/ai/<int:address_id>/', methods=["GET"])
def get_addressinfo(address_id):
    """Get address info for individual"""
    connection = get_db()
    query = "select address_,city,country,state_,zip from addressinfo where addressid = " + str(address_id)
    contactinfo = connection.execute(query).fetchone()
    context = contactinfo
    return flask.jsonify(**context)
