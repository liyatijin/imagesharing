# imagesharing
Production URL :
Published on AWS
http://35.161.151.226/
Source Code in Github:
https://github.com/liyatijin/imagesharing
Python version: 3.10.2
To run the source code:
From the Command prompt:
virtualenv myprojectenv
source myprojectenv/bin/activate
pip install -r requirements.txt
<root_directory>/imagesharing>python manage.py makemigrations
<root_directory>/imagesharing>python manage.py migrate
<root_directory>/imagesharing>python manage.py runserver
From the browser:
http://35.161.151.226/
You get the homepage where you have the options to
1)	Sign Up
2)	Sign In
Sign Up: you need to fill up a few  details such as user name, password, first name, last name, email id.
Validation done for username and password:
User name should contain only alphabets otherwise when you submit after entering all the details, it directs you to the same sign Up page. 
For password, the first password entered should be same as the second password. If this rule is not followed, it again directs you to the sign up page.
Sign In: After signup, you will be redirected to the Sign In page to enter login details. Ones you login, you are now in page where you can see all the images posted by the users. Images, a short text description and the user who uploaded the image will be displayed for each post. 
Uploading an image:
 After all the post, at the bottom right side of the page, we can see a choose file option where the current user can upload a picture which will be simultaneously added to the top of the page.
Logged in users can see the posts by time. Last uploaded post will be in the beginning.
 You can also add a caption to the picture but that is not mandatory. There is a condition which checks if the caption is given. If it is not given it takes space rather than displaying ‘None’.
API documentation
Endpoint: /Signup
Request Method: POST
Request body:
{
“Username”: string
“fname”: string
“lname”: string
“emailid”: string
“pass1”:string
“pass2”:string
}
Response:
{
“Status”: ”User registered”
“Message”: “Your account has been successfully created”
}
Endpoint: /Signin
Request Method: POST
Request body:
{
“username”: string
“pass1”: password
}
Response:
{
“Status”: ”User registered”
“Message”: “Signin authenticated”
}
Endpoint: /Signout
Request Method: POST
Request body:
{

}
Response:
{
“Status”: ”Signed Out”
“Message”: “Signed Out successfully”
}
Endpoint: /home
Request Method: POST
Request body:
{
“image”: file
“Caption”: string
}
Response:
{
“Status”: ”Success”
“Message”: ”Post is successfully saved”
}
 
