import pandas as pd
# Input Excel File
df = pd.read_excel('C:\\Users\\Tanuj Gupta\\Desktop\\Web Scraping\\Book1.xlsx', sheet_name='Sheet1')

for index, row in df.iterrows():
    url = row['URL']
    words = row['Words'].split(',')

    # Performing Word Count
    word_counts = {}
    for word in words:
        word = word.strip().lower()
        count = 0

        if word in url.lower():
            count += 1

        word_counts[word] = count

    df.at[index, 'Word Counts'] = str(word_counts)

# Generating Output Excel File
df.to_excel('output.xlsx', index=False)
