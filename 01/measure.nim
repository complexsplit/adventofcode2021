var
  line = ""

proc readDepths() =
  let f = open("01/input.txt")
  # Close the file object when you are done with it
  defer: f.close()

  while f.readLine(line):
    echo line

  # let firstLine = f.readLine()
  # echo firstLine  # prints Spitfire

readDepths()

