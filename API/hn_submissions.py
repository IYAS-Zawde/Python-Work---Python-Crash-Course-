import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS, LightStyle as LS
# Make an API call and store the respose.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
response = requests.get(url)
print("Status Code:", response.status_code)

# Process information about each submission
submission_ids = response.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_response = requests.get(url)
    #print("Status Code:", submission_response.status_code)
    response_dict = submission_response.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'https://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
    }

    submission_dicts.append(submission_dict)

submission_dicts.sort(key=itemgetter('comments'), reverse=True)
plot_dicts = []
for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion Link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])
    plot_dicts.append({
        'label': submission_dict['title'],
        'value': submission_dict['comments'],
        'xlink': submission_dict['link']
    })


# Visualizing the data
titles = [x['title'] for x in submission_dicts]

my_style = LS(color='#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truck_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.x_labels = titles
chart.add('', plot_dicts)
chart.render_to_file('hn_submissions.svg')