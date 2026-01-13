from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    x = ["cin ali", "most helpful", "worked hardest", "the best"]
    sonuc = random.choice(x)
    return f"""
    <html>
        <body style="text-align:center; font-family:Arial;">
            <h1>🎲 Rastgele Cevap</h1>
            <h2>{sonuc}</h2>
            <p>Sayfayı yenile, yeni cevap gelsin 😄</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
