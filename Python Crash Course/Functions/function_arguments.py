
def sandwiches(*items):
    print("The following sandwich has: ")
    for item in items:
        print(f"-{item}")
    print("\n")

sandwiches("whatzapp", "sex123", "milho verde")
sandwiches("goiabada", "queijo", "quiabo", "moeda")

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value

    return profile

user_profile = build_profile('Noise', 'LOL', alcoolatra='yes', fumante='yes')
print(user_profile)