# README.md

## Project Introduction
This project looks to investigate the data around NFL super bowl winning rosters, to see what possible trends exist between these rosters, and how one might draw insights when wanting to build a roster that has a higher likelihood of winning/appearing in a super bowl. 

This exploratory analysis is then followed by a logistical regression model for predicting super bowl winners and super bowl appearance teams based on regular season statistics. This prediction model predicts whether an NFL offense will appear and/or win a super bowl based on their regular season statistics, and then the same for the defense of a given team, based on aggregated data from 2017-2022. 

## Main Issues found in dataset
### EDA Issues
- The Super bowl roster drafted column included nested information that we wanted to expand in order to just get the team who drafted the particular player. Unfortunately because of the existence of two separate football leagues in the 60s. This eventually led us to forgo the draft data analysis from before the NFL AFL merger. 
- There are a lot of different positions on an NFL roster, and this led to high cardinality of categorical columns when trying to understand trends or traits of players on winning rosters. We combatted this by grouping into positional groups like offensive and defensive lines, running backs, receivers etc. We saw that in the older rosters there were some positions that have essentially gone extinct in todays game, so additional research was required to group these positions correctly. 
- There was also data wrangling and aggregation across datasets required in order to connect the winning super bowl team of a given year to their team's offensive and defensive statistics.

### Prediction model issues
- The team performance statistics were separated into individual files for each type of statistic for each year. This led to aggregation of all the files and specifying the type of statistic and scanning for any duplicate columns that may exist between those files, and removing or renaming where necessary. 
- Identifying potential X for team statistics and super bowl appearance/wins (y) was 
- Overall amount of data for super bowl winners: since there can only be one super bowl winner per year, we had a very limited amount of actual winners to train our data. This eventually led to a fairly low kappa score in our prediction model, even after oversampling with a SMOTE method to try and create a more even dataset, since SMOTE essentially duplicated the rows of super bowl winners, however it did help with predicting accuracy in a more realistic environment than pre-oversampling.
- Outliers in data were identified but not removed since these sometimes coincided with being super bowl appearing or winning teams, meaning we would lose significant rows in for predicting our y. 
- Only 5 years of statistics was eventually used for the prediction model (last 5 years), due to the manual effort required to exporting each file and the time constrains for this project. 
---

## Questions to answer
- What traits should an NFL organisation look at in a player when bringing them into their team, when aspiring to win an NFL championship (AKA Super Bowl)
- Are there any trends in terms of player traits for the Super Bowl winning players, the year they won their nth or 1st championship?
- What specific team performance statistics (on the offensive and defensive side of the ball) are likely to lead to higher likelihood of a team reaching the Super Bowl and/or a team winning the Super Bowl

## Answers to questions
### Conclusion to EDA on Age per position trends
When looking at the players on super bowl winning rosters throughout the decades, the trends per age indicate whether the player is in or near their prime. 

#### Defensive players
Defensive linemen particularly haven't changed too much in terms of age and tend to be around 25 and 28 when they are on super bowl winning rosters. 
Linebackers' age ranges have centered around 24-28, likely because they do similar jobs to defensive linemen but veer a little on the younger side due to the more athletic demands of the position, relative to linemen. 
Defensive backs are only slightly younger with their lower age range and actually have higher upper ranges relative to linebackers which was surprising. This might be due to the lesser physical nature of the position compared to linebacker, while maintaining similar heights and other stature measures. 

#### Offensive players
Offensive linemen and quarterbacks have tended to be the oldest on the field throughout the years when winning superbowls, suggesting that there is a certain pedigree and number of years in the NFL required in order to be put in a best position for winning. 

Receivers looked to have become decreasingly younger, suggesting the game has shifted to a more receiver-dependent playing style, which can be supported by the fact that passing became more frequent in recent decades. The shorter IQRs of receivers ages' also indicate the shorter 'superbowl winning prime' ages for receivers, linebackers and running backs. 

### Conclusion to EDA on Years in league before first super bowl

When looking at the average number of years in the nfl before a player typically finds themselves on a super bowl winning roster, one can see there is a general downward trend in the average number of years in the league across the last three decades, all apart from quarterbacks which has seen somewhat of a steady increase. This further supports the previous claim that quarterbacks with more years in the league has a higher likelihood to lead a team to a superbowl. 

Another insight of interest is that the typical rookie contract is around 3 years, which coincides with the general average time in league when winning a championship. This can suggest multiple assumptions.

- Teams draft/sign young players with the intent that they will win a championship by the last year of that player's contract. These 3 year contracts typically apply to players who have been drafted in the first 4 rounds of the draft.
- Players who finish their rookie contract (assuming 2-3 years) will sign a new contract and win relatively soon after signing that new contract. Teams therefore might be looking for players who are finishing their rookie contract to bring those into their organisation to boost their chances of winning.

What this would mean for a general manager or team looking to build a super-bowl calibre team: 

- If you are looking to win within the next 3 years, the players you sign in the next year are the most significant. Look to sign a quarterback who has already been in the league for 2-3 years and shows potential to grow further.
- If you are looking to win a superbowl in the next year, be confident the players you have in your team for at least the last 2 years are the some of the best in their position across the whole league. The chances of winning super bowls with those players will decrease after the next 2 years. 
- This increases the worth of quarterbacks who have been in the league for 4+ years and are still playing at a high level, as their chances of winning a super bowl remain strong until they've been in the league for about 8-9 years, provided they remain healthy. 

### Conclusion to EDA on Player draft analysis by teams: 

In terms of where players who won super bowls were drafted by or if they were drafted at all, we see that throughout the decades, offensive linemen and defensive backs were the highest volume of players signed to rosters that ended up winning super bowls in their careers. 

The first assumption of why offensive linemen are important: protect the quarterback, and win the game up front for the run game. This assumption was valid for both offensive linemen who were drafted and those who went undrafted. 
The next assumption regarding defensive backs, stop the opposing players ability to pass the ball downfield to limit their overall abilities. 


When looking at the number of teams involved in a superbowl winning team's roster, this showed that typically players were signed from 5-6 different teams (free agency also being a 'team' in this case) per super bowl winning roster, when there are a spread out number of teams winning superbowls in a given decade. 

Finally, for the teams that won multiple super bowls in particular decades, it was clear to see that they drafted a lot of players onto their roster themselves, with the the next typical 'team' being players who went undrafted, which goes to show the importance and significance for an NFL organisation to scout extensively, draft well and never count out undrafted free agents when looking to build a super bowl winning roster.

### Conclusion to EDA on College and Conferences for SB Winning players
#### Colleges
In conclusion to super bowl winning players and the colleges they played at, super bowl calibre players can be found from many colleges, and this number has increased over the decades. The typical number of colleges centering around 175 per decade. The total number of unique colleges in the super bowl winning roster file is 442, suggesting that these colleges also follow trends for the decades in terms of the calibre of player required for winning a super bowl. 

When looking at colleges that provided more than 'n' (in this case, n=3) players to super bowl winning teams within a particular timeframe, the average number of colleges providing n players to super bowl winning teams per year looked to normalise around an average of 3 after 1995. 
In this case, demonstrated in the scatterplot from college_count vs year, this would mean the super bowl roster for that year had an average of 3 colleges providing 3 or more players on that team, indicating either there are particular college football teams with a better reputation for creating super-bowl winning calibre players, or that these teams want players to come into their organisations with a familiar feel to put them in the best position to win straight away in the league. 

Looking at the top college feeders per decade, where the amount of players averaged 16 from the 'top' college, LSU (Lousiana State University) is the only college which was the top university in multiple decades for super bowl winning players. 
Other teams included Miami University in the 90s, an infamous generation of players like Ed Reed and Ray Lewis, and UCLA, Nebraska and Colorado in the 80s. 

What this could mean for NFL organisations: the chances of finding potential super bowl winners would increase if they are able to draft or sign players from these 'top' colleges, provided the colleges' performance statistics and coaching staff are remaining constant. If the NFL teams are able to sign multiple players from the same college, whether this leads to increased comraderie between team mates early on, or matches their team system of playing, they could look to sign multiple players from an average of 3 different colleges to match the trends of recent super bowl winning rosters. 

However, this should be taken with the consideration that the college football playing landscape has changed drastically with the introduction of NIL and college players now being able to legally accept compensation for their likeness, effectively being able to be paid as college athletes, as this was not the case before, and wouldn't be included in the time frame for this dataset. Certain colleges might become more attractive for top student athletes to attend in order to earn more money based on the university's reputation or potential reputation. 


#### Conferences 
For college conferences, particularly Division 1 in this analysis, the trend for super bowl winning players and their college conference showed that the SEC, Big 10 and Pac-12 tended to be the best conferences, indicating their level of higher competition degree, making colleges in these conferences more attractive for NFL execs to fill their rosters with players from there. 

It is also worth considering that the 'Other' for conferences is significantly large, indicating there are super-bowl winning calibre players in other colleges and divisions of college football, as well as abroad in places other than american college football teams. However, due to the limits on this current dataset, we were unable to dig further into this 'Other' category to find out any potential trends outside of Division 1 football conferences.  

---

### Next Steps
- Compare the trends identified in super bowl rosters among the players and positional groups against the rest of the rosters in the league per year (non super bowl winning rosters)
- Add more years of team performance statistics from previous NFL seasons to increase the sample size for the SB appearance and SB Win prediction model. 
- Look to incorporate playoff game (knockout stages of season) team performance statistics to see if this can help improve the overall accuracy and error metric scores of the prediction models and if any additional X's can be uncovered. 
- Create model for playoff appearance based off regular season team performance statistics.
- Introduce player-level statistic aggregations among the positional groups and create a model for predicting player SB appearance and SB Win likelihood based on in-season statistical performance. 

---

## Data sources:
The data in this project has been retrieved from pro-football-reference.com, for both NFL and College Football data. 

## Collaborators: 
- Alex Ferrer
- Henry Soysa

