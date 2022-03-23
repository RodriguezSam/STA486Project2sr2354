
library(dplyr)
library(tidycensus)
library(censusapi)

source('~/.Rprofile')
CENSUS_API_KEY = Sys.getenv('census_api_key')

AZ_County_Populations <- get_estimates(
  geography = "county",
  state = c('AZ'),
  product = "characteristics",
  breakdown = c('SEX', 'AGEGROUP', 'RACE', 'HISP'),
  breakdown_labels = T,
  year = 2015
)

AZ_County <- getCensus(name = "pep/population",
                       vars = c("STATE", "COUNTY", "GEONAME", "DATE_DESC", "POP"),
                       regionin = "state:04",
                       vintage = '2012',
                       region = 'county:*',
                       key = CENSUS_API_KEY)
