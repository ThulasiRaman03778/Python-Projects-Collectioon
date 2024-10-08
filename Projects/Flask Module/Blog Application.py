from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data structure to hold blog posts
posts = [
    {'id': 1, 'title': 'First Post', 'content': 'This is the first post!'},
    {'id': 2, 'title': 'Second Post', 'content': 'This is the second post!'},
    {'id': 3, 'title': 'Third Post', 'content': 'Learning Flask is fun!'},
    {'id': 4, 'title': 'Fourth Post', 'content': 'Building a blog is a great project!'},
    {'id': 5, 'title': 'Fifth Post', 'content': 'Python makes web development easier.'}
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    return render_template('post.html', post=post)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_id = len(posts) + 1
        posts.append({'id': new_id, 'title': title, 'content': content})
        return redirect(url_for('index'))
    return render_template('new_post.html')

@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if request.method == 'POST':
        post['title'] = request.form['title']
        post['content'] = request.form['content']
        return redirect(url_for('post', post_id=post_id))
    return render_template('edit_post.html', post=post)

@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    global posts
    posts = [p for p in posts if p['id'] != post_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
