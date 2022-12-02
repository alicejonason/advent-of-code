aoc_1 <- read.table("~/Desktop/aoc_1.txt", blank.lines.skip = FALSE)

person <- 0
j <- 0
for (i in 1:nrow(aoc_1)) {
  if (is.na(aoc_1[i, 1]) == FALSE) {
    person <- person + aoc_1[i, 1]
  }
  else {
    j <- j + 1
    calorie_vector[j] <- person
    person <- 0
  }
}
max(calorie_vector)
sum(sort(calorie_vector, decreasing = TRUE)[1:3])