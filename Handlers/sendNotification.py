#MIC IMPORTS
from plyer import notification
#HANDLER IMPORTS
from Handlers.dbHandle import importUserSettings as getUser

def sendnotification(title, message):
    userSettings = getUser('notifications')
    if userSettings:
        notification.notify(
            title=title,
            message=message+"\nPLEASE VIEW THE ALERTS PAGE!!",
            timeout=10  # Display duration in seconds
        )
    else:
        pass