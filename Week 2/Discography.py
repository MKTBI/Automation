import requests


url = 'https://en.wikipedia.org/wiki/Red_Hot_Chili_Peppers_discography'
response = requests.get(url)
html_content = response.text


start_index = html_content.find('Studio albums')
album_table_start_index = html_content.find('<table', start_index)
album_table_end_index = html_content.find('</table>', album_table_start_index)
album_table_html = html_content[album_table_start_index:album_table_end_index + 8]

if 'Studio albums' not in album_table_html:
    print('Could not find studio album table')
    exit()


album_title_start_index = album_table_html.find('<i>')
album_titles = []
while album_title_start_index != -1:
    album_title_end_index = album_table_html.find('</i>', album_title_start_index)
    album_title = album_table_html[album_title_start_index + 3:album_title_end_index]
    album_titles.append(album_title)
    album_title_start_index = album_table_html.find('<i>', album_title_end_index)


print('Studio album titles:')
for title in album_titles:
    print('- ' + title)
