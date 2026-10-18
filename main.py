
from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI(
    title="VayuSense Voice Endpoint",
    docs_url=None,
    redoc_url=None,
)

@app.get("/")
def health_check():
    return {"status": "VayuSense voice endpoint is running"}

@app.get("/twiml")
def get_voice_instructions():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say language="en-IN">
        Hello. This is a VayuSense emergency alert.
        A fall has been detected.
        The person may need help.
        Please check on them immediately.
    </Say>
</Response>"""

    return Response(
        content=xml,
        media_type="application/xml",
    )
