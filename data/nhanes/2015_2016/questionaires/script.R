library(dplyr)
cleanD = read.csv(file = "CleanD.csv")
cleanSleep = read.csv(file = "cleanSleep.csv")
depScore = cleanD[2]
depScore[2] = cleanD[3]
for(i in 4:11) {depScore[2] = depScore[2] + cleanD[i]}
goodSleep = merge(cleanSleep, depScore, type = "inner")
badSleep = merge(cleanSleep, depScore, type = "inner")

depSleepy = goodSleep %>% filter(SLQ120 > 2)
hapSleepy = goodSleep %>% filter(SLQ120 > 2)
depRest = goodSleep %>% filter(SLQ120 <3)
hapRest = goodSleep %>% filter(SLQ120 <3)

depSleepy = depSleepy %>% filter(DPQ010 > 9)
hapSleepy = hapSleepy %>% filter(DPQ010 < 9)
depRest = depRest %>% filter(DPQ010 > 9)
hapRest = hapRest %>% filter(DPQ010 < 9)