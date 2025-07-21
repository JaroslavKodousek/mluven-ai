import json
import websocket

def call_openai(openai_api_key: str):
    url = "wss://api.openai.com/v1/realtime?model=gpt-4o-realtime-preview-2024-12-17"
    headers = [
        "Authorization: Bearer " + openai_api_key,
        "OpenAI-Beta: realtime=v1"
    ]

    def on_open(ws):
        print("Connected to OpenAI realtime server.")

    def on_message(ws, message):
        data = json.loads(message)
        print("Received event:", json.dumps(data, indent=2))

    ws = websocket.WebSocketApp(
        url,
        header=headers,
        on_open=on_open,
        on_message=on_message
    )

    ws.run_forever()
