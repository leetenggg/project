# Random Password Generator

#### Video Demo: <URL HERE>

#### Description:

My project is a random password generator. It is able to create random strong passwords for the user and store passwords with their respective websites/accounts. This is done using HTML, CSS, Javascript, Flask (Python) and SQLite.

The first page is a log in/register page. The user will be prompted to create a username and a password for this account. This will be the only password that they have to remember. After they click log in/register, they will be brought to the home page where users can create strong passwords to meet the specific requirements of each account.

Firstly, users will specify the password length required to create their account (minimum and maximum length). There is a check in place to ensure that valid values are selected (eg. maximum should be larger than minimum).

Secondly, users will specify if they want special characters, numbers and capital letters in their password. Having these in the password will make it way stronger, therefore, these options are selected by default. However, some legacy websites/apps might not be able to process certain special characters, hence the users might want to opt out if using those websites.

Thirdly, users will click on the "Generate" button and a random password will be created for them under "Your new password".

- The length of the password will be randomised between the minimum and maximum length.
- The order of characters is (special character)(english word)(number)-(special character)(english word)(number)-...
  - eg. $Fried7-!Sam
- Random English words are generated instead of random letters to make it easier for the user to remember if they wish to do so.

They can then click on the “Copy to clipboard” button to copy the password.

Fourthly, if users wish to store the generated password along with the website on this webpage, they can do so by entering the website URL in the following box. Then, they can simply click on "Save Password" and it will be stored for them.

On the secound page in the navigation bar we have "Saved passwords" which essentially shows all the passwords and their respective websites stored by the current user. From here, they have the option to delete the password from this webpage.

The last option on the navigation bar is "Log out" which logs the user out of their account.
