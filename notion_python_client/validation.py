PAGE_SCHEMA = {
    "object": {'type': 'string'},
    "id": {'type': 'string'},
    "created_time": {'type': 'string'},
    "last_edited_time": {'type': 'string'},
    "created_by": {
        "type": "dict",
        "schema": {
            "object": {'type': 'string'},
            "id": {'type': 'string'}
        }
    },
    "last_edited_by": {
        "type": "dict",
        "schema": {
            "object": {'type': 'string'},
            "id": {'type': 'string'}
        }
    },
    "cover": {
        "type": "dict",
        "nullable": True,
        "schema": {
            "type": {'type': 'string'},
            "external": {
                "type": "dict",
                "schema": {
                    "url": {'type': 'string', 'nullable': True}
                }
            }
        }
    },
    "icon": {
        "type": "dict",
        "nullable": True,
        "schema": {
            "type": {'type': 'string'},
            "emoji": {'type': 'string', 'nullable': True}
        }
    },
    "parent": {
        "type": "dict",
        "schema": {
            "type": {'type': 'string'},
            "database_id": {'type': 'string'}
        }
    },
    "archived": {'type': 'boolean'},
    "properties": {
    },
    "url": {'type': 'string'},
    "public_url": {'type': 'string', 'nullable': True}
}
