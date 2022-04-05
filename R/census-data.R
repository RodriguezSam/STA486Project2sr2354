#' Census Demographic Information
#'
#' This data has information on the top ten populated counties in Arizona. There
#' are estimates for different demographic information on the population of
#' Arizona as collected from 2010 to 2019 in American Community Surveys data
#' profiles.
#'
#' @format A data frame with 8850 observations with 5 columns.
#' \describe{
#'   \item{index}{numerical index for full dataframe}
#'   \item{Labels}{the meaning to the value in the estimate column}
#'   \item{Year}{the year of the given information}
#'   \item{County}{the county of Arizona the value came from}
#'   \item{Estimate}{the estimated population value for the given label}
#' }
#' @source \url{https://data.census.gov/cedsci/table}
"censusData"

library(tidyverse)
library(dplyr)
library(usethis)

census19 <- read.csv('docs/census_data_2019.csv')
census18 <- read.csv('docs/census_data_2018.csv')
census17 <- read.csv('docs/census_data_2017.csv')
census16 <- read.csv('docs/census_data_2016.csv')
census15 <- read.csv('docs/census_data_2015.csv')
census14 <- read.csv('docs/census_data_2014.csv')
census13 <- read.csv('docs/census_data_2013.csv')
census12 <- read.csv('docs/census_data_2012.csv')
census11 <- read.csv('docs/census_data_2011.csv')
census10 <- read.csv('docs/census_data_2010.csv')

labelsNew <- c("SEX.AND.AGE", "Total.Population", "Male.Total.Population",
               "Female.Total.Population", "Sex.Ratio", "Under.5.Population",
               "5.to.9.Population", "10.to.14.Population", "15.to.19.Population",
               "20.to.24.Population", "25.to.34.Population",
               "35.to.44.Population", "45.to.54.Population",
               "55.to.59.Population", "60.to.64.Population",
               "65.to.74.Population", "75.to.84.Population",
               "Over.85.Population", "Median.Age", "Under.18.Population",
               "Over.16.Population", "Over.18.Population", "Over.21.Population",
               "Over.62.Population", "Over.65.Population", "Over.18",
               "Over.18.Male", "Over.18.Female", "Over.18.Sex.Ratio",
               "Over.65", "Over.65.Male", "Over.65.Female",
               "Over.65.Sex.Ration", "RACE", "Race.Total.Population",
               "One.Race.Total.Population", "Two.Or.More.Races.Population",
               "One.Race", "White", "Black.Or.African.American", "AI.and.AN",
               "Cherokee.TG", "Chippewa.TG", "Navajo.TG", "Sioux.TG", "Asian",
               "Asian.Indian", "Chinese", "Filipino", "Japanese", "Korean",
               "Vietnamese", "Other.Asian", "NH.and.OPI", "NH",
               "Guamanian.or.Chamorro", "Samoan", "OPI", "Some.Other.Race",
               "Two.Or.More.Races", "White.and.Black.or.AA",
               "White.and.AI.and.AN", "White.and.Asian",
               "Black.or.AA.and.AI.and.AN", "Race.Alone.or.Combination",
               "Race.Alone.Population", "Race.Alone.White",
               "Race.Alone.Black.or.AA", "Race.Alone.AI.and.AN",
               "Race.Alone.Asian", "Race.Alone.NH.and.OPI", "Race.Alone.Other",
               "HISPANIC.OR.LATINO.AND.RACE", "HL.Total.Population",
               "HL", "Mexican", "Puerto.Rico", "Cuban", "OH.or.LP",
               "Not.Hispanic.or.Latino", "NHL.White", "NHL.Black.or.AA",
               "NHL.AI.and.AN", "NHL.Asian.Alone", "NHL.NH.and.OPI",
               "NHL.Other", "NHL.Two.or.More.Races", "NHL.Two.Races.Including",
               "NHL.Two.Races.Excluding", "HL.Total.Housing.Units",
               "CITIZEN.VOTING.AGE.POPULATION", "Citizens.Over.18",
               "Male.Citizen.Over.18", "Female.Citizen.Over.18")
census19$Labels <- labelsNew
census18$Labels <- labelsNew
census17$Labels <- labelsNew
labelsNew <- c("SEX.AND.AGE", "Total.Population", "Male.Total.Population",
               "Female.Total.Population", "Under.5.Population",
               "5.to.9.Population", "10.to.14.Population", "15.to.19.Population",
               "20.to.24.Population", "25.to.34.Population",
               "35.to.44.Population", "45.to.54.Population",
               "55.to.59.Population", "60.to.64.Population",
               "65.to.74.Population", "75.to.84.Population",
               "Over.85.Population", "Median.Age",
               "Over.18.Population", "Over.21.Population",
               "Over.62.Population", "Over.65.Population", "Over.18",
               "Over.18.Male", "Over.18.Female",
               "Over.65", "Over.65.Male", "Over.65.Female",
               "RACE", "Race.Total.Population",
               "One.Race.Total.Population", "Two.Or.More.Races.Population",
               "One.Race", "White", "Black.Or.African.American", "AI.and.AN",
               "Cherokee.TG", "Chippewa.TG", "Navajo.TG", "Sioux.TG", "Asian",
               "Asian.Indian", "Chinese", "Filipino", "Japanese", "Korean",
               "Vietnamese", "Other.Asian", "NH.and.OPI", "NH",
               "Guamanian.or.Chamorro", "Samoan", "OPI", "Some.Other.Race",
               "Two.Or.More.Races", "White.and.Black.or.AA",
               "White.and.AI.and.AN", "White.and.Asian",
               "Black.or.AA.and.AI.and.AN", "Race.Alone.or.Combination",
               "Race.Alone.Population", "Race.Alone.White",
               "Race.Alone.Black.or.AA", "Race.Alone.AI.and.AN",
               "Race.Alone.Asian", "Race.Alone.NH.and.OPI", "Race.Alone.Other",
               "HISPANIC.OR.LATINO.AND.RACE", "HL.Total.Population",
               "HL", "Mexican", "Puerto.Rico", "Cuban", "OH.or.LP",
               "Not.Hispanic.or.Latino", "NHL.White", "NHL.Black.or.AA",
               "NHL.AI.and.AN", "NHL.Asian.Alone", "NHL.NH.and.OPI",
               "NHL.Other", "NHL.Two.or.More.Races", "NHL.Two.Races.Including",
               "NHL.Two.Races.Excluding", "HL.Total.Housing.Units",
               "CITIZEN.VOTING.AGE.POPULATION", "Citizens.Over.18",
               "Male.Citizen.Over.18", "Female.Citizen.Over.18")
census16$Labels <- labelsNew
census15$Labels <- labelsNew
labelsNew <- c("SEX.AND.AGE", "Total.Population", "Male.Total.Population",
               "Female.Total.Population", "Under.5.Population",
               "5.to.9.Population", "10.to.14.Population", "15.to.19.Population",
               "20.to.24.Population", "25.to.34.Population",
               "35.to.44.Population", "45.to.54.Population",
               "55.to.59.Population", "60.to.64.Population",
               "65.to.74.Population", "75.to.84.Population",
               "Over.85.Population", "Median.Age",
               "Over.18.Population", "Over.21.Population",
               "Over.62.Population", "Over.65.Population", "Over.18",
               "Over.18.Male", "Over.18.Female",
               "Over.65", "Over.65.Male", "Over.65.Female",
               "RACE", "Race.Total.Population",
               "One.Race.Total.Population", "Two.Or.More.Races.Population",
               "One.Race", "White", "Black.Or.African.American", "AI.and.AN",
               "Cherokee.TG", "Chippewa.TG", "Navajo.TG", "Sioux.TG", "Asian",
               "Asian.Indian", "Chinese", "Filipino", "Japanese", "Korean",
               "Vietnamese", "Other.Asian", "NH.and.OPI", "NH",
               "Guamanian.or.Chamorro", "Samoan", "OPI", "Some.Other.Race",
               "Two.Or.More.Races", "White.and.Black.or.AA",
               "White.and.AI.and.AN", "White.and.Asian",
               "Black.or.AA.and.AI.and.AN", "Race.Alone.or.Combination",
               "Race.Alone.Population", "Race.Alone.White",
               "Race.Alone.Black.or.AA", "Race.Alone.AI.and.AN",
               "Race.Alone.Asian", "Race.Alone.NH.and.OPI", "Race.Alone.Other",
               "HISPANIC.OR.LATINO.AND.RACE", "HL.Total.Population",
               "HL", "Mexican", "Puerto.Rico", "Cuban", "OH.or.LP",
               "Not.Hispanic.or.Latino", "NHL.White", "NHL.Black.or.AA",
               "NHL.AI.and.AN", "NHL.Asian.Alone", "NHL.NH.and.OPI",
               "NHL.Other", "NHL.Two.or.More.Races", "NHL.Two.Races.Including",
               "NHL.Two.Races.Excluding", "HL.Total.Housing.Units")
census14$Labels <- labelsNew
census13$Labels <- labelsNew
census12$Labels <- labelsNew
census11$Labels <- labelsNew
census10$Labels <- labelsNew
colnames(census19) <- c("index", "Labels", "Apache", "Cochies", "Coconino",
                        "Maricopa", "Mohave", "Navajo", "Pima", "Pinal",
                        "Yavapi", "Yuma", "Year")
colnames(census18) <- c("index", "Labels", "Apache", "Cochies", "Coconino",
                        "Maricopa", "Mohave", "Navajo", "Pima", "Pinal",
                        "Yavapi", "Yuma", "Year")
colnames(census17) <- c("index", "Labels", "Apache", "Cochies", "Coconino",
                        "Maricopa", "Mohave", "Navajo", "Pima", "Pinal",
                        "Yavapi", "Yuma", "Year")
colnames(census16) <- c("index", "Labels", "Apache", "Cochies", "Coconino",
                        "Maricopa", "Mohave", "Navajo", "Pima", "Pinal",
                        "Yavapi", "Yuma", "Year")
colnames(census15) <- c("index", "Labels", "Apache", "Cochies", "Coconino",
                        "Maricopa", "Mohave", "Navajo", "Pima", "Pinal",
                        "Yavapi", "Yuma", "Year")
colnames(census14) <- c("index", "Labels", "Apache", "Cochies", "Coconino",
                        "Maricopa", "Mohave", "Navajo", "Pima", "Pinal",
                        "Yavapi", "Yuma", "Year")
colnames(census13) <- c("index", "Labels", "Apache", "Cochies", "Coconino",
                        "Maricopa", "Mohave", "Navajo", "Pima", "Pinal",
                        "Yavapi", "Yuma", "Year")
colnames(census12) <- c("index", "Labels", "Apache", "Cochies", "Coconino",
                        "Maricopa", "Mohave", "Navajo", "Pima", "Pinal",
                        "Yavapi", "Yuma", "Year")
colnames(census11) <- c("index", "Labels", "Apache", "Cochies", "Coconino",
                        "Maricopa", "Mohave", "Navajo", "Pima", "Pinal",
                        "Yavapi", "Yuma", "Year")
colnames(census10) <- c("index", "Labels", "Apache", "Cochies", "Coconino",
                        "Maricopa", "Mohave", "Navajo", "Pima", "Pinal",
                        "Yavapi", "Yuma", "Year")
census_data <- rbind(census19, census18)
census_data <- rbind(census_data, census17)
census_data <- rbind(census_data, census16)
census_data <- rbind(census_data, census15)
census_data <- rbind(census_data, census14)
census_data <- rbind(census_data, census13)
census_data <- rbind(census_data, census12)
census_data <- rbind(census_data, census11)
census_data <- rbind(census_data, census10)

census <- pivot_longer(census_data, Apache:Yuma, names_to = "County",
                       values_to = "Estimate")
censusData <- census[!(census$Labels == "SEX.AND.AGE" |
                          census$Labels == "RACE" |
                          census$Labels == "Race.Alone.or.Combination" |
                          census$Labels == "HISPANIC.OR.LATINO.AND.RACE" |
                          census$Labels == "CITIZEN.VOTING.AGE.POPULATION"),]
censusData$Labels <- as.factor(censusData$Labels)
censusData$Year <- as.character(censusData$Year)
censusData$Year <- as.Date(censusData$Year, "%Y")
censusData$County <- as.factor(censusData$County)
censusData$Estimate <- as.numeric(gsub(",","",censusData$Estimate))


usethis::use_data(censusData, overwrite=TRUE)


