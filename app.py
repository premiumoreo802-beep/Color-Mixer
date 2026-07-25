from flask import Flask, render_template, request

app = Flask(__name__)

def mix(c1, c2):
    r = (int(c1[1:3],16)+int(c2[1:3],16))//2
    g = (int(c1[3:5],16)+int(c2[3:5],16))//2
    b = (int(c1[5:7],16)+int(c2[5:7],16))//2
    return f"#{r:02X}{g:02X}{b:02X}"

@app.route("/", methods=["GET","POST"])
def home():
    color1="#ff0000"
    color2="#0000ff"
    mixed=None

    if request.method=="POST":
        color1=request.form["color1"]
        color2=request.form["color2"]
        mixed=mix(color1,color2)

    return render_template(
        "index.html",
        color1=color1,
        color2=color2,
        mixed=mixed
    )

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)