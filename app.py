from flask import Flask, render_template_string, request, redirect
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def home():
    # সরাসরি এইচটিএমএল কোড এখানে রাখতে পারেন অথবা HTML ফাইলের নাম দিয়ে কাজ চালাতে পারেন
    # ফোল্ডারের ঝামেলা এড়াতে সরাসরি HTML কোড এখানে পেস্ট করে দেওয়া সবচেয়ে নিরাপদ
    html_content = """
    <!DOCTYPE html>
    <html lang="bn">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Custom Project Panel</title>
        <style>
            body { background-color: #0b0f19; color: #ffffff; font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .card { background-color: #121826; border: 1px solid #1f2937; padding: 30px; border-radius: 12px; width: 350px; text-align: center; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5); }
            h1 { font-size: 22px; margin-bottom: 10px; }
            p { font-size: 13px; color: #9ca3af; margin-bottom: 20px; }
            .discord-btn { display: block; background-color: #5865F2; color: white; text-decoration: none; padding: 12px; border-radius: 8px; font-weight: bold; }
            .discord-btn:hover { background-color: #4752C4; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Custom Project</h1>
            <p>ডিসকর্ড দিয়ে লগইন করুন এবং সার্ভার অ্যাক্সেস পান।</p>
            <a href="/auth/discord" class="discord-btn">Entrar com Discord</a>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/auth/discord')
def discord_login():
    return "ডিসকর্ড লগইন রিডাইরেক্ট পেজ"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)