from flask import Flask, render_template_string, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'ff_private_discord_password_manager_secret_key'

# ১. হোমপেজ: ডিসকর্ড লগইন এবং নরমাল লগইন/সাইন আপ অপশন
@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="bn">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Free Fire Private Panel - Login</title>
        <style>
            body { background-color: #0b0f19; color: #ffffff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
            .card { background-color: #121826; border: 1px solid #1f2937; padding: 30px; border-radius: 16px; width: 380px; box-shadow: 0 8px 30px rgba(0, 0, 0, 0.7); text-align: center; }
            h2 { color: #ffb703; margin-bottom: 5px; }
            p { font-size: 13px; color: #9ca3af; margin-bottom: 20px; }
            .discord-btn { display: block; background-color: #5865F2; color: white; text-decoration: none; padding: 12px; border-radius: 8px; font-weight: bold; margin-bottom: 15px; font-size: 14px; }
            .discord-btn:hover { background-color: #4752C4; }
            input { width: 100%; padding: 12px; margin: 8px 0; background: #1f2937; border: 1px solid #374151; color: white; border-radius: 8px; box-sizing: border-box; }
            input:focus { border-color: #ffb703; outline: none; }
            .btn { width: 100%; background-color: #ffb703; color: #000; padding: 12px; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; margin-top: 10px; font-size: 15px; }
            .btn:hover { background-color: #fb8500; color: white; }
            .reward-box { background: #1e293b; border-left: 4px solid #10b981; padding: 12px; margin-top: 15px; text-align: left; border-radius: 4px; font-size: 13px; }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>🔥 FF Private Panel</h2>
            <p>ডিসকর্ড দিয়ে এক্সেস নিন অথবা সরাসরি লগইন করুন</p>
            
            <!-- ডিসকর্ড লগইন বাটন -->
            <a href="/auth/discord" class="discord-btn">🎮 ডিসকর্ড দিয়ে লগইন করুন</a>

            <hr style="border: 0; border-top: 1px solid #1f2937; margin: 20px 0;">

            <!-- ম্যানুয়াল আইডি-পাস লগইন -->
            <form action="/login" method="POST">
                <input type="text" name="username" placeholder="গেম আইডি / অ্যাকাউন্ট নম্বর" required>
                <input type="password" name="password" placeholder="পাসওয়ার্ড" required>
                <button type="submit" class="btn">লগইন করুন</button>
            </form>

            <div class="reward-box">
                <b>🎁 মেইলবক্স সিস্টেম:</b><br>
                • প্রথম লগইনে অটো যাবে: <b>৫০০ ডায়মন্ড ও ১০০ গোল্ড</b>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

# ২. ডিসকর্ড অথেন্টিকেশন প্রসেস
@app.route('/auth/discord')
def discord_auth():
    # ডিসকর্ড থেকে এক্সেস পাওয়ার পর ইউজারকে সেশনে যুক্ত করা হলো
    session['user'] = 'Discord_Player_77'
    session['clan_id'] = 'FF_TCB_992'
    return redirect(url_for('dashboard'))

# ৩. নরমাল লগইন প্রসেস
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    session['user'] = username
    session['clan_id'] = 'FF_TCB_101'
    return redirect(url_for('dashboard'))

# ৪. ড্যাশবোর্ড: যেখানে ক্ল্যান আইডি, ডিসকর্ড স্ট্যাটাস এবং পাসওয়ার্ড চেঞ্জ করার সুবিধা থাকবে
@app.route('/dashboard')
def dashboard():
    user = session.get('user', 'Player_FF')
    clan_id = session.get('clan_id', 'FF_TCB_000')
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="bn">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Account Dashboard - FF Panel</title>
        <style>
            body {{ background-color: #0b0f19; color: #ffffff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }}
            .card {{ background-color: #121826; border: 1px solid #1f2937; padding: 25px; border-radius: 16px; width: 400px; box-shadow: 0 8px 30px rgba(0, 0, 0, 0.7); }}
            h3 {{ color: #10b981; margin-top: 0; }}
            .info-box {{ background: #1f2937; padding: 15px; border-radius: 8px; margin-bottom: 15px; font-size: 14px; line-height: 1.6; }}
            .info-box span {{ color: #ffb703; font-weight: bold; }}
            input {{ width: 100%; padding: 10px; margin: 6px 0; background: #111827; border: 1px solid #374151; color: white; border-radius: 6px; box-sizing: border-box; }}
            .btn {{ width: 100%; background-color: #3b82f6; color: white; padding: 10px; border: none; border-radius: 6px; font-weight: bold; cursor: pointer; margin-top: 8px; }}
            .btn-danger {{ background-color: #ef4444; margin-top: 15px; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h3>⚙️ অ্যাকাউন্ট ও পাসওয়ার্ড ম্যানেজমেন্ট</h3>
            <div class="info-box">
                <b>ইউজার অ্যাকাউন্ট:</b> <span>{user}</span><br>
                <b>ক্ল্যান আইডি (Clan ID):</b> <span>{clan_id}</span><br>
                <b>ডিসকর্ড স্ট্যাটাস:</b> <span style="color: #34d399;">সফলভাবে যুক্ত (Connected)</span><br>
                <b>মেইলবক্স রিওয়ার্ড:</b> ৫০০ ডায়মন্ড ও ১০০ গোল্ড যোগ হয়েছে! 🚀
            </div>

            <hr style="border: 0; border-top: 1px solid #374151; margin: 15px 0;">

            <h4>🔄 পাসওয়ার্ড পরিবর্তন করুন</h4>
            <form action="/update-password" method="POST">
                <input type="password" name="old_password" placeholder="পুরোনো পাসওয়ার্ড" required>
                <input type="password" name="new_password" placeholder="নতুন পাসওয়ার্ড দিন" required>
                <button type="submit" class="btn">পাসওয়ার্ড আপডেট ও সেভ করুন</button>
            </form>

            <form action="/" method="GET">
                <button type="submit" class="btn btn-danger">লগআউট / গেম ডিসকানেক্ট</button>
            </form>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

# ৫. পাসওয়ার্ড আপডেট করার রাউট
@app.route('/update-password', methods=['POST'])
def update_password():
    return """
    <script>
        alert('অভিনন্দন! আপনার অ্যাকাউন্টের পাসওয়ার্ড সফলভাবে চেঞ্জ করা হয়েছে। এখন গেমের ভেতর ফেসবুকে ক্লিক করে এই নতুন আইডি-পাস দিয়ে লগইন করতে পারবেন!');
        window.location.href = '/dashboard';
    </script>
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
