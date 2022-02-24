import sys
from api import CloudflareApi
from ip_finder import IPFinder
from configurator import Configurator


def main():
    configurator = Configurator()

    token = configurator.config["api"]["token"]
    zone_id = configurator.config["api"]["zone_id"]
    api = CloudflareApi(token, zone_id)

    new_ip = IPFinder().get_my_ip()
    if not len(new_ip):
        print("New ip could not be discovered")
        sys.exit(1)

    record_name = configurator.config["dns"]["record_name"]
    old_record = api.list_dns_records(record_name)
    record_id = old_record["result"][0]["id"]
    old_ip = old_record["result"][0]["content"]

    if old_ip != new_ip:
        result = api.patch_content_dns_record(record_id, new_ip)
        if not result["success"]:
            print("Could not patch dns record:\n"+str(result["errors"]))
            sys.exit(2)
        else:
            print("Successfully patched:\n"+f"{old_ip} -> {new_ip}")
            sys.exit(0)
    else:
        print("New IP matches the old IP:\n"+new_ip)
        sys.exit(0)


if __name__ == "__main__":
    main()
