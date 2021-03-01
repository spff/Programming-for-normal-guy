from Lesson7 import net

s = net.requests_retry_session()
r = s.get('https://www.example.com')
r.raise_for_status()
print(r.text)

