aoc_2 <- read.table("~/Desktop/aoc_2.txt")
aoc_2$V2 <- ifelse(aoc_2$V2 == "X", "A", ifelse(aoc_2$V2 == "Y", "B", "C"))

rps <- function(input1, input2) {
  points <- ifelse(input2 == "A", 1, ifelse(input2 == "B", 2, 3))
  score <- ifelse(input1 == input2, 3, 
                  ifelse(input2 == "A" & input1 == "C" |
                           input2 == "C" & input1 == "B" |
                            input2 == "B" & input1 == "A", 6, 0))
  return(points + score)
}
sum(rps(aoc_2$V1, aoc_2$V2))

move <- function(input1, input2) {
  if (input2 == "B") {
    return(input1)
  }
  return(ifelse(input1 == "A" & input2 == "A" | input1 == "B" & input2 == "C", "C", 
         ifelse(input1 == "A" & input2 == "C" | input1 == "C" & input2 == "A", "B", "A")))
}
aoc_2$new_move <- apply(aoc_2, 1, function(row) move(row[1], row[2]))
sum(apply(aoc_2, 1, function(row) rps(row[1], row[3])))