Sys.setenv("VROOM_CONNECTION_SIZE"=999999999) # will receive errors if conenction size is too low

# install packages if you need to

#if (!require(devtools)) install.packages("devtools")
#if (!require(nbastatR)) devtools::install_github("abresler/nbastatR")

library(tidyverse)
library(nbastatR)

##### --- NBA Source buggy note

## Sometimes the NBA packages times out / you do too many calls.
# Short term, makeshift workaround, just detach and reload the package

#detach("package:nbastatR", unload = TRUE)
#library(nbastatR)

#### Set working directory to selected folder

#setwd("")

# load current season's box scores
player_logs <- game_logs(seasons = 2024, 
                         result_types = c("player"), 
                         season_types =  c("Regular Season")) %>% 
  rename(Season = slugSeason, 
         League = slugLeague, 
         Season_Type = typeSeason, 
         Date = dateGame, 
         team = nameTeam, 
         Game_Location = locationGame, 
         Matchup = slugMatchup, 
         Team = slugTeam, 
         opp_team = slugOpponent, 
         Game_Outcome = outcomeGame, 
         Player = namePlayer, 
         ID = idPlayer)

# function to assign groups to every n numbers
# after too many calls in succession, you will be blocked from API, sometimes it can be a considerable delay.
# recommend to terminate session after each set of n games - detach nbastartR and repeat until all games are collected 

rep100<-function(games){
  games$group =  rep(1:ceiling(nrow(games)/100), each =100)[1:nrow(games)]
  games
}

# assign function to dataset of games
games <- games %>% 
  ungroup() %>% 
  group_modify(~rep100(.))

# grab first n of games via group
game_logs_adv <- games %>% 
  filter(group == 1) %>% 
  distinct()

# grab the advanced box scores for all players
game_logs_adv <- box_scores(game_logs_adv$idGame, 
                         box_score_types = c("Advanced"),
                         result_types = "player") #(could change this to teams)

# grab data element and create a table
game_logs_adv <- game_logs_adv[[2]][[1]]

# sometimes you get games with no data - may be not yet entered so they are excluded
game_logs_adv <- game_logs_adv %>% 
  group_by(idGame) %>% 
  mutate(poss = sum(possessions)) %>% 
  filter(poss >0) %>% 
  select(-poss) %>% 
  ungroup()

write.csv(game_logs_adv, "Player_game_logs_advanced.csv")
