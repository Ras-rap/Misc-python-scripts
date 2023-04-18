#The Discord webhook spammer executed by main.py in this folder

from discordwebhook import Discord

content = input("Enter the content of the webhook: ")
hook = input("Enter the webhook url: ")
avatar = input("Enter the avatar url or 'Default' to use the default: ")
name = input("Enter the name to use in the webhook or 'Default' to use the default: ")

if name == "Default":
            name = "Webhook Spammer"

if avatar == "Default":
        avatar = "https://preview.redd.it/bcyq3rjk2w071.png?width=1080&crop=smart&auto=webp&v=enabled&s=2c75012efb71ebfb18462cdb3ab7974eb68d10f7"

discord = Discord(url=hook)
ammount =  int(input("Enter how many times to send the message: "))
while ammount > 0:
        discord.post(
        username=name,
        avatar_url=avatar,
        embeds=[
            {
                "username": name,
                "author": {
                "name": name,
                "icon_url": avatar,
                },
                "description" : f"",
                "color" : 16711680,
                "fields": [
                    {"name": content, "value": f"```{content}```", "inline": False},
                    

                ],
                "thumbnail": {"url": avatar}


            },
            
            
        ],
        ),
        ammount -= 1


