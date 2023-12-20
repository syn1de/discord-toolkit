import requests

def collect_links(channel_id, headers):
    links = []

    # Discord API URL for fetching messages in a channel
    url = f'https://discord.com/api/v10/channels/{channel_id}/messages'
    params = {'limit': 100}

    while True:
        # Make a GET request to fetch messages
        response = requests.get(url, headers=headers, params=params)
        messages = response.json()

        # Extract links from messages
        for message in messages:
            if 'attachments' in message:
                for attachment in message['attachments']:
                    if 'url' in attachment:
                        links.append(attachment['url'])

            if 'embeds' in message:
                for embed in message['embeds']:
                    if 'image' in embed and 'url' in embed['image']:
                        links.append(embed['image']['url'])

                    if 'video' in embed and 'url' in embed['video']:
                        links.append(embed['video']['url'])

        # Check if there are fewer than 100 messages, indicating the end of messages
        if len(messages) < 100:
            break

        # Update 'before' parameter for the next set of messages
        last_message_id = messages[-1]['id']
        params['before'] = last_message_id

    return links

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print(" " * 20 + "LOL XD" + " " * 20)
    print("=" * 50 + "\n")

    # Get user input for token
    user_token = input("Enter your Discord token: ")

    # Set HTTP headers
    headers = {'Authorization': user_token}

    # Get user input for channel ID
    channel_id = input("Enter the Discord channel ID: ")

    # Collect links from the specified channel
    channel_links = collect_links(channel_id, headers)

    # Write links to a text file
    with open(f'{channel_id}_links.txt', 'w') as f:
        for link in channel_links:
            f.write(link + '\n')

        # Print a completion message
        print('DISRIPPER - BY CYANIDE completed.')
