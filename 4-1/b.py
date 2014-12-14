samples = {"Name1": "Address1", "Name2": "Address2", "Name3": "Address3"}

with open("newfile.txt", "w+") as f:
  for s in samples:
    f.write(str(s) + ", " + str(samples[s]) + '\n')
