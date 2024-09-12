with open("Algebre-Notes.tex", "r") as f:
    lines = f.readlines()
    lines.insert(4, "\\usepackage{fontspec}\n")
    lines.insert(5, "\\setmainfont{OpenDyslexic}\n")
with open("Algebre-Notes-dyslexia.tex", "w") as f:
    f.writelines(lines)
