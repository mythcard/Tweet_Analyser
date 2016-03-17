### reference : http://www.r-bloggers.com/downloading-your-twitter-feed-in-r/
library(twitteR)
library(twitteR)

#api_key <- "KX6Beg3VxCOtnA4KAdshln1Tg"
#api_secret <- "1d0oO62SOWexLyWxdVUmexDDekvzRMaiWvoeG3buXakv5B86Uh"
#access_token <- "338469652-iCWF35QG43qWi68kvmlj2EbmEkgMHnQ9bWAUfJ6n"
#access_token_secret <- "dRXudaJplifrqQndUpK4LJ1IT6tJuH0dFhuJTKXRzsY2G"
 
#setup_twitter_oauth(api_key,api_secret,access_token,access_token_secret)

timeLine <- homeTimeline(n = 100, retryOnRateLimit = 1000)

timeLineTweetsDF <- twListToDF(timeLine)

path <- c("D:/Data Mining/Class_Spring_2016/Tweet_Analysis/my_solution")

x_date <- Sys.Date()

x_time <- Sys.time()

type123 <- c(".csv")

file123 <-paste(c(path, x_date, x_time, type123), collapse = "")

write.csv(timeLineTweetsDF, file = file123, row.names = FALSE) 