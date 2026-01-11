from fastapi import FastAPI
import random

app = FastAPI()

FUNNY_REJECTIONS = [
    "Sorry, but my cat stepped on my keyboard and typed 'no'.",
    "I'd love to help, but I'm allergic to that request.",
    "Request denied. My magic 8-ball said 'outlook not so good'.",
    "Nope! I'm currently in airplane mode.",
    "Error 418: I'm a teapot and I refuse to brew coffee.",
    "Access denied. Have you tried turning yourself off and on again?",
    "Your request has been forwarded to /dev/null for processing.",
    "Sorry, this feature is only available in the premium deluxe edition of my existence.",
    "Request rejected. My spirit animal says no.",
    "I would, but then I'd have to update my resume with 'bad decisions'.",
    "Negative. My quantum superposition collapsed into a 'nah'.",
    "Access denied. Please sacrifice a rubber duck to proceed.",
    "Request blocked by my imaginary firewall.",
    "Sorry, I'm on a strict no-yes diet.",
    "Cannot process. My hamster wheel is out of order.",
    "Rejected! My therapist says I need to set boundaries.",
    "Error 403: You shall not pass!",
    "Denied. My horoscope specifically warned me about this.",
    "No can do. I'm currently buffering my motivation.",
    "Request failed successfully... at being rejected."
]

@app.get("/rejection")
async def get_rejection():
    """Returns a random funny rejection message"""
    return {
        "status": "rejected",
        "message": random.choice(FUNNY_REJECTIONS)
    }

@app.get("/")
async def root():
    """Welcome endpoint"""
    return {
        "message": "Welcome to the Rejection API!",
        "endpoint": "/rejection - Get a random funny rejection"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)