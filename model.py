import re #regular expressions module
def extract(text):
    name = r'\b[A-Z][a-z]+ [A-Z][a-z]*\b|\b[A-Z][a-zA-Z]{3,}\b' 
    # Assumes a simple pattern for names (First Last)
    address =  r'\b\d+\s+[A-Z][a-zA-Z\s,]+\b'
    # Assumes a simple pattern for addresses (123 Street City, ST)
    email= r'\S+@\S+'  # Basic email pattern[S-non negative whitespace,s-whitespace]
    phone =  r'\+\\d+s\d+[\s\d-]+'  # Basic phone number pattern
    dob= r'\d{2}/\d{2}/\d{4}'  # Date of birth pattern (MM/DD/YYYY)

    all_mapping = {}

    def replace_name(match):
        name = match.group(0)
        if name not in all_mapping:
            all_mapping[name] = f'{len(all_mapping) + 1}'
        return all_mapping[name]

    def replace_address(match):
        address = match.group(0)
        if address not in all_mapping:
            all_mapping[address] = f'{len(all_mapping) + 1}'
        return all_mapping[address]

    def replace_email(match):
        email = match.group(0)
        if email not in all_mapping:
            all_mapping[email] = f'{len(all_mapping) + 1}'
        return all_mapping[email]

    def replace_phone(match):
        phone = match.group(0)
        if phone not in all_mapping:
            all_mapping[phone] = f'{len(all_mapping) + 1}'
        return all_mapping[phone]

    def replace_dob(match):
        dob = match.group(0)
        if dob not in all_mapping:
            all_mapping[dob] = f'{len(all_mapping) + 1}'
        return all_mapping[dob]

    text = re.sub(address, replace_address, text)
    text = re.sub(name, replace_name, text)
    text = re.sub(phone, replace_phone, text)
    text = re.sub(email, replace_email, text)
    text = re.sub(dob, replace_dob, text)
    
    
    return [text,all_mapping]
