class ChatWrapper:
    def generate_response(self, score: int) -> str:
        if score >= 8:
            return f"Wow! You look great. Score: {score}/10."
        elif score >= 5:
            return f"You look good! Score: {score}/10."
        else:
            return f"You're unique in your own way. Score: {score}/10."
