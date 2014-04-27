xbmc_voice
==========

A script for adding voice control functionality for XBMC via an Android device. Insprired by a similar script for plex written by a Reddit user (http://www.reddit.com/r/cordcutters/comments/23kn7c/how_to_plex_voice_commands/).


Requirements
============
* An Android device with a microphone and wifi.
* Tasker for Android (https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm)
* AutoVoice for Android, Pro Unlocked (https://play.google.com/store/apps/details?id=com.joaomgcd.autovoice)
* SL4A installed with the Python 2.3 Interpreter


Setup
=====
* Copy the xbmc_voice.py script to your device, updating the IP and Port to match your setup.
* Ensure you have both Tasker and AutoVoice installed on your device.
* Open Tasker and create a new Profile:
  * Go to the 'Profiles' tab. 
  * Click on the + on the bottom bar.
  * Select 'State'
  * Click on 'Plugin' -> 'AutoVoice Recognized'
  * Click on the pencil icon.
  * Check 'Event Behavior'
  * Click on 'Command Filter' and set a one word command word that will be used to start all commands.
    * You can set multiple one word commands, I use "xbmc|x_b_m_c" 
  * Check 'Use Regex'
  * Set 'Command Id' to 'XBMC'
  * Click the check mark at the upper right to save.
  * Click on the Tasker logo at the upper left.
  * Click on 'New Task'
  * Name the tasl 'xbmc voice'
  * Click the + on the bottome bar
  * Click on Script->Run SL4A Script
  * Click on the magnifying glass and select 'xbmc_voice.py'
  * Click on the tags next to 'Pass Variables'
  * Select 'AutoVoice Recognized: First recognized Command (%avcomm)'
  * Click the Tasker logo in the top corner.
  * The task is all set, now you just need to add the 'Recognize' widget to a home screen (or enable continuous listening) and start saying commands!


Commands
========
Currently the script supports:
* Watch Movie <Movie Title> (Plays the specified movie)
* Watch Latest <Television Series> (Plays that last episode you have of a specific television series)
* Watch Next <Television Series>  (Plays the earliest episode of a series that you have not yet watched)
* Watch Season <Season #> Episode <Episode #> of <Television Series> (Plays a specific episode)
* Pause/Play/Stop (Controls video playback)
* Refresh (Refreshes the video library)


Comming Soon
============
* Play random episode of a tv series. (unwatched or watched)
* Play a random movie. (unwatched or watched)
* Volume controls
* Navigation controls
