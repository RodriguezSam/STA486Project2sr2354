#' Hospital Illness information
#'
#' This data has information hospital visits that pertain to the specific illness
#' being measured. There are 9 illness being measured over the different Arizona
#' counties that have data. The years are from 2005 to 2019.
#'
#' @format A data frame with 874 observations with 6 columns.
#' \describe{
#'   \item{County}{the county the data pertains to}
#'   \item{County.Value}{the value per 10,000 population affected by the specific illness in the county}
#'   \item{State.Rate}{the value per 10,000 population of the state of Arizona}
#'   \item{Year}{the year of the given information}
#'   \item{Content.Area}{the given illness}
#'   \item{County.Year}{combination of the county and year}
#' }
#' @source \url{https://gis.azdhs.gov/ephtexplorer/}
"hospitalData"


# library(dplyr)
# library(tidyverse)
library(usethis)

hospitalData <- read.csv('docs/hospital_data.csv')
hospitalData$County <- tolower(hospitalData$County)
hospitalData$County <- as.factor(hospitalData$County)
hospitalData$Value <- as.integer(hospitalData$Value)
hospitalData$Year <- as.character(hospitalData$Year)
hospitalData$Year <- as.Date(hospitalData$Year, "%Y")
hospitalData$Content.Area <- as.factor(hospitalData$Content.Area)
hospitalData$State..Avg. <- as.integer(hospitalData$State..Avg.)
colnames(hospitalData) <- c("index", "County", "County.Value", 'State.Rate',
                            "Year", "Content.Area", "State.Avg")
hospitalData <- hospitalData[!(hospitalData$County == "GILA" |
                         hospitalData$County == "graham" |
                         hospitalData$County == "greenlee" |
                         hospitalData$County == "la paz" |
                           hospitalData$County == "santa cruz"),]
hospitalData <- hospitalData[!(hospitalData$Year == "2005-04-05" |
                                 hospitalData$Year == "2006-04-05" |
                                 hospitalData$Year == "2007-04-05" |
                                 hospitalData$Year == "2008-04-05" |
                                 hospitalData$Year == "2009-04-05"),]
hospitalData$County.Year <- paste(hospitalData$County, hospitalData$Year)
hospitalData <- hospitalData %>% select(-index)
hospitalData <- hospitalData %>%
  mutate(State.Rate=ifelse(is.na(State.Rate), State.Avg, State.Rate)) %>%
  select(-State.Avg)


usethis::use_data(hospitalData, overwrite=TRUE)
