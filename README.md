# automation_with_python_and_selenium
Execute automated tests on a login web page 


Sauce Labs cloud based framework allows QA teams to perform both manual and automated tests on a variety of operating systems and browsers combinations. 
As it is a cloud based platform, it does not require a large storage on client machine. The actual tests are deployed on the cloud.
The Sauce Labs SaaS allows you to set up a complete testing environment in only few seconds with all the necessary configurations (OS, browser type, browser version, etc.)
Sauce Labs gives you the opportunity to execute a large scale of tests simultaneously. Documentation and reporting are made easy to use and maintain, thanks to the logging mechanism. It provides cool stuff like screen shots and a video of execution which includes all test steps that are being executed through the selenium script. 
In the given task I was asked to perform tests on a web contact page. I’ve performed the following steps in order to complete the mission:
I examined the web page manually using my browser in order to figure out what should be included in the script. I understood what are the required actions a user should make in order complete the desired transaction. 
I noticed that a successful user submission ends with a greeting “nice to meet you”. Looking into to DOM I figured out some dynamic changes in the page html source when this message is presented. The display attribute of the class element “nice-to-meet-you” is changed from ‘None’ to ‘Block’. This fact is the validation key of the scenario and is used in my script to determine failure of success of a test.
I also noticed a few bugs in this webpage indicating no validation test were done, for example:
Submission “successful” when abnormal phone number inserted such as a phone number containing letters or a one which contains wrong number of digits.
Submission “successful” when more than one “@” inserted in the email field.
And more similar bugs.
After observing the different possible results, I decided to start the automated testing. Using Selenium IDE I have recorded a simple “base script” which I enhanced later to support:
Communication with Sauce Labs framework.
Expected results validation matching the given task data.
Test reports to SaaS.
Finally I have ended up with two separate scripts which are testing the basic mechanism of the contact-us page: For positive testing I executed a script which uses valid values in all fields, and after submission a “nice to meet you” message is shown.  For the negative test I executed a script which contains invalid email address (has no “@”).
I am aware that I could use an external set of both valid and invalid parameters combinations and their expected test results, to increase the test coverage significantly. I chose two easy samples to make the point clear for this task.
Two Python script I used for this analysis are attached “formTestPos.py” and “formTestNeg.py”.
Negative test link (using “formTestNeg.py”):  https://saucelabs.com/beta/tests/02eb55701f5d4aee9e546d6942ca7468/commands
Positive test link(using “formTestPos.py”): https://saucelabs.com/beta/tests/aa884788a60a4da5bfb646853d3ef2cf/commands



 
