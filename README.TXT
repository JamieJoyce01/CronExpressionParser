To use this program you will require Python3 which can be found here: https://www.python.org/downloads/

In your commandline you will want to type the location of python3, followed by the path to the CronExpressionParser.py (Not CronExpression.py). 
Followed by your arguments for the Cron times which should be wrapped in double quotes so that it is only one commandline argument. The program will
reject it otherwise!

E.G: /usr/bin/python3 /Users/jamiejoyce/Documents/Projects/cronExpressionParser/cronExpressionParser.py "*/15 0 1,15 * 4-5 /usr/bin/find"

You may notice that my CronParser ranges from 0-11 in some cases (Such as years) whereas the example ranges from 1-12. I did this based on rules I have read online.


Steps aside, I was unable to do unit tests due to time constraints however I promise it works!

You are able to use the: * , / - operators which are all supported. NOTE program will crash if a letter is included with any of these operators as this is a edgecase
I didnt have enough time to solve. 

Standalone numbers or Asterisks with a letter will give an intended error, to my knowledge thats the only edgecase that causes a crash.