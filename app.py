from flask import Flask, jsonify
import instaloader

app = Flask(__name__)

@app.route("/")
def test():
    L = instaloader.Instaloader(
        download_pictures=False,
        download_videos=False,
        save_metadata=False
    )

    profile = instaloader.Profile.from_username(
        L.context,
        "kurtariciferat_yedi_54"
    )

    posts = []

    for post in profile.get_posts():
        posts.append({
            "caption": post.caption,
            "media": post.video_url if post.is_video else post.url,
            "thumbnail": post.url,
            "is_video": post.is_video
        })
        if len(posts) >= 5:
            break

    return jsonify(posts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
