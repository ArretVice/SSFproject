import re


test_string = '''
Hello mister Anderson, is your e-mail adress MisterAnderson@matrix.com?
We would expect you to have something like Neo.is.a-cool_hackst3r@bullshit.ua, or maybe some +- actions?
Anything about 95823ufmlkwe@fda.balls seems familiar to you@. No?
'''

def get_list_of_emails(text):
    pattern = r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
    result = re.findall(pattern, text)
    return result

s='abra_cada+bra.@sample-mailservice.boring'

if __name__ == '__main__':
    print(get_list_of_emails(test_string))
