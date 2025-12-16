library(tidyverse)

df <- read.csv("data/raw/clients.csv")

df_clean <- df %>%
  mutate_if(is.character, as.factor) %>%
  drop_na()

write.csv(df_clean, "data/processed/clients_clean_R.csv", row.names = FALSE)
