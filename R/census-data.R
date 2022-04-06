#' Census Demographic Information
#'
#' This data has information on the top ten populated counties in Arizona. There
#' are estimates for different demographic information on the population of
#' Arizona as collected from 2010 to 2019 in American Community Surveys data
#' profiles.
#'
#' @format A data frame with 100 observations with 86 columns.
#' \describe{
#'   \item{Year}{the year of the given information}
#'   \item{County}{the county of Arizona the value came from}
#'   \item{County.Year}{the combination of the county and year column}
#'   \item{Total.Population}{the total population of the location}
#'   \item{Male.Total.Population}{the total population of males}
#'   \item{Female.Total.Population}{the total population of females}
#'   \item{Sex.Ratio}{males per 100 females}
#'   \item{Under.5.Population}{the total population of under 5 years old}
#'   \item{5.to.9.Population}{the total population of 5 to 9 years of age}
#'   \item{10.to.14.Population}{the total population of 10 to 14 years of age}
#'   \item{15.to.19.Population}{the total population of 15 to 19 years of age}
#'   \item{20.to.24.Population}{the total population of 20 to 24 years of age}
#'   \item{25.to.34.Population}{the total population of 25 to 34 years of age}
#'   \item{35.to.44.Population}{the total population of 35 to 44 years of age}
#'   \item{45.to.54.Population}{the total population of 45 to 54 years of age}
#'   \item{55.to.59.Population}{the total population of 55 to 59 years of age}
#'   \item{60.to.64.Population}{the total population of 60 to 64 years of age}
#'   \item{65.to.74.Population}{the total population of 65 to 74 years of age}
#'   \item{75.to.84.Population}{the total population of 75 to 84 years of age}
#'   \item{Over.85.Population}{the total population of over 85 years old}
#'   \item{Median.Age}{the median age for the county at the year}
#'   \item{Under.18.Population}{the total population under 18 years of age}
#'   \item{Over.16.Population}{the total population of over 16 years of age}
#'   \item{Over.18.Population}{the total population of over 18 years of age}
#'   \item{Over.21.Population}{the total population of over 21 years of age}
#'   \item{Over.62.Population}{the total population of over 62 years of age}
#'   \item{Over.65.Population}{the total population of over 65 years of age}
#'   \item{Over.18}{the total population over 18 years of age}
#'   \item{Over.18.Male}{the total population males over 18 years of age}
#'   \item{Over.18.Female}{the total population females over 18 years of age}
#'   \item{Over.18.Sex.Ratio}{males per 100 females over 18 years of age}
#'   \item{Over.65.Male}{the total population of males over 65 years of age}
#'   \item{Over.65.Female}{the total population of females over 65 years of age}
#'   \item{Over.65.Sex.Ration}{males per 100 females over 65 years of age}
#'   \item{Male.Total.Population}{the total population of males}
#'   \item{One.Race.Total.Population}{the total population of people under one race}
#'   \item{Two.Or.More.Races.Population}{the total population of people under two or more races}
#'   \item{White}{the total population of white people}
#'   \item{Black.Or.African.American}{the total population of black or african american people}
#'   \item{AI.and.AN}{the total population of american indian or alaskan native people}
#'   \item{Cherokee.TG}{the total population of Cherokee tribal grouping}
#'   \item{Chippewa.TG}{the total population of Chippewa tribal grouping}
#'   \item{Navajo.TG}{the total population of Navajo tribal grouping}
#'   \item{Sioux.TG}{the total population of Sioux tribal grouping}
#'   \item{Asian}{the total population of Asian people}
#'   \item{Asian.Indian}{the total population of Asian Indian people}
#'   \item{Chinese}{the total population of Chinese people}
#'   \item{Filipino}{the total population of Filipino people}
#'   \item{Japanese}{the total population of Japanese people}
#'   \item{Korean}{the total population of Korean people}
#'   \item{Vietnamese}{the total population of Vietnamese people}
#'   \item{Other.Asian}{the total population of people other than Asian}
#'   \item{NH.and.OPI}{the total population of Native Hawaiian and Other Pacific Islander people}
#'   \item{NH}{the total population of Native Hawaiians}
#'   \item{Guamanian.or.Chamorro}{the total population of Guamanian or Chamorro people}
#'   \item{Samoan}{the total population of Samoan people}
#'   \item{OPI}{the total population of other Pacific Islander people}
#'   \item{Some.Other.Race}{the total population of some other race}
#'   \item{White.and.Black.or.AA}{the total population of White and Black or African American people}
#'   \item{White.and.AI.and.AN}{the total population of White and American Indian and Alaskan Native people}
#'   \item{White.and.Asian}{the total population of White and Asian people}
#'   \item{Black.or.AA.and.AI.and.AN}{the total population of Black or African American and American Indian and Alaskan Native people}
#'   \item{Race.Alone.White}{the total population of all White people}
#'   \item{Race.Alone.Black.or.AA}{the total population of all Black or African American people}
#'   \item{Race.Alone.AI.and.AN}{the total population of all American Indian and Alaskan Native people}
#'   \item{Race.Alone.Asian}{the total population of all Asian people}
#'   \item{Race.Alone.NH.and.OPI}{the total population of all Native Hawaiians and Other Pacific Islander people}
#'   \item{Race.Alone.Other}{the total population of all other races}
#'   \item{HL}{the total population of Hispanic or Latino people}
#'   \item{Mexican}{the total population of Mexican people}
#'   \item{Puerto.Rico}{the total population of people Puerto Rican people}
#'   \item{Cuban}{the total population of Cuban people}
#'   \item{OH.or.LP}{the total population of other Hispanic or Latino people}
#'   \item{Not.Hispanic.or.Latino}{the total population of people that not Hispanic or Latino}
#'   \item{NHL.White}{the total population of Non-Hispanic White people}
#'   \item{NHL.Black.or.AA}{the total population of Non-Hispanic Black or African American people}
#'   \item{NHL.AI.and.AN}{the total population of Non-Hispanic American Indian and Alaskan Native people}
#'   \item{NHL.Asian.Alone}{the total population of Non-Hispanic Asian people}
#'   \item{NHL.NH.and.OPI}{the total population of Non-Hispanic Native Hawaiian and Other Pacific Islander people}
#'   \item{NHL.Other}{the total population of Non-Hispanic Other Races}
#'   \item{NHL.Two.or.More.Races}{the total population of Non-Hispanic of two or more races}
#'   \item{NHL.Two.Races.Including}{the total population of Non-Hispanic of two or more races including other races}
#'   \item{NHL.Two.Races.Excluding}{the total population of Non-Hispanic of two or more races excluding other races, and three or more races}
#'   \item{HL.Total.Housing.Units}{total housing units of Hispanic people}
#'   \item{Citizens.Over.18}{the total population of citizens over 18 years of age}
#'   \item{Male.Citizens.Over.18}{the total population of male citizens over 18 years of age}
#'   \item{Female.Citizens.Over.18}{the total population of female citizens over 18 years of age}
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
censusData$County <- tolower(censusData$County)
censusData$County <- as.factor(censusData$County)
censusData$Estimate <- as.numeric(gsub(",","",censusData$Estimate))
censusData$County.Year <- paste(censusData$County, censusData$Year)
censusData <- censusData %>% select(-index)
censusData <- pivot_wider(censusData, names_from = Labels, values_from = Estimate)
censusData <- censusData %>% select(-Over.65) %>%
  select(-Race.Total.Population) %>% select(-One.Race) %>%
  select(-Two.Or.More.Races) %>% select(-Race.Alone.Population) %>%
  select(-HL.Total.Population)



usethis::use_data(censusData, overwrite=TRUE)


