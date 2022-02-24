import requests


class CloudflareApi:

    base_url = "https://api.cloudflare.com/client/v4"

    def __init__(self, api_token, zone_id):
        self.token = api_token
        self.zone_id = zone_id

    def patch_content_dns_record(self, record_id, new_content):
        url = self.base_url + f"/zones/{self.zone_id}/dns_records/{record_id}"
        headers = {"Authorization": "Bearer "+self.token}
        data = {"content": new_content}
        r = requests.patch(url, headers=headers, json=data)
        return r.json()

    def list_dns_records(self, record_name=None):
        url = self.base_url + f"/zones/{self.zone_id}/dns_records"
        headers = {"Authorization": "Bearer " + self.token}
        params = dict()
        if record_name is not None:
            params = {"name": record_name}
        r = requests.get(url, headers=headers, params=params)
        return r.json()

    def dns_record_details(self, record_id):
        url = self.base_url + f"/zones/{self.zone_id}/dns_records/{record_id}"
        headers = {"Authorization": "Bearer " + self.token}
        r = requests.get(url, headers=headers)
        return r.json()
