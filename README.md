Author : Adam Donaghy
Company : Omni Market Tide

This is a django project for the management of endpoints for the applications and services that OMT require

Supported Functionality:
	* Subscription to stock events
		* When the criteria is filled the cron job triggers an action
		* Unsubscription is also supported

Outstanding:
	* If a user deletes the app will they still get their subscriptions?
	

Code Style Guide:
	* Use CammelCase as much as possible
	* Imports are both alphabetical and in the other
		* Django native (eg django.http )
		* Third party packages (eg rest_framework)
		* Custom classes (eg .models )

Commet Guide:
	* Classes need basic description, author and date
	* Post, Get ect.. need to be documented with a short description. This is for app developers so they need to know what they're getting/ expecting
	* Anything interesting in the code needs to have inline comments. 