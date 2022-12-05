"""Module csv provide tools to read in csv file"""
import csv
import sqlite3


def db_setup():
    """Set up table and return cursor"""
    conn = sqlite3.connect("tiktok.db")
    cur = conn.cursor()
    # create table
    drop_if_exists = "DROP TABLE IF EXISTS tiktok_video"
    cur.execute(drop_if_exists)

    create_tt_video = """ CREATE TABLE tiktok_video(
    user_name TEXT,
    user_id INT,
    video_id INT,
    video_desc TEXT,
    video_time INT,
    video_length INT,
    video_link TEXT, 
    n_likes INT,
    n_shares INT,
    n_comments INT,
    n_plays INT
    );
    """
    cur.execute(create_tt_video)
    insertion = "INSERT INTO tiktok_video \
        (user_name,user_id,video_id,video_desc,video_time,video_length,video_link,n_likes,n_shares,n_comments,n_plays)\
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    tt_csv = open("./trending_videos.csv", encoding="utf8")
    data = csv.reader(tt_csv)
    cur.executemany(insertion, data)
    return cur

def get_root_message():
    ''' Generate root page message '''
    message = []
    message.append("Hello, this is an api to query info about TikTok!\n")
    message.append("Table infor summary\n")
    message.append(
        "| Column name | Description                                                          |\n\
                    |-------------|----------------------------------------------------------------------|\n\
                    | user_name   | The name of the user who posted the video. (String)                  |\n\
                    | user_id     | The id of the user who posted the video. (Integer)                   |\n\
                    | video_id    | The id of the posted video. (Integer)                                |\n\
                    | video_desc  | The description of the posted video. (String)                        |\n\
                    | video_time  | The posted time of the video. (Integer)                              |\n\
                    | video_length| The length of the posted video. (Integer)                            |\n\
                    | video_link  | The link of the posted video. (String)                               |\n\
                    | n_likes     | The number of likes the video has received. (Integer)                |\n\
                    | n_shares    | The number of shares the video has received. (Integer)               |\n\
                    | n_comments  | The number of comments the video has received. (Integer)             |\n\
                    | n_plays     | The number of times the video has been played. (Integer) expand_less |\n"
    )
    message.append("Supported APIs:\n")
    message.append("/query/getAuthor: retrieve the authors' info given specifications\n")
    message.append("/query/getTrendingVideo: retrieve the trending videoes' info given predetermined thresholds\n")
    message.append("/query/filterVideo: retrieve the info of videoes where the contens follow the pattern in description")
    return "".join(message)


def get_author_query(likes, shares, comments, plays):
    """Generate the sql query for get_author"""
    builder = []
    builder.append("SELECT user_id, user_name FROM tiktok_video WHERE n_likes >")
    builder.append(str(likes))
    builder.append(" OR n_shares >")
    builder.append(str(shares))
    builder.append(" OR n_comments >")
    builder.append(str(comments))
    builder.append(" OR n_plays > ")
    builder.append(str(plays))
    builder.append(" LIMIT 5")
    return "".join(builder)


def get_trending_video_query(likes, shares, comments, plays):
    """Generate the sql query for get_author"""
    builder = []
    builder.append(
        "SELECT video_id, video_desc, video_time, video_length, video_link\
        FROM tiktok_video WHERE n_likes >"
    )
    builder.append(str(likes))
    builder.append(" OR n_shares >")
    builder.append(str(shares))
    builder.append(" OR n_comments >")
    builder.append(str(comments))
    builder.append(" OR n_plays > ")
    builder.append(str(plays))
    builder.append(" LIMIT 5")
    return "".join(builder)


def get_video_filter(description):
    """Generate Video filter query"""
    builder = []
    builder.append(
        "SELECT video_id, video_link FROM tiktok_video WHERE video_desc LIKE "
    )
    builder.append("'%")
    builder.append(description)
    builder.append("%'")
    builder.append(" LIMIT 5")
    return "".join(builder)


def query_to_str(query_result):
    """Make query result to string"""
    builder = []
    for q_r in query_result:
        builder.append(str(q_r))
        builder.append(",")
    return "".join(builder)


def gen_response(sql, result_str):
    """Generate API response"""
    return {"sql": sql, "result": result_str}


if __name__ == "__main__":
    cursor = db_setup()
    QUERY = "SELECT user_id, user_name\
         FROM tiktok_video\
         WHERE n_likes > 10000 OR n_shares > 100000 OR n_comments > 1000 OR n_plays > 100 LIMIT 3;"
    res = cursor.execute(QUERY).fetchall()
    for r in res:
        print(r)
