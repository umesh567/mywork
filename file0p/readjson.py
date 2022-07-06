import json

with open("blogs.json","r",encoding="utf-8") as f:
    data=json.load(f)
    print(data)

print(len(data))

#no of post by userId=1

num_post_by_user=[post for post in data if post["userId"]==1]
print(len(num_post_by_user))

#total number of likes for postid6

total_likes=[len(post["liked_by"]) for post in data if post["postId"]==6]
print(total_likes)

#no of post liked by user 2

liked_by_two=len([post for post in data if 2 in post["liked_by"]])
print(liked_by_two)

