import json

# Load the notebook
with open('Shona_Tokenizer.ipynb', 'r') as f:
    notebook = json.load(f)

# Option 1: Remove metadata.widgets entirely
if 'widgets' in notebook.get('metadata', {}):
    del notebook['metadata']['widgets']

# Option 2: Add 'state' to each widget (if you prefer to keep widgets)
# if 'widgets' in notebook.get('metadata', {}):
#     for widget in notebook['metadata']['widgets'].values():
#         if 'state' not in widget:
#             widget['state'] = {}

# Save the fixed notebook
with open('Shona_Tokenizer_fixed.ipynb', 'w') as f:
    json.dump(notebook, f)