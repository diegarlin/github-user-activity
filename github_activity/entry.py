import argparse
import requests
import json

def cli_entry_point():
    parser = argparse.ArgumentParser(description='A simple github user activity program')
    
    parser.add_argument('username', help='The username you want to get the activity')
    
    args = parser.parse_args()
    
    handle_activity(args.username)
    
    
def handle_activity(username):
    activity = requests.get(f'https://api.github.com/users/{username}/events')
    if(activity.status_code == 404):
        print(f'This user doesnt exist.')
    else:
        json = activity.json()
        push_event_count = 0
        pull_request_event_count = 0
        pull_request_review_count = 0
        issues_event_count = 0 
        rest_events_count = 0
        print('-------------------------------------------------------------')
        print('COMMIT MESSAGES')
        print('-------------------------------------------------------------')
        for event in json:
            if(event['type'] == 'PushEvent'):    
                message = event['payload']['commits'][0]['message']
                print(f'- {message} \n')
            if event['type'] == 'PushEvent':
                push_event_count += 1
            elif event['type'] == 'PullRequestEvent':
                pull_request_event_count += 1
            elif event['type'] == 'PullRequestReviewEvent':
                pull_request_review_count += 1
            elif event['type'] == 'IssuesEvent':
                issues_event_count += 1
            else:
                rest_events_count += 1
                
        print('-------------------------------------------------------------')
        print('EVENTS COUNT')
        print('-------------------------------------------------------------')
        
        print(f'Push events: {push_event_count}\n')
        print(f'Pull request events: {pull_request_event_count}\n')
        print(f'Pull request reviews: {pull_request_review_count}\n')
        print(f'Issues events: {issues_event_count}\n')
        print(f'The rest: {rest_events_count}\n')
        
            
    
    
            
