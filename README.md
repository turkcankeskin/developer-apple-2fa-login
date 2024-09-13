# Environment

+ MacOs
+ Google Chrome
+ chromedriver
+ python3

Why is there a need for such a thing? It is a Selenium Python script that can be used in tools like Fastlane and can log in to Developer Apple itself. It was created to be used before fastlane in CI environments like Jenkins.

It can work on MacOs because with the 'get-2fa.sh' script, you can obtain the 6-digit security code of the developer apple account logged in on MacOs.

You can use the myacinfo value here in places like $FASTLANE_SESSION. 

https://github.com/fastlane/fastlane/discussions/22186