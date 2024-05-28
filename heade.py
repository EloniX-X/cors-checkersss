from playwright.sync_api import sync_playwright, Playwright
reqs = []

def checkreqs(reqs):
    print(reqs)
    for req in reqs:
   
        print(req)
        f = open("exploit/all.txt", "w")
        f.write(str(req) + '\n')
        f.close()
        allowcreds = req[2]
        alloworigin = req[1]
        if allowcreds == "true" and alloworigin == "null":
            print("exploitable")
            f = open("exploit/exploitable.txt", "a")
            f.write(str(req) + '\n')
            f.close

        elif allowcreds == "true" and alloworigin == "null":
            f = open("exploitable.txt", "a")
            f.write(str(req) + '\n')
            f.close
        elif allowcreds == "true" and alloworigin == "*":
            print("not exploitable")
            print("not saved")
            print(":3")
        elif alloworigin == "None" and allowcreds == "None":
            print("none")

        if allowcreds == "true" and alloworigin != "*":
            print("allow creds")
            d = open("exploit/allowcreds.txt", "a")
            d.write(str(req) + '\n')
            d.close()




def run(playwright: Playwright):
    global reqs
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    # page.on("request", lambda request: reqs.extend((request.method, request.url)))
    page.on("response", lambda response: reqs.extend(([(response.url, response.header_value("Access-Control-Allow-Origin"), response.header_value("Access-control-allow-credentials"))])))
    page.goto("")#webysite goes here
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
    checkreqs(reqs)
