
#
#  DCU
#
# inch; 1inch = 2.54cm

df_DCU_all <- read.csv('C:/Users/jkerexeta/Documents/PROIEKTUK/CAPTAIN/interactive-clustering/data/t7.3/t7.3/Complete_2020/DCU_2020.06.18/Data Transfer Participants Randomized - 18th June 2020.csv', fileEncoding = "latin1", check.names=FALSE, stringsAsFactors = F)
colnames(df_DCU_all)


as.character(df_DCU_all[3450,1:33])

df_DCU_daily = df_DCU_all[1:3430,]


df_DCU_prePost_profile <- data.frame(df_DCU_all[3451:3506,1:33])
colnames(df_DCU_prePost_profile) <- as.character(df_DCU_all[3450,1:33])


df_DCU_prePost_assessment <- data.frame(df_DCU_all[3512:3562,1:23])
colnames(df_DCU_prePost_assessment) <- as.character(df_DCU_all[3511,1:23])

df_DCU_all <- NULL

#
#  MAYNOOTH
#
# inch

df_MAYNOOTH_all <- read.csv('C:/Users/jkerexeta/Documents/PROIEKTUK/CAPTAIN/interactive-clustering/data/t7.3/t7.3/Complete_2020/Maynooth_2020.03.24/....csv', fileEncoding = "latin1", check.names=FALSE, stringsAsFactors = F)
df_MAYNOOTH_assessments <- read.csv("C:/Users/jkerexeta/Documents/PROIEKTUK/CAPTAIN/interactive-clustering/data/t7.3/t7.3/Complete_2020/Maynooth_2020.03.24/May_assessments.csv", fileEncoding = "latin1", check.names=FALSE, stringsAsFactors = F)

#
#  AUTH
#
# cm

df_AUTH <- read.csv('C:/Users/jkerexeta/Documents/PROIEKTUK/CAPTAIN/interactive-clustering/data/t7.3/t7.3/AUTH_2020.01.09/Captain_Participants_Assessments_AUTH.csv', fileEncoding = "latin1", check.names=FALSE, stringsAsFactors = F)

colnames(df_AUTH) <- df_AUTH[2,]
colnames(df_AUTH)[c(1,2,10:length(colnames(df_AUTH)))]

df_AUTH_assessment <- df_AUTH[3:20,c(1,2,10:length(colnames(df_AUTH)))]
df_AUTH_assessment$source = 'AUTH'

#
#  APSS
#
# inch

df_APSS_daily <- read.csv('C:/Users/jkerexeta/Documents/PROIEKTUK/CAPTAIN/interactive-clustering/data/t7.3/t7.3/APSS_2019.12.12/Daily_Diaries_ITA.csv', fileEncoding = "latin1", check.names=FALSE, stringsAsFactors = F)
levels(as.factor(df_APSS_daily$`Partecipant code`))

df_APSS_assessments <- read.csv('C:/Users/jkerexeta/Documents/PROIEKTUK/CAPTAIN/interactive-clustering/data/t7.3/t7.3/APSS_2019.12.12/Standard_Questionnaire_ITA.csv', fileEncoding = "latin1", check.names=FALSE, stringsAsFactors = F)
colnames(df_APSS_assessments)[-c(24:25)]
df_APSS_assessments_ <-df_APSS_assessments[,-c(24,25)]
summary(df_APSS_assessments_)

df_APSS_profiles <- read.csv('C:/Users/jkerexeta/Documents/PROIEKTUK/CAPTAIN/interactive-clustering/data/t7.3/t7.3/APSS_2019.12.12/Users_Profiling_ITA.csv', fileEncoding = "latin1", check.names=FALSE, stringsAsFactors = F)






#############################################################################
#############################################################################
##  ASSESSMENTS


df_DCU_prePost_assessment
df_APSS_assessments_
df_AUTH_assessment
df_MAYNOOTH_assessments

# Dates
df_AUTH_assessment$`Evaluation date` <- as.Date(df_AUTH_assessment$`Evaluation date`, format = "%d/%m/%Y")
df_DCU_prePost_assessment$Date <- as.Date(df_DCU_prePost_assessment$Date, format = "%d/%m/%Y")
df_APSS_assessments_$Date <- as.Date(df_APSS_assessments_$`Date of questionnaire compilation`, format = "%d/%m/%Y")
df_MAYNOOTH_assessments$Date <- as.Date(df_MAYNOOTH_assessments$Date, format = "%d/%m/%Y")

# source
df_AUTH_assessment$source = 'AUTH'
df_DCU_prePost_assessment$source = 'DCU'
df_APSS_assessments_$source = 'APSS'
df_MAYNOOTH_assessments$source = 'MAYNOOTH'


colnames(df_AUTH_assessment)
colnames(df_DCU_prePost_assessment)
colnames(df_APSS_assessments_)
colnames(df_MAYNOOTH_assessments)

assessment_cols = c(
  "User ID",                           "Evaluation date",                   "Weight",                           
  "Height",                            "BMI",                               "Chair Stand",                      
  "Arm Curl",                          "Two Minute Step",                   "Chair Sit and Reach 1",            
   "Chair Sit and Reach 2",             "Back Scratch 1",                    "Back Scratch 2",                   
   "Foot Up And Go 1",                  "Foot Up And Go 2",                  "MoCA",                             
   "MSC - A",                           "Declarative Knowledge",             "Procedural Knowledge",             
   "Conditional Knowledge",             "Planning",                          "Information Management Strategies",
   "Comprehension Monitoring",          "Debugging Strategies",              "Evaluation",                       
   "MNA mini",                          "source" 
  )

diccionary = list(
  "DB"=c(
    "AUTH",
    "DCU",
    "APSS",
    "MAY"
  ),
  "User ID"=c(
    "User ID",
    "User ID",
    "ITAID Partecipant",
    "﻿User ID"
  )
)




user_id <- c()
procedencia <- c()
for(user in unique(df_AUTH_assessment[,"User ID"])){
  user_id <- c(user_id, user)
  procedencia <- c(procedencia, 'AUTH')
}
for(user in unique(df_DCU_prePost_assessment[,"User ID"])){
  user_id <- c(user_id, user)
  procedencia <- c(procedencia, 'DCU')
}
for(user in unique(df_APSS_assessments_[,"ITAID Partecipant"])){
  if((user != "") && (user != "* DROP OUT")){
    user_id <- c(user_id, user)
    procedencia <- c(procedencia, 'APSS')
    
  }
}
for(user in unique(df_MAYNOOTH_assessments[,"﻿User ID"])){
  user_id <- c(user_id, user)
  procedencia <- c(procedencia, 'MAY')
}
length(user_id)
length(procedencia)


filter_numeric <- function(val){
  numeric_chars <- c()
  valid_characters <- c("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ",", "-", "+")
  characters <- strsplit(val, "")[[1]]
  for(char in characters){
    if(char %in% valid_characters){
      numeric_chars <- c(numeric_chars, char)
    }
  }
  return(paste(numeric_chars, collapse = ""))
}

inch_to_cm <- function(val){
  val_filtred <- filter_numeric(as.character(val)) # some are given "1.5 inch"
  return(as.character(as.numeric(val_filtred) * 2.54))
}

filter_dividers <- function(num){
  num_1 <- strsplit(num, "/")[[1]]
  num_2 <- strsplit(num_1, "v")[[1]]
  return(num_2[1])
}

# Tenemos 74 usuarios distintos

first_assessment_date = c()
second_assessment_date = c()

first_weight <- c()                           
first_height <- c()                           
first_BMI <- c()                           
first_chair_stand <- c()                           
first_arm_curl <- c()                           
first_two_minute_step <- c()                           
first_chair_sit_and_reach1 <- c()                           
first_chair_sit_and_reach2 <- c()
first_back_scratch_1 <- c()                           
first_back_scratch_2 <- c()                           
first_foot_up_and_go_1 <- c()                           
first_foot_up_and_go_2 <- c()                           
first_MOCA <- c()                           
first_MSC <- c()                           
first_declarative_knowledge <- c()                           
first_procedural_knowledge <- c()                           
first_conditional_knowledge <- c()                           
first_planning <- c()                           
first_Information_Management_Strategies <- c()                           
first_Comprehension_Monitoring <- c()                           
first_Debugging_Strategies <- c()                           
first_Evaluation <- c()                           
first_MNA_mini <- c()  




second_weight <- c()                           
second_height <- c()                           
second_BMI <- c()                           
second_chair_stand <- c()                           
second_arm_curl <- c()                           
second_two_minute_step <- c()                           
second_chair_sit_and_reach1 <- c()                           
second_chair_sit_and_reach2 <- c()
second_back_scratch_1 <- c()                           
second_back_scratch_2 <- c()                           
second_foot_up_and_go_1 <- c()                           
second_foot_up_and_go_2 <- c()                           
second_MOCA <- c()                           
second_MSC <- c()                           
second_declarative_knowledge <- c()                           
second_procedural_knowledge <- c()                           
second_conditional_knowledge <- c()                           
second_planning <- c()                           
second_Information_Management_Strategies <- c()                           
second_Comprehension_Monitoring <- c()                           
second_Debugging_Strategies <- c()                           
second_Evaluation <- c()                           
second_MNA_mini <- c()  


for(i in 1:length(user_id)){
  if(procedencia[i] == 'AUTH'){
    
    df_user_i <- df_AUTH_assessment[which(df_AUTH_assessment$`User ID` == user_id[i]), ]
    
    # assessment dates
    dates_user_i = df_AUTH_assessment$`Evaluation date`[which(df_AUTH_assessment$`User ID` == user_id[i])]
    
    
    first_loc <- which.min(dates_user_i)
    second_loc <- which.max(dates_user_i)
    # Date
    
    first_assessment_date = c(first_assessment_date, as.character(dates_user_i[first_loc]))
    second_assessment_date = c(second_assessment_date, as.character(dates_user_i[second_loc]))
    
    # weight
    
    first_weight <- c(first_weight, df_user_i[first_loc, which(colnames(df_user_i) == "Weight")])
    second_weight <- c(second_weight, df_user_i[second_loc, which(colnames(df_user_i) == "Weight")])
    
    # "Height"
    first_height <- c(first_height, df_user_i[first_loc, which(colnames(df_user_i) == "Height")])
    second_height <- c(second_height, df_user_i[second_loc, which(colnames(df_user_i) == "Height")])
    
    
    # "BMI"
    first_BMI <- c(first_BMI, df_user_i[first_loc, which(colnames(df_user_i) == "BMI")])
    second_BMI <- c(second_BMI, df_user_i[second_loc, which(colnames(df_user_i) == "BMI")])
    
    # "Chair Stand"
    
    first_chair_stand <- c(first_chair_stand, df_user_i[first_loc, which(colnames(df_user_i) == "Chair Stand")])
    second_chair_stand <- c(second_chair_stand, df_user_i[second_loc, which(colnames(df_user_i) == "Chair Stand")])
    
    
    # "Arm Curl"
    
    first_arm_curl <- c(first_arm_curl, df_user_i[first_loc, which(colnames(df_user_i) == "Arm Curl")])
    second_arm_curl <- c(second_arm_curl, df_user_i[second_loc, which(colnames(df_user_i) == "Arm Curl")])    
    
    # "Two Minute Step"
    first_two_minute_step <- c(first_two_minute_step, df_user_i[first_loc, which(colnames(df_user_i) == "Two Minute Step")])
    second_two_minute_step <- c(second_two_minute_step, df_user_i[second_loc, which(colnames(df_user_i) == "Two Minute Step")])
    
    # "Chair Sit and Reach 1"
    first_chair_sit_and_reach1 <- c(first_chair_sit_and_reach1, df_user_i[first_loc, which(colnames(df_user_i) == "Chair Sit and Reach 1")])
    second_chair_sit_and_reach1 <- c(second_chair_sit_and_reach1, df_user_i[second_loc, which(colnames(df_user_i) == "Chair Sit and Reach 1")])
    
    # "Chair Sit and Reach 2"
    first_chair_sit_and_reach2 <- c(first_chair_sit_and_reach2, df_user_i[first_loc, which(colnames(df_user_i) == "Chair Sit and Reach 2")])
    second_chair_sit_and_reach2 <- c(second_chair_sit_and_reach2, df_user_i[second_loc, which(colnames(df_user_i) == "Chair Sit and Reach 2")])
    
    # "Back Scratch 1"
    first_back_scratch_1 <- c(first_back_scratch_1, df_user_i[first_loc, which(colnames(df_user_i) == "Back Scratch 1")])
    second_back_scratch_1 <- c(second_back_scratch_1, df_user_i[second_loc, which(colnames(df_user_i) == "Back Scratch 1")])
    
    # "Back Scratch 2"
    first_back_scratch_2 <- c(first_back_scratch_2, df_user_i[first_loc, which(colnames(df_user_i) == "Back Scratch 2")])
    second_back_scratch_2 <- c(second_back_scratch_2, df_user_i[second_loc, which(colnames(df_user_i) == "Back Scratch 2")])
    
    # "Foot Up And Go 1"
    first_foot_up_and_go_1 <- c(first_foot_up_and_go_1, df_user_i[first_loc, which(colnames(df_user_i) == "Foot Up And Go 1")])
    second_foot_up_and_go_1 <- c(second_foot_up_and_go_1, df_user_i[second_loc, which(colnames(df_user_i) == "Foot Up And Go 1")])
    
    
    # "Foot Up And Go 2"
    first_foot_up_and_go_2 <- c(first_foot_up_and_go_2, df_user_i[first_loc, which(colnames(df_user_i) == "Foot Up And Go 2")])
    second_foot_up_and_go_2 <- c(second_foot_up_and_go_2, df_user_i[second_loc, which(colnames(df_user_i) == "Foot Up And Go 2")])
    
    
    # "MoCA" 
    
    first_MOCA <- c(first_MOCA, df_user_i[first_loc, which(colnames(df_user_i) == "MoCA")])
    second_MOCA <- c(second_MOCA, df_user_i[second_loc, which(colnames(df_user_i) == "MoCA")])
    
    # "MSC - A"
    first_MSC <- c(first_MSC, df_user_i[first_loc, which(colnames(df_user_i) == "MSC - A")])
    second_MSC <- c(second_MSC, df_user_i[second_loc, which(colnames(df_user_i) == "MSC - A")])
    
    # "Declarative Knowledge"
    first_declarative_knowledge <- c(first_declarative_knowledge, df_user_i[first_loc, which(colnames(df_user_i) == "Declarative Knowledge")])
    second_declarative_knowledge <- c(second_declarative_knowledge, df_user_i[second_loc, which(colnames(df_user_i) == "Declarative Knowledge")])
    
    # "Procedural Knowledge"  
    first_procedural_knowledge <- c(first_procedural_knowledge, df_user_i[first_loc, which(colnames(df_user_i) == "Procedural Knowledge")])
    second_procedural_knowledge <- c(second_procedural_knowledge, df_user_i[second_loc, which(colnames(df_user_i) == "Procedural Knowledge")])
    
    # "Conditional Knowledge"
    first_conditional_knowledge <- c(first_conditional_knowledge, df_user_i[first_loc, which(colnames(df_user_i) == "Conditional Knowledge")])
    second_conditional_knowledge <- c(second_conditional_knowledge, df_user_i[second_loc, which(colnames(df_user_i) == "Conditional Knowledge")])
    
    # "Planning"
    first_planning <- c(first_planning, df_user_i[first_loc, which(colnames(df_user_i) == "Planning")])
    second_planning <- c(second_planning, df_user_i[second_loc, which(colnames(df_user_i) == "Planning")])
    
    # "Information Management Strategies"
    first_Information_Management_Strategies <- c(first_Information_Management_Strategies, df_user_i[first_loc, which(colnames(df_user_i) == "Information Management Strategies")])
    second_Information_Management_Strategies <- c(second_Information_Management_Strategies, df_user_i[second_loc, which(colnames(df_user_i) == "Information Management Strategies")])
    
    # "Comprehension Monitoring"
    first_Comprehension_Monitoring <- c(first_Comprehension_Monitoring, df_user_i[first_loc, which(colnames(df_user_i) == "Comprehension Monitoring")])
    second_Comprehension_Monitoring <- c(second_Comprehension_Monitoring, df_user_i[second_loc, which(colnames(df_user_i) == "Comprehension Monitoring")])
    
    # "Debugging Strategies"
    first_Debugging_Strategies <- c(first_Debugging_Strategies, df_user_i[first_loc, which(colnames(df_user_i) == "Debugging Strategies")])
    second_Debugging_Strategies <- c(second_Debugging_Strategies, df_user_i[second_loc, which(colnames(df_user_i) == "Debugging Strategies")])
    
    # "Evaluation"      
    first_Evaluation <- c(first_Evaluation, df_user_i[first_loc, which(colnames(df_user_i) == "Evaluation")])
    second_Evaluation <- c(second_Evaluation, df_user_i[second_loc, which(colnames(df_user_i) == "Evaluation")])
    
    # "MNA mini"
    first_MNA_mini <- c(first_MNA_mini, df_user_i[first_loc, which(colnames(df_user_i) == "MNA mini")])
    second_MNA_mini <- c(second_MNA_mini, df_user_i[second_loc, which(colnames(df_user_i) == "MNA mini")])
    

  }else if(procedencia[i] == 'DCU'){
    
    
    # df_DCU_prePost_assessment
    colnames(df_DCU_prePost_assessment)
    
    
    
    df_user_i <- df_DCU_prePost_assessment[which(df_DCU_prePost_assessment$`User ID` == user_id[i]), ]
    
    # assessment dates
    dates_user_i = df_DCU_prePost_assessment$Date[which(df_DCU_prePost_assessment$`User ID` == user_id[i])]
    
    
    first_loc <- which.min(dates_user_i)
    second_loc <- which.max(dates_user_i)
    # Date
    
    first_assessment_date = c(first_assessment_date, as.character(dates_user_i[first_loc]))
    second_assessment_date = c(second_assessment_date, as.character(dates_user_i[second_loc]))
    
    # weight
    # No hay
    
    first_weight <- c(first_weight, NA)
    second_weight <- c(second_weight, NA)
    
    # "Height"
    # No Hay
    first_height <- c(first_height, NA)
    second_height <- c(second_height, NA)
    
    
    # "BMI"
    # No hay
    first_BMI <- c(first_BMI, NA)
    second_BMI <- c(second_BMI, NA)
    
    # "Chair Stand"
    
    first_chair_stand <- c(first_chair_stand, df_user_i[first_loc, which(colnames(df_user_i) == "Chair Stand (Number in 30 seconds)")])
    second_chair_stand <- c(second_chair_stand, df_user_i[second_loc, which(colnames(df_user_i) == "Chair Stand (Number in 30 seconds)")])
    
    
    # "Arm Curl"
    
    first_arm_curl <- c(first_arm_curl, df_user_i[first_loc, which(colnames(df_user_i) == "Arm Curl (Number in 30 seconds)")])
    second_arm_curl <- c(second_arm_curl, df_user_i[second_loc, which(colnames(df_user_i) == "Arm Curl (Number in 30 seconds)")])    
    
    # "Two Minute Step"
    first_two_minute_step <- c(first_two_minute_step, df_user_i[first_loc, which(colnames(df_user_i) == "Two Minute Step (Number of Steps)")])
    second_two_minute_step <- c(second_two_minute_step, df_user_i[second_loc, which(colnames(df_user_i) == "Two Minute Step (Number of Steps)")])
    
    # "Chair Sit and Reach 1"
    val_1 <- df_user_i[first_loc, which(colnames(df_user_i) == "Chair Sit & Reach (Nearest 1/2 inch: +/-) Trial 1")]
    first_chair_sit_and_reach1 <- c(first_chair_sit_and_reach1, inch_to_cm(val_1))
    val_2 <- df_user_i[second_loc, which(colnames(df_user_i) == "Chair Sit & Reach (Nearest 1/2 inch: +/-) Trial 1")]
    second_chair_sit_and_reach1 <- c(second_chair_sit_and_reach1, inch_to_cm(val_2))
    
    # "Chair Sit and Reach 2"
    
    val_1 <- df_user_i[first_loc, which(colnames(df_user_i) == "Chair Sit & Reach (Nearest 1/2 inch: +/-) Trial 2")]
    first_chair_sit_and_reach2 <- c(first_chair_sit_and_reach2, inch_to_cm(val_1))
    
    val_2 <- df_user_i[second_loc, which(colnames(df_user_i) == "Chair Sit & Reach (Nearest 1/2 inch: +/-) Trial 2")]
    second_chair_sit_and_reach2 <- c(second_chair_sit_and_reach2, inch_to_cm(val_2))
    
    # "Back Scratch 1"
    val_1 <- df_user_i[first_loc, which(colnames(df_user_i) == "Chair Sit & Reach (Nearest 1/2 inch: +/-) Trial 2")]
    first_back_scratch_1 <- c(first_back_scratch_1, inch_to_cm(val_1))
    
    val_2 <- df_user_i[second_loc, which(colnames(df_user_i) == "Chair Sit & Reach (Nearest 1/2 inch: +/-) Trial 2")]
    second_back_scratch_1 <- c(second_back_scratch_1, inch_to_cm(val_2))
    
    
    # "Back Scratch 2"
    first_back_scratch_2 <- c(first_back_scratch_2, inch_to_cm(df_user_i[first_loc, which(colnames(df_user_i) == "Back Stretch (Nearest 1/2 inch: +/-) Trial 2")]))
    second_back_scratch_2 <- c(second_back_scratch_2, inch_to_cm(df_user_i[second_loc, which(colnames(df_user_i) == "Back Stretch (Nearest 1/2 inch: +/-) Trial 2")]))
    
    # "Foot Up And Go 1"
    first_foot_up_and_go_1 <- c(first_foot_up_and_go_1, filter_numeric(df_user_i[first_loc, which(colnames(df_user_i) == "Foot Up-and-Go (Nearest 1/10 second) Trial 1")]))
    second_foot_up_and_go_1 <- c(second_foot_up_and_go_1, filter_numeric(df_user_i[second_loc, which(colnames(df_user_i) == "Foot Up-and-Go (Nearest 1/10 second) Trial 1")]))
    
    
    # "Foot Up And Go 2"
    first_foot_up_and_go_2 <- c(first_foot_up_and_go_2, filter_numeric(df_user_i[first_loc, which(colnames(df_user_i) == "Foot Up-and-Go (Nearest 1/10 second) Trial 2")]))
    second_foot_up_and_go_2 <- c(second_foot_up_and_go_2, filter_numeric(df_user_i[second_loc, which(colnames(df_user_i) == "Foot Up-and-Go (Nearest 1/10 second) Trial 2")]))
    
    
    # "MoCA"    ## dividers
    
    first_MOCA <- c(first_MOCA, filter_dividers(df_user_i[first_loc, which(colnames(df_user_i) == "Montreal Cognitive Assessment (MOCA) result")]))
    second_MOCA <- c(second_MOCA, filter_dividers(df_user_i[second_loc, which(colnames(df_user_i) == "Montreal Cognitive Assessment (MOCA) result")]))
    
    # "MSC - A"
    first_MSC <- c(first_MSC, filter_dividers(df_user_i[first_loc, which(colnames(df_user_i) == "Memory Complaint Scale (MCS) Version A (Self-Reported) Score")]))
    second_MSC <- c(second_MSC, filter_dividers(df_user_i[second_loc, which(colnames(df_user_i) == "Memory Complaint Scale (MCS) Version A (Self-Reported) Score")]))
    
    # "Declarative Knowledge"
    first_declarative_knowledge <- c(first_declarative_knowledge, filter_dividers(df_user_i[first_loc, which(colnames(df_user_i) == "Declarative Knowledge")]))
    second_declarative_knowledge <- c(second_declarative_knowledge, filter_dividers(df_user_i[second_loc, which(colnames(df_user_i) == "Declarative Knowledge")]))
    
    # "Procedural Knowledge"  
    first_procedural_knowledge <- c(first_procedural_knowledge, filter_dividers(df_user_i[first_loc, which(colnames(df_user_i) == "Procedural Knowledge")]))
    second_procedural_knowledge <- c(second_procedural_knowledge, filter_dividers(df_user_i[second_loc, which(colnames(df_user_i) == "Procedural Knowledge")]))
    
    # "Conditional Knowledge"
    first_conditional_knowledge <- c(first_conditional_knowledge, filter_dividers(df_user_i[first_loc, which(colnames(df_user_i) == "Conditional Knowledge")]))
    second_conditional_knowledge <- c(second_conditional_knowledge, filter_dividers(df_user_i[second_loc, which(colnames(df_user_i) == "Conditional Knowledge")]))
    
    # "Planning"
    first_planning <- c(first_planning, filter_dividers(df_user_i[first_loc, which(colnames(df_user_i) == "Planning")]))
    second_planning <- c(second_planning, filter_dividers(df_user_i[second_loc, which(colnames(df_user_i) == "Planning")]))
    
    # "Information Management Strategies"
    first_Information_Management_Strategies <- c(first_Information_Management_Strategies, filter_dividers(df_user_i[first_loc, which(colnames(df_user_i) == "Information Management Strategies")]))
    second_Information_Management_Strategies <- c(second_Information_Management_Strategies, filter_dividers(df_user_i[second_loc, which(colnames(df_user_i) == "Information Management Strategies")]))
    
    # "Comprehension Monitoring"
    first_Comprehension_Monitoring <- c(first_Comprehension_Monitoring, filter_dividers(df_user_i[first_loc, which(colnames(df_user_i) == "Comprehension Monitoring")]))
    second_Comprehension_Monitoring <- c(second_Comprehension_Monitoring, filter_dividers(df_user_i[second_loc, which(colnames(df_user_i) == "Comprehension Monitoring")]))
    
    # "Debugging Strategies"
    first_Debugging_Strategies <- c(first_Debugging_Strategies, filter_dividers(df_user_i[first_loc, which(colnames(df_user_i) == "Debugging Strategies")]))
    second_Debugging_Strategies <- c(second_Debugging_Strategies, filter_dividers(df_user_i[second_loc, which(colnames(df_user_i) == "Debugging Strategies")]))
    
    # "Evaluation"      
    first_Evaluation <- c(first_Evaluation, filter_dividers(df_user_i[first_loc, which(colnames(df_user_i) == "Evaluation")]))
    second_Evaluation <- c(second_Evaluation, filter_dividers(df_user_i[second_loc, which(colnames(df_user_i) == "Evaluation")]))
    
    # "MNA mini"
    first_MNA_mini <- c(first_MNA_mini, filter_dividers(df_user_i[first_loc, which(colnames(df_user_i) == "Nestlé Mini Nutritional Assessment MNA ®")]))
    second_MNA_mini <- c(second_MNA_mini, filter_dividers(df_user_i[second_loc, which(colnames(df_user_i) == "Nestlé Mini Nutritional Assessment MNA ®")]))
    
  }else if(procedencia[i] == 'APSS'){
    
    
    df_user_i <- df_APSS_assessments_[which(df_APSS_assessments_$`ITAID Partecipant` == user_id[i]), ]
    
    # assessment dates
    dates_user_i = as.Date(df_user_i$Date)
    
    
    first_loc <- which.min(dates_user_i)
    second_loc <- which.max(dates_user_i)
    # Date
    
    first_assessment_date = c(first_assessment_date, as.character(dates_user_i[first_loc]))
    second_assessment_date = c(second_assessment_date, as.character(dates_user_i[second_loc]))
    
    # weight
    
    first_weight <- c(first_weight, NA)
    second_weight <- c(second_weight, NA)
    
    # "Height"
    first_height <- c(first_height, NA)
    second_height <- c(second_height, NA)
    
    
    # "BMI"
    first_BMI <- c(first_BMI, NA)
    second_BMI <- c(second_BMI, NA)
    
    # "Chair Stand"
    
    first_chair_stand <- c(first_chair_stand, df_user_i[first_loc, which(colnames(df_user_i) == "Chair Stand (volte in 30 secondi)")])
    second_chair_stand <- c(second_chair_stand, df_user_i[second_loc, which(colnames(df_user_i) == "Chair Stand (volte in 30 secondi)")])
    
    
    # "Arm Curl"
    
    first_arm_curl <- c(first_arm_curl, df_user_i[first_loc, which(colnames(df_user_i) == "Arm Curl (volte in 30 secondi)")])
    second_arm_curl <- c(second_arm_curl, df_user_i[second_loc, which(colnames(df_user_i) == "Arm Curl (volte in 30 secondi)")])    
    
    # "Two Minute Step"
    first_two_minute_step <- c(first_two_minute_step, df_user_i[first_loc, which(colnames(df_user_i) == "Two Minute Step (numero di steps)")])
    second_two_minute_step <- c(second_two_minute_step, df_user_i[second_loc, which(colnames(df_user_i) == "Two Minute Step (numero di steps)")])
    
    # "Chair Sit and Reach 1"
    first_chair_sit_and_reach1 <- c(first_chair_sit_and_reach1, inch_to_cm(df_user_i[first_loc, which(colnames(df_user_i) == "Chair Sit & Reach (approssimato al 1/2 pollice) prova 1")]))
    second_chair_sit_and_reach1 <- c(second_chair_sit_and_reach1, inch_to_cm(df_user_i[second_loc, which(colnames(df_user_i) == "Chair Sit & Reach (approssimato al 1/2 pollice) prova 1")]))
    
    # "Chair Sit and Reach 2"
    first_chair_sit_and_reach2 <- c(first_chair_sit_and_reach2, inch_to_cm(df_user_i[first_loc, which(colnames(df_user_i) == "Chair Sit & Reach (approssimato al 1/2 pollice) prova 2")]))
    second_chair_sit_and_reach2 <- c(second_chair_sit_and_reach2, inch_to_cm(df_user_i[second_loc, which(colnames(df_user_i) == "Chair Sit & Reach (approssimato al 1/2 pollice) prova 2")]))
    
    # "Back Scratch 1"
    first_back_scratch_1 <- c(first_back_scratch_1, inch_to_cm(df_user_i[first_loc, which(colnames(df_user_i) == "Back Stretch (approssimato al 1/2 pollice) prova 1")]))
    second_back_scratch_1 <- c(second_back_scratch_1, inch_to_cm(df_user_i[second_loc, which(colnames(df_user_i) == "Back Stretch (approssimato al 1/2 pollice) prova 1")]))
    
    # "Back Scratch 2"
    first_back_scratch_2 <- c(first_back_scratch_2, inch_to_cm(df_user_i[first_loc, which(colnames(df_user_i) == "Back Stretch (approssimato al 1/2 pollice) prova 2")]))
    second_back_scratch_2 <- c(second_back_scratch_2, inch_to_cm(df_user_i[second_loc, which(colnames(df_user_i) == "Back Stretch (approssimato al 1/2 pollice) prova 2")]))
    
    # "Foot Up And Go 1"
    first_foot_up_and_go_1 <- c(first_foot_up_and_go_1, df_user_i[first_loc, which(colnames(df_user_i) == "Foot Up-and-Go (approssimato a 1/10 di secondo) prova 1")])
    second_foot_up_and_go_1 <- c(second_foot_up_and_go_1, df_user_i[second_loc, which(colnames(df_user_i) == "Foot Up-and-Go (approssimato a 1/10 di secondo) prova 1")])
    
    
    # "Foot Up And Go 2"
    first_foot_up_and_go_2 <- c(first_foot_up_and_go_2, df_user_i[first_loc, which(colnames(df_user_i) == "Foot Up-and-Go (approssimato a 1/10 di secondo) prova 2")])
    second_foot_up_and_go_2 <- c(second_foot_up_and_go_2, df_user_i[second_loc, which(colnames(df_user_i) == "Foot Up-and-Go (approssimato a 1/10 di secondo) prova 2")])
    
    
    # "MoCA" 
    
    first_MOCA <- c(first_MOCA, df_user_i[first_loc, which(colnames(df_user_i) == "Montreal cognitive assessment (MOCA)")])
    second_MOCA <- c(second_MOCA, df_user_i[second_loc, which(colnames(df_user_i) == "Montreal cognitive assessment (MOCA)")])
    
    # "MSC - A"
    first_MSC <- c(first_MSC, df_user_i[first_loc, which(colnames(df_user_i) == "Memory complaint scale (MCS) VERSION A. Punteggio")])
    second_MSC <- c(second_MSC, df_user_i[second_loc, which(colnames(df_user_i) == "Memory complaint scale (MCS) VERSION A. Punteggio")])
    
    # "Declarative Knowledge"
    first_declarative_knowledge <- c(first_declarative_knowledge, df_user_i[first_loc, which(colnames(df_user_i) == "DECLARATIVE KNOWLEDGE")])
    second_declarative_knowledge <- c(second_declarative_knowledge, df_user_i[second_loc, which(colnames(df_user_i) == "DECLARATIVE KNOWLEDGE")])
    
    # "Procedural Knowledge"  
    first_procedural_knowledge <- c(first_procedural_knowledge, df_user_i[first_loc, which(colnames(df_user_i) == "PROCEDURAL KNOWLEDGE")])
    second_procedural_knowledge <- c(second_procedural_knowledge, df_user_i[second_loc, which(colnames(df_user_i) == "PROCEDURAL KNOWLEDGE")])
    
    # "Conditional Knowledge"
    first_conditional_knowledge <- c(first_conditional_knowledge, df_user_i[first_loc, which(colnames(df_user_i) == "CONDITIONAL KNOWLEDGE")])
    second_conditional_knowledge <- c(second_conditional_knowledge, df_user_i[second_loc, which(colnames(df_user_i) == "CONDITIONAL KNOWLEDGE")])
    
    # "Planning"
    first_planning <- c(first_planning, df_user_i[first_loc, which(colnames(df_user_i) == "PLANNING")])
    second_planning <- c(second_planning, df_user_i[second_loc, which(colnames(df_user_i) == "PLANNING")])
    
    # "Information Management Strategies"
    first_Information_Management_Strategies <- c(first_Information_Management_Strategies, df_user_i[first_loc, which(colnames(df_user_i) == "INFORMATION MANAGEMENT STRATEGIES")])
    second_Information_Management_Strategies <- c(second_Information_Management_Strategies, df_user_i[second_loc, which(colnames(df_user_i) == "INFORMATION MANAGEMENT STRATEGIES")])
    
    # "Comprehension Monitoring"
    first_Comprehension_Monitoring <- c(first_Comprehension_Monitoring, df_user_i[first_loc, which(colnames(df_user_i) == "COMPREHENSION MONITORING")])
    second_Comprehension_Monitoring <- c(second_Comprehension_Monitoring, df_user_i[second_loc, which(colnames(df_user_i) == "COMPREHENSION MONITORING")])
    
    # "Debugging Strategies"
    first_Debugging_Strategies <- c(first_Debugging_Strategies, df_user_i[first_loc, which(colnames(df_user_i) == "DEBUGGING STRATEGIES")])
    second_Debugging_Strategies <- c(second_Debugging_Strategies, df_user_i[second_loc, which(colnames(df_user_i) == "DEBUGGING STRATEGIES")])
    
    # "Evaluation"      
    first_Evaluation <- c(first_Evaluation, df_user_i[first_loc, which(colnames(df_user_i) == "EVALUATION")])
    second_Evaluation <- c(second_Evaluation, df_user_i[second_loc, which(colnames(df_user_i) == "EVALUATION")])
    
    # "MNA mini"
    first_MNA_mini <- c(first_MNA_mini, df_user_i[first_loc, which(colnames(df_user_i) == "Nestlé Mini Nutritional Assessment MNA ®")])
    second_MNA_mini <- c(second_MNA_mini, df_user_i[second_loc, which(colnames(df_user_i) == "Nestlé Mini Nutritional Assessment MNA ®")])
    
    
  }else if(procedencia[i] == 'MAY'){
    
    df_user_i <- df_MAYNOOTH_assessments[which(df_MAYNOOTH_assessments["﻿User ID"] == user_id[i]), ]
    
    # Date
    first_assessment <- df_user_i[,1:63]
    second_assessment <- df_user_i[,64:length(colnames(df_user_i))]
    
    first_assessment_date = c(first_assessment_date, as.character(first_assessment$Date))
    second_assessment_date = c(second_assessment_date, as.character(as.Date(second_assessment$Date, format="%d/%m/%Y")))
    
    # weight
    
    first_weight <- c(first_weight, first_assessment$Weight)
    second_weight <- c(second_weight, second_assessment$Weight)
    
    # "Height"
    first_height <- c(first_height, first_assessment$Height)
    second_height <- c(second_height, second_assessment$Height)
    
    
    # "BMI"
    first_BMI <- c(first_BMI, first_assessment$Weight/(first_assessment$Height/100)**2)
    second_BMI <- c(second_BMI, second_assessment$Weight/(second_assessment$Height/100)**2)
    
    # "Chair Stand"
    
    first_chair_stand <- c(first_chair_stand, first_assessment$`Fullerton - Chair Stand`)
    second_chair_stand <- c(second_chair_stand, second_assessment$`Fullerton - Chair Stand`)
    
    
    # "Arm Curl"
    
    first_arm_curl <- c(first_arm_curl, first_assessment$`Fullerton - Arm Curl`)
    second_arm_curl <- c(second_arm_curl, second_assessment$`Fullerton - Arm Curl`)    
    
    # "Two Minute Step"
    first_two_minute_step <- c(first_two_minute_step, first_assessment$`Fullerton - 2 Minute Step`)
    second_two_minute_step <- c(second_two_minute_step, second_assessment$`Fullerton - 2 Minute Step`)
    
    # "Chair Sit and Reach 1"
    first_chair_sit_and_reach1 <- c(first_chair_sit_and_reach1, inch_to_cm(first_assessment$`Fullerton - Chair Sit and Reach Trial 1`))
    second_chair_sit_and_reach1 <- c(second_chair_sit_and_reach1, inch_to_cm(second_assessment$`Fullerton - Chair Sit and Reach Trial 1`))
    #marka
    # "Chair Sit and Reach 2"
    first_chair_sit_and_reach2 <- c(first_chair_sit_and_reach2, inch_to_cm(first_assessment$`Fullerton - Chair Sit and Reach Trial 2`))
    second_chair_sit_and_reach2 <- c(second_chair_sit_and_reach2, inch_to_cm(second_assessment$`Fullerton - Chair Sit and Reach Trial 2`))
    
    # "Back Scratch 1"
    first_back_scratch_1 <- c(first_back_scratch_1, inch_to_cm(first_assessment$`Fullerton - Back Stretch Trial 1`))
    second_back_scratch_1 <- c(second_back_scratch_1, inch_to_cm(second_assessment$`Fullerton - Back Stretch Trial 1`))
    
    # "Back Scratch 2"
    first_back_scratch_2 <- c(first_back_scratch_2, inch_to_cm(first_assessment$`Fullerton - Back Stretch Trial 2`))
    second_back_scratch_2 <- c(second_back_scratch_2, inch_to_cm(second_assessment$`Fullerton - Back Stretch Trial 2`))
    
    # "Foot Up And Go 1"
    first_foot_up_and_go_1 <- c(first_foot_up_and_go_1, first_assessment$`Fullerton - Foot up and go trial 1`) 
    second_foot_up_and_go_1 <- c(second_foot_up_and_go_1, second_assessment$`Fullerton - Foot up and go trial 1`)
    
    
    # "Foot Up And Go 2"
    first_foot_up_and_go_2 <- c(first_foot_up_and_go_2, first_assessment$`Fullerton - Foot up and go trial 2`)
    second_foot_up_and_go_2 <- c(second_foot_up_and_go_2, second_assessment$`Fullerton - Foot up and go trial 2`)
    
    
    # "MoCA" 
    
    first_MOCA <- c(first_MOCA, first_assessment$`MOCA - total pre`)
    second_MOCA <- c(second_MOCA, second_assessment$`MOCA - total post`)
    
    # "MSC - A"
    first_MSC <- c(first_MSC, first_assessment$`MCS - total pre`)
    second_MSC <- c(second_MSC, second_assessment$`MCS - total post`)
    
    # "Declarative Knowledge"
    first_declarative_knowledge <- c(first_declarative_knowledge, first_assessment$`MAI - Declarative`)
    second_declarative_knowledge <- c(second_declarative_knowledge, second_assessment$`MAI - Declarative`)
    
    # "Procedural Knowledge"  
    first_procedural_knowledge <- c(first_procedural_knowledge, first_assessment$`MAI - Procedural`)
    second_procedural_knowledge <- c(second_procedural_knowledge, second_assessment$`MAI - Procedural`)
    
    # "Conditional Knowledge"
    first_conditional_knowledge <- c(first_conditional_knowledge, first_assessment$`MAI - Conditional`)
    second_conditional_knowledge <- c(second_conditional_knowledge, second_assessment$`MAI - Conditional`)
    
    # "Planning"
    first_planning <- c(first_planning, first_assessment$`MAI - Planning`)
    second_planning <- c(second_planning, second_assessment$`MAI - Planning`)
    
    # "Information Management Strategies"
    first_Information_Management_Strategies <- c(first_Information_Management_Strategies, first_assessment$`MAI - Information Management Strategies`)
    second_Information_Management_Strategies <- c(second_Information_Management_Strategies, second_assessment$`MAI - Information Management Strategies`)
    
    # "Comprehension Monitoring"
    first_Comprehension_Monitoring <- c(first_Comprehension_Monitoring, first_assessment$`MAI - Comprehension Monitoring`)
    second_Comprehension_Monitoring <- c(second_Comprehension_Monitoring, second_assessment$`MAI - Composthension Monitoring`)
    
    # "Debugging Strategies"
    first_Debugging_Strategies <- c(first_Debugging_Strategies, first_assessment$`MAI - Debugging Strategies`)
    second_Debugging_Strategies <- c(second_Debugging_Strategies, second_assessment$`MAI - Debugging Strategies`)
    
    # "Evaluation"      
    first_Evaluation <- c(first_Evaluation, first_assessment$`MAI - Evaluation`)
    second_Evaluation <- c(second_Evaluation, second_assessment$`MAI - Evaluation`)
    
    # "MNA mini"
    first_MNA_mini <- c(first_MNA_mini, first_assessment$`Nutrition - MNA`)
    second_MNA_mini <- c(second_MNA_mini, second_assessment$`Nutrition - MNA - post`)
    
  }else{
    print("WTF!!")
  }
}


df_first_assessment = data.frame(
  list(
    'user' = user_id,
    'assessment_date' = first_assessment_date,
    'weight' = first_weight,
    'height' = first_height,
    'BMI' = first_BMI,
    'chair_stand' = first_chair_stand,
    'arm_curl' = first_arm_curl,
    'two_minute_step' = first_two_minute_step,
    'chair_sit_and_reach1' = first_chair_sit_and_reach1,
    'chair_sit_and_reach2' = first_chair_sit_and_reach2,
    'back_scratch_1' = first_back_scratch_1,
    'back_scratch_2' = first_back_scratch_2,
    'foot_up_and_go_1' = first_foot_up_and_go_1,
    'foot_up_and_go_2' = first_foot_up_and_go_2,
    'MOCA' = first_MOCA,
    'MSC' = first_MSC,
    'declarative_knowledge' = first_declarative_knowledge,
    'procedural_knowledge' = first_procedural_knowledge,
    'conditional_knowledge' = first_conditional_knowledge,
    'planning' = first_planning,
    'Information_Management_Strategies' = first_Information_Management_Strategies,
    'Comprehension_Monitoring' = first_Comprehension_Monitoring,
    'Debugging_Strategies' = first_Debugging_Strategies,
    'Evaluation' = first_Evaluation,
    'MNA_mini' = first_MNA_mini,
    'dataset_source' = procedencia
    )
  )

write.csv(df_first_assessment, 'C:/Users/jkerexeta/Documents/PROIEKTUK/CAPTAIN/interactive-clustering/preprocess/df_first_assessment.csv')
df_second_assessment = data.frame(
  list(
    'user' = user_id,
    'assessment_date' = second_assessment_date,
    'weight' = second_weight,
    'height' = second_height,
    'BMI' = second_BMI,
    'chair_stand' = second_chair_stand,
    'arm_curl' = second_arm_curl,
    'two_minute_step' = second_two_minute_step,
    'chair_sit_and_reach1' = second_chair_sit_and_reach1,
    'chair_sit_and_reach2' = second_chair_sit_and_reach2,
    'back_scratch_1' = second_back_scratch_1,
    'back_scratch_2' = second_back_scratch_2,
    'foot_up_and_go_1' = second_foot_up_and_go_1,
    'foot_up_and_go_2' = second_foot_up_and_go_2,
    'MOCA' = second_MOCA,
    'MSC' = second_MSC,
    'declarative_knowledge' = second_declarative_knowledge,
    'procedural_knowledge' = second_procedural_knowledge,
    'conditional_knowledge' = second_conditional_knowledge,
    'planning' = second_planning,
    'Information_Management_Strategies' = second_Information_Management_Strategies,
    'Comprehension_Monitoring' = second_Comprehension_Monitoring,
    'Debugging_Strategies' = second_Debugging_Strategies,
    'Evaluation' = second_Evaluation,
    'MNA_mini' = second_MNA_mini,
    'dataset_source' = procedencia
    )
)
write.csv(df_second_assessment, 'C:/Users/jkerexeta/Documents/PROIEKTUK/CAPTAIN/interactive-clustering/preprocess/df_second_assessment.csv')

