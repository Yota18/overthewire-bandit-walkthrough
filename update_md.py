import re

files_mapping = {
    "Bandit_Walkthrough_Part1.md": list(range(0, 11)),  # 0 to 10
    "Bandit_Walkthrough_Part2.md": list(range(11, 21)), # 11 to 20
    "Bandit_Walkthrough_Part3.md": list(range(21, 32))  # 21 to 31
}

for filename, levels in files_mapping.items():
    try:
        with open(filename, "r") as f:
            content = f.read()
        
        # Special case for Level 0 -> 1 (mapped to "bandit0_step.png")
        if 0 in levels:
            content = content.replace("## Level 0 -> 1", "## Level 0 -> 1\n\n![Level 0 Output](bandit0_step.png)")
            
        for i in levels:
            if i == 0: continue # Handled above
            header = f"## Level {i} -> {i+1}"
            image = f"![Level {i} Output](bandit{i}_step.png)"
            if header in content:
                content = content.replace(header, f"{header}\n\n{image}")
            else:
                pass # print(f"Warning: Header '{header}' not found in {filename}")

        with open(filename, "w") as f:
            f.write(content)
        print(f"Updated {filename}")
        
    except FileNotFoundError:
        print(f"File {filename} not found, skipping.")

print("Done updating parts.")
