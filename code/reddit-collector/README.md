# Reddit Collector - run.py
This program is design to collect all data from a subreddit and organize the
data by submissions, user comments. Below I will provide execution commands
as well as the output file format.

## Commands

**Subreddit:** `-s | --subreddit` will allow the user to select which subreddit
they want to extract data from
* Default: /r/all

**Limit:** `-l | --limit` will allow the user to select the amount of submissions
they want to retrieve.
* Default: None, which will retrieve all submissions

## Execution

```
python run.py --subreddit=catan -l=5
```

## Output

For a quick live data example please run the execution command above to retrieve a small
example file.

**Psuedo Output Format:**
```
{
  "subreddit_name": [
    {
      "submission_id": [
        {
          "submission_title": "...",
          "submission_text": "...",
          "submission_timestamp": "YYYY-MM-DD HH:mm:SS",
          "comments": [
            {
              "User_Name_1": [
                {
                    "comment_1_id": [
                      "comment_timestamp": "...",
                      "comment_text": ".." 
                    ],
                    "comment_2_id": [
                      "comment_timestamp": "...",
                      "comment_text": ".." 
                    ]
                }
              ],
              "User_Name_2": [
                {
                    "comment_1_id": [
                      "comment_timestamp": "...",
                      "comment_text": ".." 
                    ],
                    "comment_2_id": [
                      "comment_timestamp": "...",
                      "comment_text": ".." 
                    ]
                }
              ]
            }
           ]
         }
      ]
    }
  ]
}
```
# Reddit User Collector - reddit_user.py
This program is designed to pull comments and submissions from a(n) redditor(s). Below I will provide execution commands.

## Commands
**User** `-u | --user` allows the user to input the name(s) of the redditor(s) they want to pull information from. Default is None
**Limit** `-l | --limit` allows the user to input the max number of comments/submissions they want to pull. Default is None

## Execution

```
python reddit_user.py -u user1,user2 -l 20
```
The above command will attempt to pull up to 20 comments and 20 submissions for both redditor 'user1' and redditor 'user2'
