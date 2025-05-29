import pymongo
import os
from flask import request
from dotenv import load_dotenv

load_dotenv()

Mongo_uri = os.getenv("MONGO_URI")

client = pymongo.MongoClient(MONGO_URI)
userdb = client['userdb']
users = userdb.customers


def insert_data():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		password = request.form['pass']

		reg_user = {}
		reg_user['name'] = name
		reg_user['email'] = email
		reg_user['password'] = password

		if users.find_one({"email":email}) == None:
			users.insert_one(reg_user)
			return True
		else:
			return False


def check_user():

	if request.method == 'POST':
		email = request.form['email']
		password = request.form['pass']

		user = {
			"email": email,
			"password": password
		}

		user_data = users.find_one(user)
		if user_data == None:
			return False, ""
		else:
			return True, user_data["name"]
