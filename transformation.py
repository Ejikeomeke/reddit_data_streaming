#data transformation function
def transforming_data(raw_data):
    from datetime import datetime, date

    data_tranformed = []
    for post in raw_data['data']['children']:
        date_created = datetime.fromtimestamp(post['data']['created_utc']).date().strftime("%Y-%m-%d %H:%M:%S")[0:11]
        time_created = datetime.fromtimestamp(post['data']['created_utc']).time().strftime("%Y-%m-%d %H:%M:%S")[11:-1]
        subtitle = post['data']['subreddit']
        post_id =post['kind']+'_'+post['data']['id']
        post_title = post['data']['title']
        text = post['data']['selftext']
        up_vote = post['data']['ups']
        down_vote = post['data']['downs']
        score = post['data']['score']
        
        data_tranformed.append({
            
            'post_id':post_id,
            'post_title':post_title,
            'subtitle':subtitle,
            'text':text,
            'date_created':date_created,
            'time_created':time_created,
            'up_vote':up_vote,
            'down_vote':down_vote,
            'score':score
        })
        
    
    return data_tranformed


