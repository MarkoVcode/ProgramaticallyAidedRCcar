from websocket import create_connection

ws = create_connection("wss://metrics-on-cloud.appspot.com/chat")
print "Sending 'Hello, World'..."
ws.send("[\"chat message\",\"sdsdsd\"]")
print "Sent"
print "Reeiving..."
result =  ws.recv()
print "Received '%s'" % result
ws.close()