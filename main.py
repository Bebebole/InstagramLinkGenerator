import urllib.parse, pyshorteners

link = "twitter.com"

s = pyshorteners.Shortener()
l = s.isgd.short(link)
l = f"https://l.instagram.com/?u={urllib.parse.quote_plus(l)}&e=ATP0prj_k63aDaGZl2YtyRtW6vNQ0LHyFd8hQX4qVniihZ_teBGaSGzrKGl0_WQ4Rlb_BcWvvnzkxpLdyR3rgyM&s=1"

print(l)