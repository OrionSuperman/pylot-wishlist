"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from flask import session, flash

class Items(Controller):
	def __init__(self, action):
	    super(Items, self).__init__(action)
	    self.load_model('Item')

	def index(self):
	    """ 
	    A loaded model is accessible through the models attribute 
	    self.models['WelcomeModel'].get_all_users()
	    """
	    return self.load_view('index.html')

	def dashboard(self):
		wishlist = self.models['Item'].user_wishlist()
		

		other_items = self.models['Item'].other_items()
		

		return self.load_view('dashboard.html', wishlist=wishlist, other_items=other_items)

	def add(self):

		return self.load_view('additem.html')

	def create(self):
		print '*' * 50
		print session['user_id']
		
		request.form['item']
		
		item_info = {
		'item' : request.form['item'],
		'user_id' : session['user_id']
		}
		
		self.models['Item'].create(item_info)
		print '*' * 50
		return redirect('/dashboard')

		# except:
		# 	flash('item unable to be added')
		# 	return redirect('/wish_item/add')

	def wish(self):
		self.models['Item'].add_wish(request.form['item_id'], session['user_id'])
		return redirect('/dashboard')

	def kill_dream(self):
		self.models['Item'].kill_dream(request.form['item_id'], session['user_id'])
		return redirect('/dashboard')

	def kill_everyones_dream(self):

		self.models['Item'].kill_everyones_dream(request.form['item_id'])
		return redirect('/dashboard')

	def item_view(self, id):
		item_info = self.models['Item'].get_item_info(id)
		piners = self.models['Item'].users_who_want(id)
		
		return self.load_view('item.html', item_info=item_info[0], piners=piners)