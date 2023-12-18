# prepend = '>'

with open('input.txt', 'r') as caldoc:
  caldoc = caldoc.readlines()

  nummap = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
  }
  
  sum = 0
  for entry in caldoc:
    entry = entry.strip()
    entry_map = {}
    last_start = ""
    last_end = None
    for strnum in nummap:
      current_start = entry.find(strnum)
      current_end = (len(strnum) - 1) + current_start

      if current_start != -1:
        if current_end in entry_map:
          # print(prepend, "is final index", current_end, 'for entry "' + strnum + '" from "' + entry + '" in the beginning index history for word numbers in "' + entry + '"?')
          if str(current_end) in last_start:
            # print(prepend, "yes,", current_end, 'is in "' + entry + '" beginning index history: ' + str(last_start.split()))
            # print(prepend, 'thus, delete "' + entry_map[current_end] + '" at', current_end,'in', entry_map)
            del entry_map[current_end]
        else:
          if last_end == current_start:
            last_end = current_end
            last_start += str(current_start)
            continue

        entry_map[current_start] = strnum
        # print(prepend, '"' + strnum + '" has been added at', current_start)
        last_end = current_end
        last_start += str(current_start)

    # print(prepend, "locations of number words:", entry_map)
    
    chrnum = 0
    numstr = ''
    while chrnum < len(entry):
      if ord(entry[chrnum]) > 47 and ord(entry[chrnum]) < 58:
        # print(prepend, 'unicode number codepoint detected, placing "' + entry[chrnum] + '" into "' + numstr + '"')
        numstr += entry[chrnum]
      else:
        if chrnum in entry_map:
          # print(prepend, 'unicode non-number codepoint detected, using "' + str(chrnum) + '" for', entry_map, 'selection')
          # print(prepend, 'using selection "' + entry_map[chrnum] + '" for', nummap, 'selection')
          # print(prepend, 'placing "' + nummap[entry_map[chrnum]] + '" into "' + numstr + '"')
          numstr += nummap[entry_map[chrnum]]

      chrnum += 1

    # print("resulting number:", numstr)
    # print(prepend, 'adding', numstr[0] + numstr[-1], "to previous sum,", sum)
    print(sum)
    sum += int(numstr[0] + numstr[-1])
    print('+', numstr[0] + numstr[-1], '=', sum)
  print(sum)

