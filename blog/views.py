from blog.models import users,posts

session={}

#decorator ane ithe

def signin_required(fn):
    def wrapper (*args,**kwargs):
        if "user " in session:
            return fn(*args,**kwargs)
        else:
            print("invalid session you must log in")
    return wrapper


def authenticate (*args,**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")

    user=[user for user in users if user["username"]==username and user["password"]==password]
    return user
print(authenticate(username="akhil",password="Password@123"))

class LoginView:

    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
            session["user"]=user[0]
        print(session)

class postListviews:
    @signin_required
    def get (self,*args,**kwargs):
        return posts


class mypostlistview:
    @signin_required
    def get(self,*args,**kwargs):
        userid=session["user"]["id"]
        my_posts=[post for post in posts if post["userid"]==userid]
        return my_posts



log_in=LoginView()
log_in.post(username="akhil",password="Password@123")
all_post=postListviews()
print(all_post.get())
myposts=mypostlistview()
print(myposts.get())