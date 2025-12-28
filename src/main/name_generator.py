from randomuser import RandomUser
import json

def generate_fake_profiles(num_profiles):
    allowed_nats = [
        "US", "GB", "FR", "DE", "IN", "JP", "CN",
        "KR", "TH", "VN", "PH", "BR", "AR", "MX", "CL", "CO"
    ]

    r = RandomUser({'nat': ','.join(allowed_nats)})
    users = r.generate_users(num_profiles)

    data = []
    for user in users:
        profile = {
            "First Name": user.get_first_name(),
            "Last Name": user.get_last_name(),
            "Phone" : user.get_phone(),
            "Country": user.get_country(),
            "State" : user.get_state(),
            "City" : user.get_city(),
            "Address" : user.get_street()
        }
        data.append(profile)

    return data

if __name__ == "__main__":
    df = generate_fake_profiles(100000)

    with open("../data_libraries/fake_person_profiles.json", "w", encoding="utf-8") as f:
        json.dump(df, f, ensure_ascii=False, indent=2)
