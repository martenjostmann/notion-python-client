Quick Start
===========

1. Authentication Setup: To use NPC, you need to create an integration in your Notion workspace and obtain an API token. Follow our authentication guide to set this up.

2. Import NPC: Import the library into your Python script:

.. code-block:: python

    from notion_python_client import NPC


1. Create a Notion Client: Initialize a Notion client with your API token:

.. code-block:: python

    client = NPC("YOUR_API_TOKEN")


1. Interact with Notion: You're ready to start using NPC to interact with Notion. Here's an example of creating a new page:

.. code-block:: python

    pages = client.database_handler.get_pages("YOUR_DATABASE_ID")
