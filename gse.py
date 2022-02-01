import sentry_sdk
sentry_sdk.init(
    "https://4d3e66b26cf74c04aabbxxxxxxxxxxxxx@o1132632.ingest.sentry.io/xxxxxxxx",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

division_by_zero = 1 / 0
