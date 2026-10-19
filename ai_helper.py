import os

def explain_with_ai(location, minutes, budget, interests, places):
    if not places:
        return 'No matching places found. Try increasing your budget or available time.'
    try:
        from google import genai
        key = os.getenv('GEMINI_API_KEY')
        if not key:
            return 'Recommendations are based on your preferences. Add a Gemini API key to enable AI explanations.'
        client = genai.Client(api_key=key)
        prompt = (
            'You are a city guide for Astana, Kazakhstan. Use ONLY the places provided below; '
            'do not invent distances, opening hours, prices or travel times. '
            f'User starting area: {location}; free time: {minutes} minutes; '
            f'budget: {budget} KZT; interests: {interests}. '
            f'Places: {places}. Explain briefly why the top places fit. '
            'State that costs are estimates and location proximity is unverified.'
        )
        response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
        return response.text or 'AI returned no explanation.'
    except Exception as exc:
        return f'AI temporarily unavailable ({type(exc).__name__}). Your recommendations still work.'
