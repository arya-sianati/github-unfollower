from selenium import webdriver


def unfollower(url):
    firefox.get(url)

    # Find unfollow button
    elem = firefox.find_elements_by_xpath("//input[@value='Unfollow']")
    for i in elem:
        i.click()


firefox = webdriver.Firefox(executable_path="geckodriver.exe")

# Open browser and load the login page and you login to your github account then press enter
firefox.get("https://github.com/login")
input("Log in to your account and then press Enter button.")
username = input("Enter your username : ")
url = "https://github.com/" + username + "?tab=following"

while 1:
    unfollower(url)
