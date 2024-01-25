import requests

def get_droplets_info(api_token):
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json',
    }

    response = requests.get('https://api.digitalocean.com/v2/droplets', headers=headers)

    if response.status_code == 200:
        droplets = response.json().get('droplets', [])
        droplets_info = {}

        for droplet in droplets:
            name = droplet.get('name', '')
            ip_info = droplet.get('networks', {}).get('v4', [])
            if ip_info:
                ip_address = ip_info[1]['ip_address']
                group = name.split('.')[2]  # Extract the group from the droplet name
                key = f'lamp_{group}' if group != 'memcached' else 'lamp_memcached'

                if key not in droplets_info:
                    droplets_info[key] = []

                droplets_info[key].append((name, ip_address))

        return droplets_info

    return {}
    
def write_hosts_file(api_token, output_file='hosts.ini'):
    droplets_info = get_droplets_info(api_token)

    with open(output_file, 'r') as existing_file:
        existing_content = existing_file.read()

    with open(output_file, 'a') as file:
        for group, droplets in droplets_info.items():
            # Check if group header already exists in the file
            if f'[{group}]' not in existing_content:
                file.write(f'\n[{group}]\n')

            for name, ip_address in droplets:
                # Check if IP already exists in the file
                if ip_address not in existing_content:
                    file.write(f'{ip_address}\n')

        # Add [all:vars] section if not already present
        all_vars_section = '\n[all:vars]\nansible_connection=ssh\nansible_user=root\n'
        if all_vars_section not in existing_content:
            file.write(all_vars_section)

if __name__ == "__main__":
    api_token = 'YOUR_API_TOKEN'
    write_hosts_file(api_token)
