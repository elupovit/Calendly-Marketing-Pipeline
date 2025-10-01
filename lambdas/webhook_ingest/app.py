import json

def handler(event, _context):
    return {
        "statusCode": 200,
        "body": json.dumps({"ok": True, "event": event})
    }
