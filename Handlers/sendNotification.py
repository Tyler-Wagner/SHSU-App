from plyer import notification
from Handlers.dbHandle import importUserSettings as getUser

def sendnotification(title, message):
    userSettings = getUser('notifications')
    print("Settings: ", userSettings)
    if userSettings:
        notification.notify(
            title=title,
            message=message,
            timeout=10  # Display duration in seconds
        )
    else:
        pass