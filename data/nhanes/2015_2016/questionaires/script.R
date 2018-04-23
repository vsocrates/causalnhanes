library(dplyr)
cleanD = read.csv(file = "CleanD.csv")
cleanSleep = read.csv(file = "cleanSleep.csv")
depScore = cleanD[2]
depScore[2] = cleanD[3]
for(i in 4:11) {depScore[2] = depScore[2] + cleanD[i]}
goodSleep = merge(cleanSleep, depScore, type = "inner")
badSleep = merge(cleanSleep, depScore, type = "inner")
goodSleep = goodSleep %>% filter(SLQ120 < 3)
badSleep = badSleep %>% filter(SLQ120 > 2)
