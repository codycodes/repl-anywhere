import sys

original_text = sys.argv[1]
text_to_replace = sys.argv[2]
replacement_text = sys.argv[3]

print(original_text.replace(text_to_replace, replacement_text))