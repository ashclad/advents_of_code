# CURRENT GRADE: F

with open('input.txt', 'r') as caldoc:
  caldoc = caldoc.readlines()

  sum = 0
  for entry in caldoc:
    chrnum = 0
    numeral_opts = ''
    while chrnum < len(entry):
      if ord(entry[chrnum]) > 47 and ord(entry[chrnum]) < 58:
        numeral_opts += entry[chrnum]
      else:
        chrnum += 1
        continue
      chrnum += 1
    
    number = int(numeral_opts[0] + numeral_opts[-1])
    sum += number
  print(sum)
