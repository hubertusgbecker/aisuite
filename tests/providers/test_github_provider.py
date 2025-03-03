import pytest
from unittest.mock import patch, MagicMock

from aisuite.providers.github_provider import GitHubProvider


@pytest.fixture(autouse=True)
def patch_get_token(monkeypatch):
    """Patch _get_token to set a fake token so no real network call is made."""

    def fake_get_token(self):
        self.token = "fake-token"

    monkeypatch.setattr(GitHubProvider, "_get_token", fake_get_token)


def test_github_provider():
    """High-level test that GitHubProvider initializes and requests chat completions successfully."""

    user_greeting = "Hello!"
    message_history = [{"role": "user", "content": user_greeting}]
    selected_model = "gpt-4"
    chosen_temperature = 0.75
    response_text_content = "mocked-text-response-from-model"

    provider = GitHubProvider()
    provider.token = "fake-token"  # Ensure the token is set
    # Prepare a fake streaming response mimicking the API's output.
    # GitHubProvider expects lines starting with "data: {".
    fake_response_line = (
        f'data: {{"choices": [{{"delta": {{"content": "{response_text_content}"}}}}]}}'
    )
    fake_response_text = fake_response_line + "\n"

    fake_response = MagicMock()
    fake_response.text = fake_response_text
    fake_response.status_code = 200

    with patch("requests.post", return_value=fake_response) as mock_post:
        response = provider.chat_completions_create(
            messages=message_history,
            model=selected_model,
            temperature=chosen_temperature,
        )
        mock_post.assert_called_with(
            "https://api.githubcopilot.com/chat/completions",
            headers={
                "authorization": f"Bearer {provider.token}",
                "Editor-Version": "vscode/1.80.1",
            },
            json={
                "intent": False,
                "model": provider.MODEL,
                "temperature": 0,
                "top_p": 1,
                "n": 1,
                "stream": True,
                "messages": provider.messages,
            },
        )
        assert response.choices[0].message.content == response_text_content
