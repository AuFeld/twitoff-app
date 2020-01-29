from flask import Flask
app = Flask(__name__)

@app.route('/')
def home(): 
	#deployed model goes here
	return "<h1>Hello, World!</h1>"

if __name__ == "__main__":
	app.run(debug=True, port = 8080)

@app.route('/user/<username>')
def show_user_profile(username): 
    # show the user profile for that user
    return f'User {username}'

@app.route('/post/<post_id>')
def show_post(post_id):
    # show the post with the given id, the id in an integer
    return 'Post %d' % (post_id + 1)