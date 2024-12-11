''' s '''
import requests

keys = [343311, 343311, 343392]

DATA = ",".join(str(key) for key in keys)
url = f"https://reference.medscape.com/druginteraction.do?action=getMultiInteraction&ids={DATA}"

r = requests.get(url=url, timeout=1000)
print(r.json())
