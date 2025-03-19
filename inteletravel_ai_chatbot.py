from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to handle AI responses
def get_ai_response(user_message):
    responses = {
        "hello": "Hi! Welcome to InteleTravel AI. How can I assist you today?",
        "recommend": "I can help with travel recommendations! What type of trip are you looking for? (budget, luxury, adventure, beach, family)",
        "budget": "For budget-friendly trips, I recommend Thailand, Mexico, and Portugal.",
        "luxury": "For luxury travel, consider Dubai, Santorini, or the Maldives.",
        "beach": "For a beach getaway, I suggest Hawaii, Bali, or the Bahamas.",
        "training": "To get certified as an InteleTravel agent, complete the online training module and pass the certification quiz.",
        "commission": "Commissions vary by supplier, typically ranging from 10% to 16%. Check your agent portal for details.",
        "social media post": "Here's a sample post: '🌴 Dreaming of paradise? Book your tropical getaway today! #TravelDeals #LuxuryEscape'",
        "email campaign": "Subject: 'Exclusive Travel Deals Inside!' Body: 'Hi [Name], I have an amazing vacation offer for you... Contact me for details!'",
        "follow up": "I'll remind you to follow up with this lead in 3 days. Would you like me to schedule an email?"
    }
    return responses.get(user_message.lower(), "I'm here to help! Ask me about travel, bookings, commissions, or marketing.")

# API Route for chatbot messages
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    response = get_ai_response(user_message)
    return jsonify({"response": response})

# API Route for fetching travel prices
@app.route("/fetch_prices", methods=["GET"])
def fetch_prices():
    sample_prices = {
        "flights": {"NYC to Miami": "$199", "LA to Paris": "$599"},
        "hotels": {"Miami Beach Resort": "$150/night", "Paris Luxury Suite": "$350/night"},
        "car_rentals": {"Compact Car": "$40/day", "SUV": "$75/day"}
    }
    return jsonify(sample_prices)

# Ensure the app runs on the correct host and port
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

