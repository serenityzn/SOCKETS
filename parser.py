
#!/usr/bin/env python
import re
import sys

def get_lines( message ):
    error_code = 0
    line = 0
    prom = ""
    lines = []
    strlen = len( message )
    for i in range( 0, strlen ):
        prom += message[i]
        if  message[i] == '\n':
            lines.append(prom)
            prom = ""
            line += 1
    pattern = re.compile("^(HEAD|GET|POST|OPTIONS|PUT|DELETE|TRACE|CONNECT).(\/.*)\ (HTTP.*)$")
    if not pattern.match(lines[0]):
        error_code = 1

    return lines, error_code

def get_main_params(line):
    strlen = len(line)
    params = []
    prom = ""
    for i in range( 0, strlen ):
        if line[i] == " " or line[i] == "\r":
            params.append(prom)
            prom = ""
        else:
            prom += line[i]

    return params[0], params[1], params[2]
