import json

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        expression = body.get("expression", "")

        # Evaluate safely
        result = eval(expression, {"__builtins__": {}}, {})

        return {
            "statusCode": 200,
            "headers": { "Content-Type": "application/json" },
            "body": json.dumps({ "result": result })
        }

    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({ "error": str(e) })
        }
