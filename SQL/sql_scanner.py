#!/usr/bin/python

# Simple SQL Injection Vulnerability Scanner by Valentin Hoebel
# Version 0.3 (3rd June 2010)

# Contact me at valentin@xenuser.org
# ASCII FOR BREAKFAST

# Features:
# - Scan a single URL
# - Detect SQL injection vulnerabilities
# - User agent for web requests
# - User friendly (easy to use, everything is automated)
# - Error handling for http requests
# - Display a short scan report
# - Check if the provided URL is reachable

# This tool was not made for SQL injection experts, but for webmasters
# who want to scan their own websites for SQL injection vulnerabilities.
 
# I know that there are much better tools, but well, I do this for learning
# and understanding Python && SQL Injections.
# And ofc for fun!

# Attention: Tool is far away from being perfect, so don't rely a 100 percent on it.

# Known issue:
# For some reason sometimes a "500" error occurs while probing a parameter.
# The scanner then fails to detect vulnerabilities.
# Many other scripted vulnerability scanners have the same problem.
# error code 500 = internal server error
# It is the same with the error code 403.

# Greetz: JosS and Packet Storm staff (love this website!)
# THX to the darkc0de members, you really write awesome scripts!

# Tool was written for educational purposes only! Only scan websites you
# are allowed to test! Know and respect your local laws!
# I am not responsible if you or my script cause any damage or break laws.

# Power to the cows!

import sys,  re,  urllib,  urllib2,  string
from urllib2 import Request,  urlopen,  URLError,  HTTPError
from urlparse import urlparse

# Define the usage, the first thing a users sees if he/she starts the script without any parameter
def print_usage():
    print ""
    print ""
    print "________________________________________________"
    print "Simple SQL Injection Vulnerability Scanner"
    print "by Valentin Hoebel (valentin@xenuser.org)"
    print ""
    print "Version 0.3 (3rd June 2010)   ^__^"
    print "                              (oo)\________"
    print "                              (__)\        )\/\ "
    print "                                  ||----w |"
    print "Power to teh cows!                ||     ||"
    print "________________________________________________"
    print ""
    print "[!] Use parameter --help for help!"
    print ""
    print ""
    return
   
# Define the help message
def print_help():
    print ""
    print ""
    print "________________________________________________"
    print "Simple SQL Injection Vulnerability Scanner"
    print "by Valentin Hoebel (valentin@xenuser.org)"
    print ""
    print "Version 0.3 (3rd June 2010)   ^__^"
    print "                              (oo)\________"
    print "                              (__)\        )\/\ "
    print "                                  ||----w |"
    print "Power to teh cows!                ||     ||"
    print "________________________________________________"
    print ""
    print "The SQL Injection Vulnerability Scanner helps you"
    print "to find SQL injection vulnerabilities within a"
    print "website. It is not perfect so don't rely a 100% on it!"
    print ""
    print "Usage example:"
    print "sqli_scanner.py -u \"http://target/index.php?var1=x&var2=y\""
    print ""
    print "Options:"
    print " -u <URL>   (starts the scanner)"
    print " --help     (displays this text)"
    print ""
    print "Features:"
    print " - Scan a single URL"
    print " - Detect SQL injection vulnerabilities"
    print " - User agent for web requests"
    print " - User friendly (easy to use, everything is automated"
    print " - Error handling for http requests"
    print " - Display a short scan report"
    print " - Check if the provided URL is reachable"
    print ""
    print "Log feature:"
    print "I did not include any log feature for various"
    print "reasons. Simply add \"> test.log\" at the end"
    print "of the command if you use linux. Example:"
    print "sqli_scanner.py -u http://target... > test.log"
    print ""
    print "Disclaimer:"
    print "Only use this tool to check websites you are"
    print "allowed to test (e.g. for penetration testing)."
    print "Nerver use this tool on foreign websites!"
    print "Know and respect your local laws!"
    print "I am not responsible if you cause any damage or"
    print "run into trouble."
    print ""
    print "This tool was written for educational purposes only."
    print ""
    print ""
    return

# Define the banner which is printed when the tool was started with parameters
def print_banner():
    print ""
    print ""
    print "________________________________________________"
    print "Simple SQL Injection Vulnerability Scanner"
    print "by Valentin Hoebel (valentin@xenuser.org)"
    print ""
    print "Version 0.3 (3rd June 2010)   ^__^"
    print "                              (oo)\________"
    print "                              (__)\        )\/\ "
    print "                                  ||----w |"
    print "Power to teh cows!                ||     ||"
    print "________________________________________________"
    return

# Define the function which tests if a URL is reachable
def test_URL(provided_url):
    # Define User-Agent variable, change it if you like!
    user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)"
    
    # Adding the User-Agent to the HTTP request (via GET) 
    request_URL = urllib2.Request(provided_url)
    request_URL.add_header("User-Agent",  user_agent)
    
    # Now let's do the HTTP request
    print "[.] Checking if a connection can be established..."
    try:
        http_request_for_test = urllib2.urlopen(request_URL)
    except HTTPError,  e:
        print "[!] The connection could not be established."
        print "[!] Error code: ",  e.code
        print "[!] Exiting now!"
        print ""
        print ""
        sys.exit(1)
    except URLError,  e:
        print "[!] The connection could not be established."
        print "[!] Reason: ",  e.reason
        print "[!] Exiting now!"
        print ""
        print ""
        sys.exit(1)
    else:
        print "[.] Connected to target! URL seems to be valid."
    return

# Scan the provided URL for a SQL injection vulnerability
def scan_URL(provided_url):
    # Define some variables needed for detecting MySQL errors in the source code
    mysql_error_1 = "You have an error in your SQL syntax"
    mysql_error_2 = "supplied argument is not a valid MySQL result resource"
    mysql_error_3 = "check the manual that corresponds to your MySQL"
    param_equals = "="
    param_sign_1 = "?"
    param_sign_2 = "&"
    trigger_error_1 = "'"
    trigger_error_2 = "-1"
    
    # Define dict which will list all vulnerable parameters
    vulnerable_parameters = {}
    
    # Define User-Agent variable, change it if you like!
    user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)"
    
    # Adding the User-Agent to the HTTP request (via GET) 
    request_URL = urllib2.Request(provided_url)
    request_URL.add_header("User-Agent",  user_agent)
    
    # Starting the request
    try:
        http_request_for_call = urllib2.urlopen(request_URL)
    except HTTPError,  e:
        print "[!] The connection could not be established."
        print "[!] Error code: ",  e.code
        print "[!] Exiting now!"
        print ""
        print ""
        sys.exit(1)
    except URLError,  e:
        print "[!] The connection could not be established."
        print "[!] Reason: ",  e.reason
        print "[!] Exiting now!"
        print ""
        print ""
        sys.exit(1)  
    
    # Storing the response (source code of called website)
    html_call_URL_lite = http_request_for_call.read()
    
    # Paring the URL so we can work with it
    get_parsed_url = urlparse(provided_url)
    print ""
    print "[.] Moving on now."
    print "[.] Server/Domain is:",  get_parsed_url.netloc
    if len(get_parsed_url.path) == 0:
        print "[!] The URL doesn't contain a script (e.g. target/index.php)."
    else:
        print "[.] Detected the path to the script:",  get_parsed_url.path
    if len(get_parsed_url.query) == 0:
        print "[!] The URL doesn't contain a query string (e.g. index.php?var1=x&var2=y)."
    else:
        print "[.] Detected the URL query string:",  get_parsed_url.query
        print ""
    
    # Searching it for MySQL errors
    look_for_mysql_errors_1 = re.findall(mysql_error_1, html_call_URL_lite)
    if len(look_for_mysql_errors_1) != 0:
        print "[!] SQL error in the original URL/website found."
        print "[!] There might be problems exploiting this website (if it is vulnerable)."
    
    look_for_mysql_errors_2 = re.findall(mysql_error_2,  html_call_URL_lite)
    if len(look_for_mysql_errors_2) != 0:
        print "[!] SQL error in the original URL/website found."
        print "[!] There might be problems exploiting this website (if it is vulnerable)."
    
    look_for_mysql_errors_3 = re.findall(mysql_error_3,  html_call_URL_lite)
    if len(look_for_mysql_errors_3) != 0:
        print "[!] SQL error in the original URL/website found."
        print "[!] There might be problems exploiting this website (if it is vulnerable)."
    
    # Finding all URL parameters
    if param_sign_1 in provided_url and param_equals in provided_url:
        print "[.] It seems that the URL contains at least one parameter."
        print "[.] Trying to find also other parameters..."
        
        # It seems that there is at least one parameter in the URL. Trying to find out if there are also others...
        if param_sign_2 in get_parsed_url.query and param_equals in get_parsed_url.query:
            print "[.] Also found at least one other parameter in the URL."
        else:
            print "[.] No other parameters were found."
        
    else:
        print ""
        print "[!] It seems that there is no parameter in the URL."
        print "[!] How am I supposed to find a vulnerability?"
        print "[!] Please provide an URL with a script and query string."
        print "[!] Example: target/index.php?cat=1&article_id=2"
        print "[!] Hint: I can't handle SEO links, so try to find an URL with a query string."
        print "[!] Exiting now!"
        print ""
        print ""
        sys.exit(1)
    
    # Get the parameters
    # Thanks to atomized.org for the URL splitting and parameters parsing part!
    parameters = dict([part.split('=') for part in get_parsed_url[4].split('&')])

    # Count the parameters
    parameters_count = len(parameters)
    
    # Print the parameters and store them in single variables
    print "[.] The following", parameters_count, "parameter(s) was/were found:"
    print "[.]",  parameters
    print "[.] Starting to scan the provided URL(s) for SQL injection vulnerabilities."
    print ""

    # Have a look at each parameter and do some nasty stuff 
    for index, item in enumerate(parameters):
        # Now modify the original URL for triggering MySQL errors. Time to start your prayers :)
        print "[.] Probing parameter \"",  item, "\"..."
  
        # We now have to solve the problem that we can not modify tuples in the way we need it here.
        # We therefore copy the content of the query string (of the provided URL) into a new string.
        # The string can be modified as we like it :) Afterwards we only have to put the original URL together again.
        query_string_for_replacement = "".join(get_parsed_url[4:5])
        modified_query_string = query_string_for_replacement.replace(parameters[item],  trigger_error_1)

        # Put the URL together again
        # (Yeah I know, I am a real Python noob.)#      
        trigger_URL_1_part_1 = "".join(get_parsed_url[0:1]) + "://"
        trigger_URL_1_part_2 = "".join(get_parsed_url[1:2]) 
        trigger_URL_1_part_3 = "".join(get_parsed_url[2:3])  + "?"
        trigger_URL_1_part_4 = "".join(modified_query_string)  
        trigger_URL_1 = trigger_URL_1_part_1 + trigger_URL_1_part_2 + trigger_URL_1_part_3 + trigger_URL_1_part_4

        # Calling the modified URL
        try:
            http_request_trigger_1 = urllib2.urlopen(trigger_URL_1)
        except HTTPError,  e:
            print "[!] The connection could not be established."
            print "[!] Error code: ",  e.code
        except URLError,  e:
            print "[!] The connection could not be established."
            print "[!] Reason: ",  e.reason
    
        # Storing the response (source code of called website)
        html_call_URL_trigger_1 = http_request_trigger_1.read()

        # Searching the response for MySQL errors
        look_for_mysql_errors_trigger_1 = re.findall(mysql_error_1, html_call_URL_trigger_1)
        look_for_mysql_errors_trigger_2 = re.findall(mysql_error_2, html_call_URL_trigger_1)
        look_for_mysql_errors_trigger_3 = re.findall(mysql_error_3, html_call_URL_trigger_1)
        
        # If the first method was not successfull we simply try the next one
        if len(look_for_mysql_errors_trigger_1) == 0 and len(look_for_mysql_errors_trigger_2) == 0 and len(look_for_mysql_errors_trigger_3) == 0:
            modified_query_string = query_string_for_replacement.replace(parameters[item],  trigger_error_2)
            trigger_URL_2_part_1 = "".join(get_parsed_url[0:1]) + "://"
            trigger_URL_2_part_2 = "".join(get_parsed_url[1:2]) 
            trigger_URL_2_part_3 = "".join(get_parsed_url[2:3])  + "?"
            trigger_URL_2_part_4 = "".join(modified_query_string)  
            trigger_URL_2 = trigger_URL_2_part_1 + trigger_URL_2_part_2 + trigger_URL_2_part_3 + trigger_URL_2_part_4
            try:
                http_request_trigger_2 = urllib2.urlopen(trigger_URL_2)
            except HTTPError,  e:
                print "[!] The connection could not be established."
                print "[!] Error code: ",  e.code
            except URLError,  e:
                print "[!] The connection could not be established."
                print "[!] Reason: ",  e.reason
            
            html_call_URL_trigger_2 = http_request_trigger_2.read()
            look_for_mysql_errors_trigger_1 = re.findall(mysql_error_1, html_call_URL_trigger_2)
            look_for_mysql_errors_trigger_2 = re.findall(mysql_error_2, html_call_URL_trigger_2)
            look_for_mysql_errors_trigger_3 = re.findall(mysql_error_3, html_call_URL_trigger_2)
            
            if len(look_for_mysql_errors_trigger_1) == 0 and len(look_for_mysql_errors_trigger_2) == 0 and len(look_for_mysql_errors_trigger_3) == 0:
                print "[.] The parameter \"",  item,  "\" doesn't seem to be vulnerable."
        
        else:
            print "[+] Found possible SQL injection vulnerability! Parameter:", item
            vulnerable_parameters[index+1] = item
        
    # Generate a short report
    if len(vulnerable_parameters) != 0:
        print ""
        print "[#] Displaying a short report for the provided URL:"
        print "[#] At least one parameter seems to be vulnerable. "
        print "[#]",  vulnerable_parameters
        print "[#] (Pattern: param number, param name)"
    else:
        print ""
        print "[#] Displaying a short report for the provided URL:"
        print "[#] No SQL injection vulnerabilities found."

    # And exit
    print ""
    print "[.] That's it. Bye!"
    print ""
    print ""
    sys.exit(1)
    return
    # End of scan_url function
    

# Checking if argument was provided
if len(sys.argv) <=1:
    print_usage()
    sys.exit(1)
    
for arg in sys.argv:
    # Checking if help was called
    if arg == "--help":
        print_help()
        sys.exit(1)
    
    # Checking if  URL was provided, if yes -> go!
    if arg == "-u":
        provided_url = sys.argv[2]
        print_banner()
        
        # At first we test if we can actually reach the provided URL
        test_URL(provided_url)
        
        # Now start the main scanning function
        scan_URL(provided_url)
    