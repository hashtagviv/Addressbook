import os
import shutil
import tempfile
import uuid
import hashlib
from operator import itemgetter
import flask
import arrow
import addressbook
from addressbook.model import get_db

def delete_address(id):
    query = "delete from Addresses where lastname=\ '" + id + '\''
    get_db.cursor().execute(query)

def add_address(lastname, firstname, company, email, category):
    query = "insert in to Addresses lastname, firstname, company VALUES(\'"
    query += lastname + '\',' + firstname + '\',' + company + '\',' + email + '\',' + category + ')'
    get_db.cursor().execute(query)

@addressbook.app.route('/', methods=['GET', 'POST'])
def show_index():
    query = "select * from addresses"
    addresses = get_db().cursor().execute(query)
    context = {'addresses': addresses}
    return flask.render_template('index.html', **context)

@addressbook.app.route('/address/new', methods=['GET', 'POST'])
def show_new_address():
    if flask.request.method == 'POST':
        con = get_db()
        cur = con.cursor()
        query = "insert into addresses(lastname,firstname,Company,Email, Category) values(\'"
        query += flask.request.form['lastname'] + "\',\'"
        query += flask.request.form['firstname'] + "\',\'"
        query += flask.request.form['category'] + "\',\'"
        query += flask.request.form['company'] + "\',\'"
        query += flask.request.form['email'] + "\')"
        addressid = cur.execute(query).lastrowid
        query = "insert into contactinfo(addressid, workphone, homephone, mobile, urllink) values(\'"
        query += str(addressid) + "\',\'"
        query += flask.request.form['workphone'] + "\',\'"
        query += flask.request.form['homephone'] + "\',\'"
        query += flask.request.form['mobile'] + "\',\'"
        query += flask.request.form['url'] + "\')"
        cur.execute(query)
        query = "insert into addressinfo(addressid, address_, city, country, state_, zip) values(\'"
        query += str(addressid) + "\',\'"
        query += flask.request.form['address'] + "\',\'"
        query += flask.request.form['city'] + "\',\'"
        query += flask.request.form['country'] + "\',\'"
        query += flask.request.form['state'] + "\',\'"
        query += flask.request.form['zip'] + "\')"
        cur.execute(query)
        return flask.redirect(flask.url_for('show_index'))
        
    return flask.render_template('create.html')

@addressbook.app.route('/address/<int:address_id>', methods=['GET', 'POST'])
def show_address(address_id):
    if flask.request.method == 'POST':
        if 'submitchanges' in flask.request.form:
            query = "update addresses set lastname = \'" + flask.request.form['lastname'] + '\','
            query += "firstname = \'" + flask.request.form['firstname'] + "\',"
            query += "firstname = \'" + flask.request.form['firstname'] + "\',"
            query += "Category = \'" + flask.request.form['category'] + "\',"
            query += "Company = \'" + flask.request.form['company'] + "\',"
            query += "email = \'" + flask.request.form['email'] + "\' "
            query += "where addressid = " + str(address_id)
            get_db().cursor().execute(query)
            query = "update contactinfo set "
            query += "workphone = \'" + flask.request.form['workphone'] + "\',"
            query += "homephone = \'" + flask.request.form['homephone'] + "\',"
            query += "mobile = \'" + flask.request.form['mobile'] + "\',"
            query += "urllink = \'" + flask.request.form['urllink'] + "\' "
            query += "where addressid = " + str(address_id)
            get_db().cursor().execute(query)
            query = "update addressinfo set address_ = \'" + flask.request.form['address'] + '\','
            query += "city = \'" + flask.request.form['city'] + "\',"
            query += "country = \'" + flask.request.form['country'] + "\',"
            query += "state_ = \'" + flask.request.form['state'] + "\',"
            query += "zip = \'" + flask.request.form['zip'] + "\' "
            query += "where addressid = " + str(address_id)
            get_db().cursor().execute(query)
        elif 'delete' in flask.request.form:
            con = get_db()
            cur = con.cursor()
            query = "delete from addresses where addressid = " + str(address_id)
            cur.execute(query)
            query = "delete from addressinfo where addressid = " + str(address_id)
            cur.execute(query)
            query = "delete from contactinfo where addressid = " + str(address_id)
            cur.execute(query)
            return flask.redirect(flask.url_for('show_index'))
    connection = get_db()
    cur = connection.execute("Select * from Addresses where addressid = " + str(address_id))
    address = cur.fetchone()
    cur = connection.execute("Select * from contactinfo where addressid = " + str(address_id))
    contactinfo = cur.fetchone()
    cur = connection.execute("Select * from addressinfo where addressid = " + str(address_id))
    addressinfo = cur.fetchone()
    name = address["firstname"] + " " + address["lastname"]
    context = {"address": address, "contactinfo": contactinfo, "addressinfo": addressinfo, "name": name}
    return flask.render_template('address.html', **context)
