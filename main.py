  #function isValid(stale, latest, otjson) {
#  // this is the part you will write!
#}
#
#isValid(
#  'Repl.it uses operational transformations to keep #everyone in a multiplayer repl in sync.',
#  'Repl.it uses operational transformations.',
#  '[{"op": "skip", "count": 40}, {"op": "delete", #"count": 47}]'
#); // true

def isValid(stale, latest, otjson):
  cursorPos = 0
  staleIndex = []
  print("Original string is: " + stale)
  for char in range(len(stale)):
    staleIndex.append(char)
  for op in otjson:
    #print("Original cursor pos: " + stale[cursorPos])
    if op["op"] == "skip":
      cursorPos = cursorPos + op["count"]
      if cursorPos > len(stale):
        print(False, "- Skipped past the end of the string")
    #  print(cursorPos)
    if op["op"] == "insert":
      stale = stale + op["chars"]
      finalStr = stale
      curserPos=stale[len(stale)-1]
      #print("Modified string is: '" + stale + "'")
    if op["op"] == "delete":
      left, right = stale[:cursorPos], stale[cursorPos:]
      count = (len(right) - op["count"])*-1
      right = right[count:]
      finalStr = left + right
  print("Modified string is: " + finalStr)
  print("Desired string is: " + latest)
  if cursorPos > len(finalStr):
    print(False, "- Skipped beyond the end of the string")
  elif latest == finalStr:
    print(True, "- Stale string is modified correctly")
    print("")
      
isValid("Repl.it uses operational transformations.", "Repl.it uses operational.", [{"op": "skip", "count": 24}, {"op": "delete", "count": 16}])

isValid("Test", "Test me", [{"op": "skip", "count": 4},{"op": "insert", "chars": " me"} ])

isValid("Repl.it uses operational transformations.", "Repl.it uses operational.", [{"op": "skip", "count": 24}, {"op": "delete", "count": 16}, {"op": "skip", "count": 2}])