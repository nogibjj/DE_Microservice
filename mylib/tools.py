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


if __name__ == "__main__":
    cursor = db_setup()
    QUERY = "SELECT user_id, user_name\
         FROM tiktok_video\
         WHERE n_likes > 10000 OR n_shares > 100000 OR n_comments > 1000 OR n_plays > 100 LIMIT 3;"
    res = cursor.execute(QUERY).fetchall()
    for r in res:
        print(r)


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
