from decouple import config
from flask import Flask, render_template, request
from .models import DB, User
from .twitter import add_or_update_user

def create_app():
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	DB.init_app(app)

	@app.route('/')
	def root():
		DB.create_all()
		users = User.query.all()
		return render_template('base.html', title='Home', users=users)
	
	@app.route('/user', methods=['POST'])
	@app.route('/user/<name>', methods=['GET'])
	def user(name=None, message=''):
		name = name or request.values['user_name']
		try: 
			if request.method == 'POST': 
				add_or_update_user(name)
				message = f'User {name} succesfully added!'
			tweets = User.query.filter(User.name==name).one().tweets
		except Exception as e:
			message = f'Error while trying to add user {name}: {e}'
			tweets = []
		return render_template('user.html', title=name, message=message)

	@app.route('/reset')
	def reset(): 
		DB.drop_all()
		DB.create_all()
		return render_template('base.html', title='DB Reset!', users=[])

	return app

# to call in terminal per A.Gallant: from twitoff.app import DB
