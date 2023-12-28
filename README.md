# Random Password Generator
#### Video Demo: https://youtu.be/S34ZbYVv7wE?feature=shared
#### Description:

My project is a random password generator. In today's technology driven world, one crucial aspect of digital security is the creation and management of strong, unique passwords for various online accounts. The importance of robust cybersecurity practices cannot be overstated. In order to address this, I have created a comprehensive random password generator which is able to create random strong passwords for the user and store passwords with their respective websites/accounts. This is done by employing the use of HTML, CSS, Javascript, Flask (Python) and SQLite. To make it user-friendly, my project uses simple colours and readable fonts.

Upon accessing the project, the first page is a user-friendly log in/register page that users will be greeted by. Here, the user will be prompted to create a username and a password for this account, which serves as the sole credential for accessing the system. This will be the only password that they have to remember in order to access the system. After they click log in/register, they will be brought to the home page, which is the central hub for generating and saving strong passwords. Here, users have the option to create and customise strong passwords to meet the specific requirements of each online account. The process of crafting different passwords is both intuitive and customisable, allowing users to tailor their own passwords.

Firstly, users will commence by specifying the desired password length needed to create their account, defining both minimum and maximum length. For instance, they can define a password length that is between 8-15 characters. There is a check in place to ensure that valid values are selected (eg. ensuring that maximum should be larger than minimum) in order to ensure that the user's choice is viable.

Secondly, users will specify if they want special characters, numbers and capital letters in their password. Having these in the password will make it way stronger, therefore, these options are selected by default initially for the user. However, as I recognise that some legacy websites/apps might not be able to process certain special characters, and that some users may not desire having too complicated passwords, hence I have included the option for users to opt out of these special characters and numbers when tailoring their password choice. The flexibility to do so will greatly enhance the user's satisfaction with the system.

After having customised the password that they wish to obtain, users will then click on the "Generate" button and wait for the magic to happen. A random password will be created for them under "Your new password"., according to the password style that they have requested. The length of the password will be randomised between the minimum and maximum length. The order of characters is (special character)(english word)(number)-(special character)(english word)(number). Shown below is an example.

eg. $Fried7-!Sam is a password that was generated.

Notably, Random English words are generated instead of random letters to make it easier for the user to remember the passwords, which would otherwise be confusing with just a mix of random letters. In the above example, "Fried" and "Sam" are the random English words that were being generated.

Once the password has been generated, they can then click on the “Copy to clipboard” button to copy the password, allowing users to swiftly integrate the generated password into their desired applications or websites, enhancing accessibility and usability.

Fourthly, if users wish to store the generated password along with the website on this webpage, they can do so by entering the website URL in the following box. Examples of these websites would include Lazada, Shopee, Amazon and many more. These are online shopping platforms that many young people use nowadays. Then, they can simply click on "Save Password" and it will be stored securely for them. This function swiftly transforms the project from a mere password generator to a secure vault.

On the secound page in the navigation bar we have "Saved passwords" which essentially shows all the passwords and their respective websites stored by the current user. From this repository, users have the option to seamlessly delete the password from this webpage should they no longer require it, providing an avenue for ongoing security management.

Recognizing the importance of user privacy, the project also incorporates a "Log out" option in the navigation bar. Upon clicking the button, this feature allows users to exit their accounts securely, closing the digital door and safeguarding sensitive information.

In conclusion, the Random Password Generator project not only empowers users to create and manage strong, unique passwords but also cultivates a secure digital environment. By blending user-friendly interfaces with robust security measures, the project aligns with contemporary cybersecurity needs, ensuring that users can navigate the digital landscape with confidence and resilience against potential threats. Overall, this is a simple project that hopes to be able to solve certain individuals' troubles of creating strong passwords and not being able to remember them.
