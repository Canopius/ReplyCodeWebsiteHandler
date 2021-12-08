#Requires ChromeDriver in path or wd (google to download)
#pip install selenium
#If using multiple versions of py then use pip(VERSION) ...

from selenium import webdriver
import glob, os, time

driver = webdriver.Chrome()

def Login():
	Credentials = open(r"C:\Users\joshu\Documents\Creds.txt", "r")

	
	driver.get("https://challenges.reply.com/tamtamy/user/login.action")
	driver.implicitly_wait(60)
	EmailBox = driver.find_element(by="xpath", value="/html/body/div[5]/div/form/div/div[2]/div[3]/div[2]/div/div/input")
	PasswordBox = driver.find_element(by="xpath", value="/html/body/div[5]/div/form/div/div[2]/div[3]/div[3]/div/div[1]/input")
	LoginButton = driver.find_element(by="xpath", value="/html/body/div[5]/div/form/div/div[2]/div[3]/div[6]/div/button")

	EmailBox.send_keys(Credentials.readline())
	PasswordBox.send_keys(Credentials.readline())
	LoginButton.click()

	driver.get("https://challenges.reply.com/tamtamy/challenge/code-teen-2021/detail") # Change to correct page (Challenge page)
	AcceptCookies = driver.find_element(by="xpath", value="/html/body/div[1]/div/div[1]/div[2]/div[3]/div/div[1]/button")
	AcceptCookies.click()

	return True

def GetInput():
	# Make sure that the button is visible
	AllOldInput = glob.glob(r'C:\Users\joshu\Documents\ProgrammingProjects\ReplyChallenge\2022\Competiton\InputFile*')
	print(AllOldInput)
	for _, OldFile in enumerate(AllOldInput):
		os.remove(OldFile)

	driver.implicitly_wait(60)
	InputButton = driver.find_element(by="xpath", value="/html/body/div/div[7]/div/div/div/div/div/div/div/form/div/div/div[2]/div[3]/div/div[1]/div[3]/div[2]/div[1]/div[3]/span/div/span/div/div/div[2]/div[1]/button")
	InputButton.click()

	CrDownloads = glob.glob(r'C:\Users\joshu\Downloads\*.crdownload')
	while len(CrDownloads) >= 1:
		time.sleep(0.5)
		CrDownloads = glob.glob(r'C:\Users\joshu\Downloads\*.crdownload')

	AllDownloads = glob.glob(r'C:\Users\joshu\Downloads\*.txt') # * means all if need specific format then *.csv
	LastDownload = max(AllDownloads, key=os.path.getmtime)
	os.rename(LastDownload, r"C:\Users\joshu\Documents\ProgrammingProjects\ReplyChallenge\2022\Competiton\InputFile\Input.txt")

	return True


if __name__ == "__main__":
	Login()
	input()
	GetInput()
	input()