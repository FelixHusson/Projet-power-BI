library(tidyverse)

df <- read.csv("data/processed/clients_clean_R.csv")

df$age_group <- ntile(df$age, 4)

write.csv(df, "data/processed/clients_engineered_R.csv", row.names = FALSE)
