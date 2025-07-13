from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    response = VoiceResponse()
    intro = "היי, כאן שירי. מצאנו עבורך כספים פנסיוניים ממעסיקים קודמים – בלי כאב ראש, ותשלום רק אחרי הצלחה. אפשר לדבר רגע?"
    response.say(intro, voice="Polly.Carmit", language="he-IL")
    response.pause(length=1)
    response.say("אם זה מעניין אותך, תגיד כן. ואם לא, תגיד לא.", voice="Polly.Carmit", language="he-IL")
    return Response(str(response), mimetype="text/xml")

@app.route("/", methods=["GET"])
def index():
    return "Shiri AI Voice Server is live."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
