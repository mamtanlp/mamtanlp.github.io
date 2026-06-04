import os

filepath = '_bibliography/papers.bib'
with open(filepath, 'r') as f:
    content = f.read()

replacements = {
    "https://aclanthology.org/2026.findings-acl.tinyattack.pdf": "https://kclpure.kcl.ac.uk/ws/portalfiles/portal/371696857/TinyAttack_ACL26.pdf",
    "https://dl.acm.org/doi/pdf/10.1145/3664647.3681668": "https://dl.acm.org/doi/10.1145/3664647.3681703",
    "https://ieeexplore.ieee.org/document/10587087": "https://ieeexplore.ieee.org/document/10722034",
    "https://www.sciencedirect.com/science/article/pii/S0885230824000792": "https://dl.acm.org/doi/10.1016/j.csl.2024.101668",
    "https://ieeexplore.ieee.org/document/10440432": "https://ieeexplore.ieee.org/document/10483106",
    "https://link.springer.com/article/10.1007/s10844-023-00789-8": "https://link.springer.com/article/10.1007/s10844-023-00808-x",
    "pdf={https://aclanthology.org/2022.findings-aacl.40.pdf}": "html={https://aclanthology.org/2022.findings-aacl.44/}",
    "https://dl.acm.org/doi/10.1145/3505244": "https://dl.acm.org/doi/10.1145/3514498",
    "https://aclanthology.org/2022.lrec-1.761.pdf": "https://aclanthology.org/2022.lrec-1.764.pdf",
    "pdf={https://aclanthology.org/2020.lrec-1.620.pdf}": "html={https://aclanthology.org/2020.lrec-1.621/}",
    "https://aclanthology.org/2020.icon-main.51.pdf": "https://aclanthology.org/2020.icon-main.60.pdf"
}

for old_str, new_str in replacements.items():
    if old_str in content:
        content = content.replace(old_str, new_str)
        print(f"Replaced: {old_str}")
    else:
        print(f"NOT FOUND: {old_str}")

with open(filepath, 'w') as f:
    f.write(content)

