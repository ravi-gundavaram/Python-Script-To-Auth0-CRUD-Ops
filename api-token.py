import http.client

conn = http.client.HTTPSConnection("dev-l00uxukorawizvqe.us.auth0.com")

payload = "{\"client_id\":\"hWEqfvU4PPXQFfiNSdAgpR2MADkRpl4l\",\"client_secret\":\"nX4OahZLl3EL2xaYrEKukcPXCSdfssPqaRfR2iPsRZH3zANHTPCNVUefr7Has6Ns\",\"audience\":\"https://dev-l00uxukorawizvqe.us.auth0.com/api/v2/\",\"grant_type\":\"client_credentials\"}"

headers = { 'content-type': "application/json" }

conn.request("POST", "/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))