Sys.setenv("VROOM_CONNECTION_SIZE"=999999999) # will receive errors if conenction size is too low

library(data.table)
library(nbastatR)
library(tidyverse)

##### --- NBA Source buggy note

## Sometimes the NBA packages times out / you do too many calls.
# Short term, makeshift workaround, just detach and reload the package

#detach("package:nbastatR", unload = TRUE)
#library(nbastatR)

#### Set working directory to selected folder

#setwd("")

# load current season's box scores game ids
current_player_logs <- 
  game_logs(seasons = 2024,
            result_types = c("player"), 
            season_types =  c("Regular Season")) %>% # replace with below when time comes for it
  #season_types =  c("Regular Season", "Playoffs", "PlayIn")) %>%  
  select(idGame) %>% 
  distinct()

# load range of seasons wanted of box scores game ids
# if seeking seasons prior to the 19-20 season you would exclude "PlayIn" from call
player_logs <- game_logs(seasons = c(2020:2023),
                         result_types = c("player"), 
                         season_types =  c("Regular Season", "Playoffs", "PlayIn")) %>% 
  select(idGame) %>% 
  distinct()

# read in existing advanced box scores, select only the idGame
adv_games_logs <- read.csv("Player_game_logs_advanced.csv") %>% 
  distinct() %>% 
  group_by(idGame) %>% 
  mutate(poss = as.numeric(sum(possessions))) %>% 
  filter(poss > 0) %>% # sometimes you get games with no data - may be not yet entered
  select(idGame)  %>% 
  distinct()

# anti join to pull new records yet collected
games <- anti_join(player_logs, adv_games_logs) %>% 
  distinct(idGame)

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

# reload advanced dataset
game_logs_adv_set <- read.csv("Player_game_logs_advanced.csv") %>% 
  select(-X) %>% 
  filter(!is.na(slugTeam)) %>% 
  distinct() %>% 
  group_by(idGame) %>% 
  mutate(poss = as.numeric(sum(possessions))) %>% 
  filter(poss > 0) %>% 
  select(-poss) %>% 
  distinct() 

# stack collected games into existing loaded frame

game_logs_adv_set_updated <- 
  rbind(game_logs_adv_set, game_logs_adv) %>% distinct()

# before saving, ensure that rows in game_logs_adv_set_update > game_logs_adv_set

write.csv(game_logs_adv_set_update, "Player_game_logs_advanced.csv")
