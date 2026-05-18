def evaluate_response(response, expected_keywords):
    matched = 0

    for keyword in expected_keywords:
        if keyword.lower() in response.lower():
            matched += 1

    score = matched / len(expected_keywords)

    return {
        "score": score,
        "passed": score == 1.0
    }
