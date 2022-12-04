[![Data Engineering API](https://github.com/nogibjj/DE_Microservice/actions/workflows/cicd.yml/badge.svg?branch=main)](https://github.com/nogibjj/DE_Microservice/actions/workflows/cicd.yml)
# DE_Microservice
This is the repo for the 706 final project.

Members: Boyi Wang (bw224), Qiheng Gao (qg45), Yutong Zhang (yz566), Zilin Yin (zy108)
<br>

### "tiktok_video" Table Description:

| Column name | Description                                                          |
|-------------|----------------------------------------------------------------------|
| user_name   | The name of the user who posted the video. (String)                  |
| user_id     | The id of the user who posted the video. (Integer)                   |
| video_id    | The id of the posted video. (Integer)                                |
| video_desc  | The description of the posted video. (String)                        |
| video_time  | The posted time of the video. (Integer)                              |
| video_length| The length of the posted video. (Integer)                            |
| video_link  | The link of the posted video. (String)                               |
| n_likes     | The number of likes the video has received. (Integer)                |
| n_shares    | The number of shares the video has received. (Integer)               |
| n_comments  | The number of comments the video has received. (Integer)             |
| n_plays     | The number of times the video has been played. (Integer) expand_less |
<br>

### Sample SQL Queries:

1.. Find all videos of certain user:

```
SELECT * FROM tiktok_video WHERE user_name = <user_name>;
```

2.. Identifying popular TikTok authors to target for scraping videos and liked videos:

```
SELECT user_id, user_name FROM tiktok_video WHERE n_likes > <n_likes> OR n_shares > <n_shares> OR n_comments > <n_comments> OR n_plays > <n_plays>;
```

3.. Finding trending videos on TikTok for further analysis:

```
SELECT video_id, video_desc, video_time, video_length, video_link FROM tiktok_video WHERE n_likes > <n_likes> OR n_shares > <n_shares> OR n_comments > <n_comments> OR n_plays > <n_plays>;
```

4.. Generating a list of videos from the TikTok app that are tagged with the #funny hashtag:

```
SELECT video_id, video_link FROM tiktok_video WHERE video_desc LIKE '#funny';
```