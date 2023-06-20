class CronExpression:
    # Couldve used a global variable with perhaps a parent class but I felt 
    # it was unneeded for a script of this size.
    NUMBER_OF_ARGS: int = 6

    # Min and max time bounds of each timeField.
    TIME_BOUNDS: list[tuple[int,int]] = [
        (0, 59), # Minutes
        (0, 23), # Hours
        (1, 31), # Days of Month
        (0, 11), # Months
        (1, 7),  # Days of Week
        ]
    

    def listTimes(self, times: list[str], lowerBound: int, upperBound: int):
        # Check if the user entered the times in the correct order when using a ','. 
        # If so we then check they confine within the bounds. Then return as no change
        # is needed.

        if(sorted(times, key=int) != times):
            self.terminate()
        self.checkBounds(int(times[0]), lowerBound, int(times[-1]), upperBound)
        return times
    
    def rangeTimes(self, times: list[str], lowerBound: int, upperBound: int):
        # We check the length and bounds to make sure they are correct. We then
        # range the two numbers and return all the numbers inbetween.
 
        startTime = int(times[0])
        endTime = int(times[1])
        self.checkLengthAndBounds(times, startTime, lowerBound, endTime, upperBound)
        newTimes = []
        for i in range(startTime, endTime+1):
            newTimes.append(str(i))
        return newTimes

    def addTimes(self, times: list[str], lowerBound: int, upperBound: int):
        # We do our checks again and then increment the time by the specified amount, either from
        # the lowerbound or whatever the user specifies.

        startTime = int(times[0]) if times[0] != "*" else lowerBound
        incrementTime = int(times[1])
        self.checkLengthAndBounds(times, startTime, lowerBound, incrementTime, upperBound)
        newTimes = []
        newTimes.append(str(startTime))
        currentTime = startTime
        while(currentTime+incrementTime <= upperBound):
            newTimes.append(str(currentTime+incrementTime))
            currentTime += incrementTime
        return newTimes
    
    def checkLengthAndBounds(self, arr, startTime, lowerBound, endTime, upperBound):
        if(len(arr) != 2):
            self.terminate()
        self.checkBounds(startTime, lowerBound, endTime, upperBound)

    def checkBounds(self, startTime, lowerBound, endTime, upperBound):
        # Separate bounds function for the listTimes method where we dont check the length.
        if(startTime < lowerBound or endTime > upperBound):
            self.terminate()
    
    # Dictionary with divider to functions to call the appropriate method.
    dividerFuncs = {
        ',': listTimes,
        '-': rangeTimes,
        '/': addTimes,
    }
    def __init__(self, timeFields: list[str], terminate) -> None:
        self.terminate = terminate
        self.times = []
        self.timeFields = timeFields

    def processEntries(self):
        # Lower and upper bounds provided with the field so we know the contraints of the timefield.
        for field, (lowerTimeBound, upperTimeBound) in zip(self.timeFields, self.TIME_BOUNDS):
            if(field == "*"):
                # Add all times to list if asterisk.
                self.times.append(self.getAllTimeBounds(lowerTimeBound, upperTimeBound))
                continue
            
            dividerPresent = False
            for divider in self.dividerFuncs.keys():
                if(divider in field):
                    dividerPresent = True
                    # Function call to appropriate function.
                    # Ran out of time but here is an Edgecase where we dont check for a letter and program crashes.
                    timeRanges = self.dividerFuncs[divider](self, field.split(divider), lowerTimeBound, upperTimeBound)
                    self.times.append(timeRanges)
            # If not an asterisk, letter and no divider present it must be a number.
            if not dividerPresent:
                if not field.isnumeric():
                    self.terminate()

                self.times.append([field])
        return self.times

    def getAllTimeBounds(self, lowerBound, upperBound):
        times = []
        # (Inclusive, Exclusive)
        for i in range(lowerBound, upperBound+1):
            times.append(str(i))
        return times
