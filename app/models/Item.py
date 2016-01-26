""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
from flask import session

class Item(Model):
	def __init__(self):
		super(Item, self).__init__()



	def user_wishlist(self):
		query = "SELECT items.id as item_id, items.item, items.created_at, users.id as creator_id, users.username as creator FROM wishlists JOIN items ON wishlists.item_id=items.id LEFT JOIN users ON items.user_id = users.id WHERE wishlists.user_id = {}".format(session['user_id'])
		testing = self.db.query_db("SELECT * FROM items")
		print testing
		return self.db.query_db(query)

	def other_items(self):

		query = "SELECT items.id as item_id, items.item, items.created_at, users.id as creator_id, users.username as creator FROM wishlists JOIN items ON wishlists.item_id=items.id LEFT JOIN users ON items.user_id = users.id WHERE items.id NOT IN (SELECT items.id FROM wishlists JOIN items ON wishlists.item_id=items.id LEFT JOIN users ON items.user_id = users.id WHERE wishlists.user_id = {})".format(session['user_id'])
		
		return self.db.query_db(query)

	def create(self, item_info):
		query = "INSERT INTO items (item, user_id, created_at, updated_at) VALUES ('{}', {}, NOW(), NOW())".format(item_info['item'], item_info['user_id'])
		self.db.query_db(query)

		query2 = "SELECT id FROM items WHERE item = '{}'".format(item_info['item'])
		item_id = self.db.query_db(query2)

		self.add_wish(item_id[0]['id'], item_info['user_id'])

	def add_wish(self, item_id, user_id):
		query = "INSERT INTO wishlists (item_id, user_id) VALUES ({}, {})".format(item_id, user_id)
		self.db.query_db(query)

	def kill_dream(self, item_id, user_id):
		query = "DELETE FROM wishlists WHERE item_id={} AND user_id={}".format(item_id, user_id)
		self.db.query_db(query)

	def kill_everyones_dream(self, item_id):
		query = "DELETE FROM wishlists WHERE item_id={}".format(item_id)
		self.db.query_db(query)

		query = "DELETE FROM items WHERE id={}".format(item_id)
		self.db.query_db(query)

	def get_item_info(self, id):
		query = "SELECT * FROM items WHERE id={}".format(id)
		return self.db.query_db(query)

	def users_who_want(self, id):
		query = "SELECT users.username FROM wishlists LEFT JOIN users ON wishlists.user_id = users.id WHERE wishlists.item_id = {}".format(id)
		return self.db.query_db(query)