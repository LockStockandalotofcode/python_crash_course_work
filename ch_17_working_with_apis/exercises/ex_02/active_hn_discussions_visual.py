from operator import itemgetter
import plotly.express as px
import requests

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
titles, comments, submission_dicts = [], [], []
for submission_id in submission_ids[:30]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    # print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    try:
        # build a dictionary for each article.
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    except KeyError:
        pass
    else:
        submission_dicts.append(submission_dict)
        comments.append(response_dict['descendants'])

        title = response_dict['title']
        link = submission_dict['hn_link']
        discussion_link = f"<a href='{link}'>{title}</a>"
        titles.append(discussion_link)
        # discussion_link = f"<a href='{url}'>{title}</a>"
        # hover_texts.append(discu)



submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Make visualization. Customising title, labels.
# Further customising, making discussion title clickable.
title = "Most Active Discussions currently happening on Hacker News"
labels = {'x': 'Discussion Title', 'y': 'Comments'}
fig = px.bar(x=titles, y=comments, title=title, labels=labels)

# Updating layout, marker, 
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()