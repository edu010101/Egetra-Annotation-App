def ConvertMillisecondsTime(MilisecondsTime):
        Seconds=int((MilisecondsTime/1000)%60)
        Minutes=int((MilisecondsTime/(1000*60))%60)
        Hours=int((MilisecondsTime/(1000*60*60))%24)

        TimeString = "%02d:%02d:%02d" % (Hours, Minutes, Seconds)

        return TimeString
