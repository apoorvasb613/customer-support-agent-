import pytest
from fastapi.testclient import TestClient
from app.ui.tester import app

client = TestClient(app)

TEST_CASES = [
    {
        "question": "what is refund policy",
        "expected_keywords": ["30 days"]
    },
    {
        "question": "where is my order 101",
        "expected_keywords": ["shipped"]
    },
    {
        "question": "hello",
        "expected_keywords": ["assist"]
    }
]


@pytest.mark.parametrize("case", TEST_CASES)
def test_chat_api(case):

    response = client.post(
        "/chat",
        json={"user_query": case["question"]}
    )

    assert response.status_code == 200

    body = response.json()
    text = str(body).lower()

    for keyword in case["expected_keywords"]:
        assert keyword.lower() in text