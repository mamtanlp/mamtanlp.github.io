import re

with open('_bibliography/papers.bib', 'r') as f:
    content = f.read()

def fix_preview(match):
    header = match.group(1) # @inproceedings{key,
    key = match.group(3)
    # the existing preview line is next: \n    preview = {inproceedings.png},
    return f"{header}\n    preview = {{{key}.gif}},"

# Replace the incorrect preview lines
new_content = re.sub(r'(@(inproceedings|article)\{([^,]+),)\n\s*preview\s*=\s*\{[^}]+\},', fix_preview, content)

with open('_bibliography/papers.bib', 'w') as f:
    f.write(new_content)

print("Fixed papers.bib")
