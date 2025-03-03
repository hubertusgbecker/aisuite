# AISuite

This is my fork of the original AISuite repository. Everything remains the same except that a new **GitHub Provider** has been added to enable GPT-4 access via a GitHub Copilot subscription.

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/hubertusgbecker/aisuite.git
cd aisuite
pip install -e .

## Usage

Use the new GitHub Provider as follows:

```python
from aisuite.providers.github_provider import GitHubProvider
from aisuite.framework.message import Message

provider = GitHubProvider()
prompt = {"content": "Hello, what is the capital of France?", "role": "user"}
response = provider.chat_completions_create("gpt-4", [prompt])
print(response.choices[0].message.content)


## License

aisuite is released under the MIT License. You are free to use, modify, and distribute the code for both commercial and non-commercial purposes.

## Contributing

If you would like to contribute, please read our [Contributing Guide](https://github.com/andrewyng/aisuite/blob/main/CONTRIBUTING.md) and join our [Discord](https://discord.gg/T6Nvn8ExSb) server!
