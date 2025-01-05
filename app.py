from flask import Flask, request, render_template
import sqlite3

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)

# ホームページ
@app.route('/')
def home():
    return "Welcome to ZIRI!"

# フォームページ
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        email = request.form['email']
        # データベースに保存
        conn = sqlite3.connect('ziri.db')
        c = conn.cursor()
        c.execute('INSERT INTO users (name, age, email) VALUES (?, ?, ?)', (name, age, email))
        conn.commit()
        conn.close()
        return f"Hello, {name}! Your details have been saved to the database!"
    return render_template('form.html')

# 保存されたユーザーを表示
@app.route('/users')
def users():
    conn = sqlite3.connect('ziri.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')  # データベースから全てのユーザーを取得
    rows = c.fetchall()
    conn.close()
    return render_template('users.html', users=rows)

# ユーザー削除
@app.route('/delete/<int:id>', methods=['POST'])
def delete_user(id):
    conn = sqlite3.connect('ziri.db')
    c = conn.cursor()
    c.execute('DELETE FROM users WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return "User deleted successfully! <a href='/users'>Go back to Users</a>"

# アプリケーションの起動
if __name__ == '__main__':
    app.run(debug=True)
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    conn = sqlite3.connect('ziri.db')
    c = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        email = request.form['email']
        c.execute('UPDATE users SET name = ?, age = ?, email = ? WHERE id = ?', (name, age, email, id))
        conn.commit()
        conn.close()
        return "User updated successfully! <a href='/users'>Go back to Users</a>"
    c.execute('SELECT * FROM users WHERE id = ?', (id,))
    user = c.fetchone()
    conn.close()
    return render_template('edit.html', user=user)

