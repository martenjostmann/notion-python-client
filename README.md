# Notion Python Client (NPC)

![pytthon-versions](https://img.shields.io/badge/python-3.9%20|%203.10%20|%203.11%20|%203.12--dev-blue) [![codecov](https://codecov.io/gh/martenjostmann/notion-python-client/graph/badge.svg?token=RTV5XNU7SR)](https://codecov.io/gh/martenjostmann/notion-python-client)
![example workflow](https://github.com/martenjostmann/notion-python-client/actions/workflows/test.yml/badge.svg)

## Introduction

NPC (Notion Python Client) is a Python library that simplifies interactions with the Notion API. With this library, you can effortlessly integrate your Python applications with Notion, allowing you to create, retrieve, update, and manage Notion pages, databases, and more, all within your Python code.

## Features

- **Simple and Intuitive:** NPC provides a user-friendly interface to interact with the Notion API. Whether you are a seasoned developer or new to Notion, you'll find it easy to get started.

- **Diverse Functionality:** You can perform a wide range of actions using NPC, such as creating new pages, updating page content, retrieving database entries, and much more.

- **Authentication:** NPC takes care of the authentication process, allowing you to focus on your application logic without worrying about the intricacies of the API's authentication flow.

- **Customization:** The library is designed to be flexible, making it easy to adapt to your specific project requirements. You can use it to integrate Notion with your websites, productivity tools, or automate your Notion workspace.

## Installation

You can install NPC using pip:

```bash
pip install notion-python-client
```

## Getting Started

1. Authentication Setup: To use NPC, you need to create an integration in your Notion workspace and obtain an API token. Follow our authentication guide to set this up.

2. Import NPC: Import the library into your Python script:

```python
from notion_python_client import NPC
```

3. Create a Notion Client: Initialize a Notion client with your API token:

```python
client = NPC("YOUR_API_TOKEN")
```

4. Interact with Notion: You're ready to start using NPC to interact with Notion. Here's an example of creating a new page:

```python
pages = client.database_handler.get_pages("YOUR_DATABASE_ID")
```

## Documentation

For detailed documentation, please visit the [NPC Documentation](https://notion-python-client.readthedocs.io).

## Examples

Explore our examples directory for sample Python scripts that showcase various use cases of NPC. (Coming Soon)

<br>
<br>

---

<br>
<br>
Thank you for choosing NPC for your Notion integration needs! We look forward to seeing what you build with it. Happy coding!
