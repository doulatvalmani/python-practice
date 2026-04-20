def process_api_response(response):
    try:
        if response['status'] == 'success':
            print(f"Campaign successful!")
            print(f"Sent: {response['sent']}")          # fill this
            print(f"Total: {response['total']}")         # fill this
            success_rate = response['sent'] / response['total'] * 100
            print(f"Success rate: {success_rate:.2f}%")
        else:
            print(f"Error: {response['error']}")         # fill this
    except KeyError as e:
        print(f"Missing field: {e}")

# test 1 - success
process_api_response({
    "status": "success",
    "sent": 950,
    "total": 1000
})

print("---")

# test 2 - error
process_api_response({
    "status": "error",
    "error": "Invalid API key!"
})
