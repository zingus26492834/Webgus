Debug is turned on because turning it off disables images and gifs

Website Login (also superuser):
	user: L
	email: L@bananas.com
	password: bananas
(you may already be logged in, to log out go to "http://127.0.0.1:8000/admin/", log out should be in the top right)


To open virtual environment:
	1. open vz.bat
	- while in virtual env in "\myzingus\Zingus" type "zingus" to run server

To run website:
	1. open runzingus.bat

Troubleshooting:
	1. in "myzingus" edit "pyvenv.cfg"
	2. change user in filepath to your user
	3. change python version to your python version
	4. in filepath change "Python.3.9_qbz5n2kfra8p0" to your python version (delete the gibberish at the end)

	- I use python 3.9.13 so installing that version might help
	- When inside the virtual environment and in "C:\Users\(user)\Desktop\Webgus\myzingus\Zingus", write "fix" in command prompt, it should download/redownload dependencies if they do not work (using "pip uninstall ____" before "fix" may help)
