
# Part 1
aoc_3 <- read.table("~/Desktop/aoc_3.txt")
aoc_3$first <- str_sub(aoc_3$V1, start = 1, end = nchar(aoc_3$V1)/2)
aoc_3$second <- str_sub(aoc_3$V1, start = (nchar(aoc_3$V1)/2) + 1, end = nchar(aoc_3$V1))

# Vectors of letters and points
lower <- letters[seq(from = 1, to = 26)]
lower_points <- seq(1:26)
upper <- LETTERS[seq(from = 1, to = 26)]
upper_points <- seq(from = 27, to = 52)

# Function to find match and compute points
find_match <- function(string1_split, string2_split) {
  item <- intersect(string1_split, string2_split)
  points <- c()
  for (i in 1:length(item)) {
    points[i] <- sum(na.omit(lower_points[match(item[i], lower)])) + 
      sum(na.omit(upper_points[match(item[i], upper)]))
  }
  return(sum(points))
}

sum(apply(aoc_3, 1, function(row) find_match(unlist(strsplit(row[2], "")), 
                                             unlist(strsplit(row[3], "")))))

# Part 2
aoc_3 <- read.table("~/Desktop/aoc_3.2.txt")
for (i in seq(1, nrow(aoc_3), 3)){
  aoc_3$V2[i] <- aoc_3$V1[i + 1]
  aoc_3$V3[i] <- aoc_3$V1[i + 2]
}
new_aoc_3 <- data.frame(aoc_3[seq(1, nrow(aoc_3), 3), ])

find_badge <- function(string1_split, string2_split, string3_split) {
  item <- intersect(intersect(string1_split, string2_split), string3_split)
  points <- c()
  for (i in 1:length(item)) {
    points[i] <- sum(na.omit(lower_points[match(item[i], lower)])) + 
      sum(na.omit(upper_points[match(item[i], upper)]))
  }
  return(sum(points))
}

sum(apply(new_aoc_3, 1, function(row) find_badge(unlist(strsplit(row[1], "")),
                                                 unlist(strsplit(row[2], "")),
                                                 unlist(strsplit(row[3], "")))))