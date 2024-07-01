#real life program for API automation using match case
browser=str(input('Enter the browser name\n'))
browser=browser.lower()
match browser:
    case 'chrome':
        print('chrome code executed')
    case 'firefox':
        print('firefox code executed')
    case _:
        print('No browser found')