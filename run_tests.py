import requests
from tests.test_cases import TEST_CASES
from app.evaluations.evaluator import evaluate_response

API_URL = "http://127.0.0.1:8000/chat"

results = []

for test in TEST_CASES:

    payload = {
        "user_query": test["question"]
    }

    response = requests.post(API_URL, json=payload)

    data = response.json()

    ai_response = data["response"]

    evaluation = evaluate_response(
        ai_response,
        test["expected_keywords"]
    )

    result = {
        "question": test["question"],
        "response": ai_response,
        "score": evaluation["score"],
        "passed": evaluation["passed"]
    }

    results.append(result)

for r in results:
    print("\n==============================")
    print("QUESTION:", r["question"])
    print("RESPONSE:", r["response"])
    print("SCORE:", r["score"])
    print("PASSED:", r["passed"])
