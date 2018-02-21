
import os
import io

for root, dirs, fns in os.walk("."):
	for fn in fns:
		if fn.endswith(".md"):
			fullfn = os.path.join(root, fn)
			with io.open(fullfn, encoding="utf8") as fp:
				texts = []
				title = ""
				headsep = 0
				for line in fp:
					if line.startswith("---"):
						headsep += 1
					if headsep < 2:
						if ":" in line:
							kk, vv = line.split(":", 1)
							line = kk.strip() + ": " + vv.strip() + "\n"

							line = line[0].upper() + line[1:]
							if line[:5].lower() == "title":
								title = line
								continue

							if line[:4].lower() == "tags":
								line = line.replace("[", "").replace("]", "")

							line = line.replace("Update", "Modified")

					texts.append(line)

			with io.open(fullfn, "w", encoding="utf8") as fp:
				texts.insert(1, title)
				fp.write("".join(texts))



