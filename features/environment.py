import os


def before_all(context):
    # 1) Check if user provided a base_url via the -D option
    base_url = context.config.userdata.get("BASE_URL")
    # 2) If not provided, fall back to an environment variable
    #    or a default localhost
    if not base_url:
        base_url = os.getenv("BASE_URL", "http://127.0.0.1:5000")

    context.base_url = base_url
    print(f"[BEHAVE] Using BASE URL: {context.base_url}")
