import sys

from CronExpression import CronExpression

class CronExpressionparser:
    # Use of Constant incase further times are added e.g seconds, years.
    NUMBER_OF_ARGS: int = 6
    # Distance in UI between titles and values.
    SPACE_AFTER_FIELDS: int = 14

    TIME_FIELDS: list[str] = [
        "minute",
        "hour",
        "day of month",
        "month",
        "day of week",
        "command",
    ]

    def __init__(self) -> None:
        self.sysArgs: list[str] = self.processCmdArgs()
        # Sending through all the args except the command path to avoid the hassle.
        self.cronExpression: CronExpression = CronExpression(self.sysArgs[:-1], self.terminateProgram)
        self.times: list[str] = self.cronExpression.processEntries()

    def outputUi(self) -> None:
        # Here we append the command path on the end so that we dont have to write logic to ignore it in the CronExpression class.
        self.times.append(self.sysArgs[-1])
        for timeField, times in zip(self.TIME_FIELDS, self.times):
            headingWithSpace = timeField + " "*(self.SPACE_AFTER_FIELDS - len(timeField))
            if(timeField == "command"):
                print(headingWithSpace + times)
                break
            print(headingWithSpace + " ".join(times))

    def processCmdArgs(self) -> list[str]:
        """
        Fetch the command line arguments, verify there are only 2 (including the path of the script).
        Split the ones we care about into a list to pass to CronExpression.
        """
        sysArgs = self.getCmdArgs()
        self.checkValidArgsLength(sysArgs, 2)
        return self.splitArgs(sysArgs)


    def splitArgs(self, sysArgs) -> list[str]:
        args = sysArgs[1].split()
        self.checkValidArgsLength(args, self.NUMBER_OF_ARGS)
        return args

    def checkValidArgsLength(self, args: list[str], length: int) -> None:
        """
        Checks the arguments provided against the expected length also provided. 
        If these dont match up we terminate.
        """
        if(len(args) == length):
            return
        else:
            self.terminateProgram()

    def terminateProgram(self) -> None:
        """
        Prints generic output to console and terminates the program.
        """
        print('Please enter a valid Cron Expression as an argument. Cron Expression should be encolsed in " " as one argument.')
        sys.exit()

    def getCmdArgs(self) -> list[str]:
        return sys.argv

    @staticmethod
    def createCronParserFactory() -> object:
        return CronExpressionparser()
    

cronExpressionParser: CronExpressionparser = CronExpressionparser.createCronParserFactory()
cronExpressionParser.outputUi()