from getpass import getpass
import instaloader

username = input("Username: ")
password = getpass("Password: ")

L = instaloader.Instaloader()
L.login(username, password)
profile = instaloader.Profile.from_username(L.context, "amirhossein_hajian_")

f = open("followers.txt", "r")
old_followers = []
for line in f:
    old_followers.append(line.strip())
f.close()

new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower.username)

instagram_new_followers_finder = []
for new_follower in new_followers:
    if new_follower not in old_followers:
        instagram_new_followers_finder.append(new_follower)
print(instagram_new_followers_finder)

f = open("followers.txt", "w")
for new_follower in new_followers:
    f.write(new_follower + "\n")
f.close()