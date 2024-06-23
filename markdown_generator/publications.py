import os
import pandas as pd

# Load publications from TSV
publications = pd.read_csv('publications.tsv', sep='\t')

# Path to markdown files
markdown_path = './_portfolio/'

# Generate markdown files for each publication
for index, row in publications.iterrows():
    file_name = os.path.join(markdown_path, f"{row['date']}-{row['slug']}.md")
    with open(file_name, 'w') as f:
        f.write(f"---\n")
        f.write(f"title: \"{row['title']}\"\n")
        f.write(f"date: {row['date']}\n")
        f.write(f"---\n\n")
        f.write(f"{row['citation']}\n")

print("Markdown files generated successfully.")
